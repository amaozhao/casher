from django.urls import path

from wxappb.views import WxAppBLogin

urlpatterns = [
    path("login/", WxAppBLogin.as_view(), name="wxappb_login"),
]
