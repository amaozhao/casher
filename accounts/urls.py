from django.urls import path

from accounts.views import (GoogleCallback, GoogleLoginUrl, GoogleLoginView,
                            WXCallback, WXCallback, WXLoginAPIView, WXQRCodeAPIView)

urlpatterns = [
    path("google/login_url/", GoogleLoginUrl.as_view(), name="google_login_url"),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("google/callback/", GoogleCallback.as_view(), name="google_callback"),
    path("weixin/login_url/", WXQRCodeAPIView.as_view(), name="weixin_login_url"),
    path("weixin/login/", WXLoginAPIView.as_view(), name="weixin_login"),
    path("weixin/callback/", WXCallback.as_view(), name="weixin_callback"),
]
