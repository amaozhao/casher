from django.urls import path

from flow.views import FlowList, WechatProgramLoginImage

urlpatterns = [
    path("flows/", FlowList.as_view()),
    path('qrcode/', WechatProgramLoginImage.as_view())
]
