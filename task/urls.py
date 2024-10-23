from django.urls import path

from task.views import ImageDisplayView, ImageUploadView, PromptView, PromptCompleted

urlpatterns = [
    path("upload/", ImageUploadView.as_view(), name="image-upload"),
    path("prompt/", PromptView.as_view(), name="prompt"),
    path("completed/", PromptCompleted.as_view(), name="completed"),
    path("view/", ImageDisplayView.as_view(), name="view"),
]
