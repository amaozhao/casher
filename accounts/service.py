from django.conf import settings
import urllib.parse
from urllib.parse import urljoin
import json
from django.urls import reverse


def genarate_wx_url(techsid):
    redirect_uri = urllib.parse.quote_plus(
        urljoin("https://test.aidep.cn", reverse("weixin_callback"))
    )
    state = {"techsid": techsid}
    state = urllib.parse.quote_plus(urllib.parse.quote_plus(json.dumps(state)))
    url = (f'https://open.weixin.qq.com/connect/qrconnect'
                f'?appid={settings.WEIXINB_H5_APPID}&redirect_uri={redirect_uri}'
                f'&response_type=code&scope=snsapi_login&state={state}#wechat_redirect')
    return url
