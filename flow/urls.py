from django.urls import path

from flow.views import FlowList, WechatProgramLoginImage, UploadAPIView

urlpatterns = [
    path('api/upload/', UploadAPIView.as_view(), name='upload_api'),
    path("flows/", FlowList.as_view()),
    path("qrcode/", WechatProgramLoginImage.as_view()),
]
