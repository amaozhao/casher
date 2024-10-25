from django.urls import path

from flow.views import (
    WorkFlowListView,
    WorkFlowDetailView,
    UploadAPIView,
    WechatCallback,
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
    path("wechat/callback/", WechatCallback.as_view(), name="wechat_callback"),
    path("google/login_url/", GoogleLoginUrl.as_view(), name='google_login_url'),
    path("google/login/", GoogleLoginView.as_view(), name="flow_google_login"),
    path("google/callback/", GoogleCallback.as_view(), name="flow_google_callback"),
]
