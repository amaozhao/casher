from django.urls import path

from flow.views import (
    WorkFlowList,
    UploadAPIView,
    WechatQRLogin,
    WechatCallback,
    WechatMinAppLogin,
    GoogleLoginView,
    GoogleLoginCallback,
    GoogleLoginUrl,
)

urlpatterns = [
    path("api/upload/", UploadAPIView.as_view(), name="upload_api"),
    path("flows/", WorkFlowList.as_view()),
    path("wechat/qrcode/", WechatQRLogin.as_view(), name="wechat_qrcode"),
    path(
        "wechat/miniapp/auth/", WechatMinAppLogin.as_view(), name="wechat_miniapp_login"
    ),
    path("wechat/callback/", WechatCallback.as_view(), name="wechat_callback"),
    path("google/loginurl/", GoogleLoginUrl.as_view(), name='google_login_url'),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("google/callback/", GoogleLoginCallback.as_view(), name="google_callback"),
]
