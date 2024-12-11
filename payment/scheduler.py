# your_app/scheduler.py

from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def create_weekly_billing_task():
    # 创建或获取每周任务调度
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="0",
        day_of_week="1",  # 每周一
        day_of_month="*",  # 每月每天
        month_of_year="*"
    )

    # 创建周期性任务
    PeriodicTask.objects.update_or_create(
        crontab=schedule,
        name="Weekly Billing Task",  # 任务唯一名称
        defaults={
            'task': 'payment.tasks.process_weekly_billing',  # 任务路径
            'args': json.dumps([]),  # 如果有参数，使用 JSON 格式
        },
    )

