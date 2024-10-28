import requests
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView, OAuth2LoginView
from .provider import WxAppProvider

class WxAppOAuth2Adapter(WeixinOAuth2Adapter):
    provider_id = WxAppProvider.id

    def complete_login(self, request, app, token, response):
        # 构造小程序认证请求
        url = f"https://api.weixin.qq.com/sns/jscode2session"
        params = {
            "appid": app.client_id,
            "secret": app.secret,
            "js_code": token.token,  # 从小程序前端获取的登录code
            "grant_type": "authorization_code"
        }
        response = requests.get(url, params=params)
        extra_data = response.json()

        if "openid" in extra_data:
            login = self.get_provider().sociallogin_from_response(request, extra_data)
            return login
        else:
            raise Exception("Failed to retrieve openid from WeChat API")


oauth2_login = OAuth2LoginView.adapter_view(WeixinOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(WeixinOAuth2Adapter)