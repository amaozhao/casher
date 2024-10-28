from django.urls import path

from account.views import (
    GoogleLoginView,
    GoogleCallback,
    GoogleLoginUrl,
)

urlpatterns = [
    path("google/login_url/", GoogleLoginUrl.as_view(), name='google_login_url'),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("google/callback/", GoogleCallback.as_view(), name="flow_google_callback"),
]