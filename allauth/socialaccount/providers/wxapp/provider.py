from allauth.socialaccount.providers.weixin.provider import WeixinProvider


class WxAppProvider(WeixinProvider):
    id = "wxapp"  # 确保此ID唯一
    name = "WeChat Mini Program"

    def get_default_scope(self):
        # 小程序通常不使用额外的OAuth作用域
        return []
