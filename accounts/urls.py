from django.urls import path

from accounts.views import (
    GoogleLoginView,
    GoogleCallback,
    GoogleLoginUrl,
    WechatQRLogin, WechatCallback
)

urlpatterns = [
    path("google/login_url/", GoogleLoginUrl.as_view(), name='google_login_url'),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("google/callback/", GoogleCallback.as_view(), name="google_callback"),

    path("weixin/login_url/", WechatQRLogin.as_view(), name='weixin_login_url'),
    path("weixin/login/", WechatQRLogin.as_view(), name="weixin_login"),
    path("weixin/callback/", WechatCallback.as_view(), name="weixin_callback"),
]