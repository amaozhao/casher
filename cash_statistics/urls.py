from django.urls import path

from cash_statistics.views import CashStatisticsView

urlpatterns = [
    path(
        "cash-statistics/",
        CashStatisticsView.as_view(),
        name="cash_statistics",
    ),
]
