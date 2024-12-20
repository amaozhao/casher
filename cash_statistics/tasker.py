from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta

from allauth.socialaccount.models import SocialAccount
from cash_statistics.models import CashStatistics
from task.models import UserTask
from casher.celery_casher import app
from payment.models import PagsmilePayout, UserPayin, WechatPayout


@app.task(bind=True, ignore_result=True)
def update_statistics(self, user_id):
    user = User.objects.get(id=user_id)
    if not user:
        return
    socialaccount = SocialAccount.objects.filter(user=user).first()
    if socialaccount and socialaccount.get_provider() == "google":
        payout_cls = PagsmilePayout
    else:
        payout_cls = WechatPayout
    total_fee = UserPayin.objects.filter(user=user, status="success").aggregate(
        total_fee=Sum("fee")
    )["total_fee"]
    payouted_fee = payout_cls.objects.filter(user=user, status="success").aggregate(
        total_fee=Sum("fee")
    )["payouted_fee"]
    stat = CashStatistics.objects.filter(user=user).first()
    if not stat:
        CashStatistics.objects.create(
            user=user,
            cashable=(total_fee - payouted_fee),
            withdrawned=payouted_fee,
            total_income=total_fee,
        )
    else:
        stat.cashable = total_fee - payouted_fee
        stat.withdrawned = payouted_fee
        stat.total_income = total_fee
        stat.save()


@app.task(bind=True, ignore_result=True)
def update_task_result(self):
    current_time = now()
    one_hour_ago = current_time - timedelta(hours=1)
    UserTask.objects.filter(status='queue', updated__lt=one_hour_ago).update(status='fail')
