from django.urls import path

from flow.views import (
    WorkFlowListView,
    WorkFlowDetailView,
    UploadAPIView,
    WorkFlowCommentList,
)

urlpatterns = [
    path("api/upload/", UploadAPIView.as_view(), name="upload_api"),
    path("flows/", WorkFlowListView.as_view()),
    path("flows/<int:id>/", WorkFlowDetailView.as_view()),
    path("comments/<int:workflow_id>/", WorkFlowCommentList.as_view(), name="flow_comments"),
]
