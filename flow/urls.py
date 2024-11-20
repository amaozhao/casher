from django.urls import path

from flow.views import (
    BWorkFlowDetailView,
    BWorkFlowListView,
    UploadAPIView,
    WorkFlowBannerView,
    WorkFlowCommentList,
    WorkFlowDetailView,
    WorkFlowListView,
    BWorkFlowTemplateView,
    ComfyUIView,
    WorkflowDownloadAPIView,
    ContactAPIView,
)

urlpatterns = [
    path("api/upload/", UploadAPIView.as_view(), name="upload_api"),
    path("flows/", WorkFlowListView.as_view()),
    path("b_flows/", BWorkFlowListView.as_view()),
    path("b_templates/", BWorkFlowTemplateView.as_view()),
    path("flows/<int:id>/", WorkFlowDetailView.as_view()),
    path("b_flows/<int:id>/", BWorkFlowDetailView.as_view()),
    path(
        "comments/",
        WorkFlowCommentList.as_view(),
        name="flow_comments",
    ),
    path(
        "banner/",
        WorkFlowBannerView.as_view(),
        name="flow_banner",
    ),
    path(
        "comfyui/",
        ComfyUIView.as_view(),
        name="comfyui",
    ),
    path(
        "download/",
        WorkflowDownloadAPIView.as_view(),
        name="flow_download",
    ),
    path(
        "contact/",
        ContactAPIView.as_view(),
        name="contact",
    ),
]
