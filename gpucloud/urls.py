from django.urls import path

from gpucloud.views import GPUCloudView, GPUCloudTokenView

urlpatterns = [
    path(
        "gpucloud-fetch/",
        GPUCloudView.as_view(),
        name="gpucloud_fetch",
    ),
    path(
        "gpucloud-token/",
        GPUCloudTokenView.as_view(),
        name="gpucloud_token",
    ),
]
