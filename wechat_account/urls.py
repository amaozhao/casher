from django.urls import path
from wechat_account.views import GenerateWeixinQRCodeView


urlpatterns = [
    path('weixin/qr-login/', GenerateWeixinQRCodeView.as_view(), name='weixin_qr_login'),
]