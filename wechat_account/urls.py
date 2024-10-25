from django.urls import path
from views import GenerateWeixinQRCodeView


urlpatterns = [
    path('weixin/qr-login/', GenerateWeixinQRCodeView.as_view(), name='weixin_qr_login'),
]