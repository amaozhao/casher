from django.urls import path
from task.views import ImageUploadView, PromptView, ImageDisplayView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('prompt/', PromptView.as_view(), name='prompt'),
    path('view/', ImageDisplayView.as_view(), name='view')
]
