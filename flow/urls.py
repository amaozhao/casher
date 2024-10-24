from django.urls import path

from flow.views import (
    WorkFlowListView,
    WorkFlowDetailView,
    UploadAPIView,
    WechatQRLogin,
    WechatCallback,
    WechatMinAppLogin,
    GoogleLoginView,
    GoogleCallback,
    GoogleLoginUrl,
    WorkFlowCommentList,
)

urlpatterns = [
    path("api/upload/", UploadAPIView.as_view(), name="upload_api"),
    path("flows/", WorkFlowListView.as_view()),
    path("flows/<int:id>/", WorkFlowDetailView.as_view()),
    path("comments/<int:workflow_id>/", WorkFlowCommentList.as_view(), name="flow_comments"),
    path("wechat/qrcode/", WechatQRLogin.as_view(), name="wechat_qrcode"),
    path(
        "wechat/miniapp/auth/", WechatMinAppLogin.as_view(), name="wechat_miniapp_login"
    ),
    path("wechat/callback/", WechatCallback.as_view(), name="wechat_callback"),
    path("google/login_url/", GoogleLoginUrl.as_view(), name='google_login_url'),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("google/callback/", GoogleCallback.as_view(), name="flow_google_callback"),
]
