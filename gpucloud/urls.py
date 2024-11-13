from django.urls import path

from gpucloud.views import GPUCloudView

urlpatterns = [
    path(
        "gpucloud-fetch/",
        GPUCloudView.as_view(),
        name="gpucloud_fetch",
    ),
]
