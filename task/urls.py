from django.urls import path

from task.views import (
    ImageDisplayView,
    ImageUploadView,
    PromptCompleted,
    PromptView,
    TaskHistoryDeleteView,
    TaskHistoryView,
    TaskHistoryDetailView,
    TaskHistoryDeleteViewV2
)

urlpatterns = [
    path("upload/", ImageUploadView.as_view(), name="image-upload"),
    path("prompt/", PromptView.as_view(), name="prompt"),
    path("completed/", PromptCompleted.as_view(), name="completed"),
    path("view/", ImageDisplayView.as_view(), name="view"),
    path("history/", TaskHistoryView.as_view(), name="history"),
    path(
        "history/delete/",
        TaskHistoryDeleteView.as_view(),
        name="history-delete",
    ),
    path(
        "history/delete/<int:id>/",
        TaskHistoryDeleteViewV2.as_view(),
        name="history-delete-v2",
    ),
    path(
        "history/detail/",
        TaskHistoryDetailView.as_view(),
        name="history-detail",
    ),
]
