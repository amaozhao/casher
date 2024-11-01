from django.urls import path

from flow.views import (
    UploadAPIView,
    WorkFlowCommentList,
    WorkFlowDetailView,
    WorkFlowListView,
    BWorkFlowListView,
    BWorkFlowDetailView,
)

urlpatterns = [
    path("api/upload/", UploadAPIView.as_view(), name="upload_api"),
    path("flows/", WorkFlowListView.as_view()),
    path("b_flows/", BWorkFlowListView.as_view()),
    path("flows/<int:id>/", WorkFlowDetailView.as_view()),
    path("b_flows/<int:id>/", BWorkFlowDetailView.as_view()),
    path(
        "comments/",
        WorkFlowCommentList.as_view(),
        name="flow_comments",
    ),
]
