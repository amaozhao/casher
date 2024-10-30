from django.urls import path

from wxapp.views import WxAppLogin

urlpatterns = [
    path("login/", WxAppLogin.as_view(), name="wxapp_login"),
]
