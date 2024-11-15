from django.urls import path

from wxappb.views import WxAppBLogin, WxQrCodeView

urlpatterns = [
    path("login/", WxAppBLogin.as_view(), name="wxappb_login"),
    path("b-qrcode/", WxQrCodeView.as_view(), name="b_qrcode"),

]
