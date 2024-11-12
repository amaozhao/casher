from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cash_statistics.models import CashStatistics


class CashStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        cash_stat = CashStatistics.objects.filter(user=user).first()
        if not cash_stat:
            cash_stat = CashStatistics.objects.create(inviter=user)
        return Response(
            {
                "data": {
                    "statistics": {
                        "cashable": cash_stat.cashable,
                        "withdrawing": cash_stat.withdrawing,
                        "withdrawned": cash_stat.withdrawned,
                        "total_income": cash_stat.total_income,
                        "in_transit": cash_stat.in_transit,
                        "refunded": cash_stat.refunded,
                    },
                    "status": status.HTTP_200_OK,
                }
            }
        )
