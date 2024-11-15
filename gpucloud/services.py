import requests
from datetime import datetime, timedelta
from allauth.socialaccount.models import SocialAccount
from wxappb.models import WxAppBUserProfile
from gpucloud.models import GPUAccount
from urllib.parse import urljoin


class GPUCloudService:
    base_url = "http://www.deploycloud.cn"

    def signin(self, data):
        return requests.post(urljoin(self.base_url, "/api/c/signin"), json=data)

    def get_user_profile(self, user):
        wx_user = WxAppBUserProfile.objects.filter(user=user).first()
        data = {"id": user.id}
        if wx_user:
            data.update(
                {
                    "nickname": wx_user.nick_name,
                    "sex": wx_user.gender,
                    "city": wx_user.city,
                    "province": wx_user.province,
                    "country": wx_user.country,
                    "avatarUrl": wx_user.avatarUrl,
                    "unionid": wx_user.unionid,
                    "provider": "wxapp",
                }
            )
            unique_target = wx_user.unionid
        else:
            social_account = SocialAccount.objects.filter(user=user).first()
            data.update(social_account.extra_data)
            unique_target = social_account.extra_data.get(
                "unionid"
            ) or social_account.extra_data.get("email")
        return data, unique_target

    def get_token(self, user):
        account = GPUAccount.objects.filter(user=user).first()
        data, unique_target = self.get_user_profile(user)
        if not account or account.expired <= datetime.now():
            response = self.signin(data)
            token = response.json().get("data").get("token")
            GPUAccount.objects.create(
                user=user,
                unique_target=unique_target,
                token=token,
                expired=datetime.now() + timedelta(days=1),
            )
            return token
        return account.token

    def request_data(self, url, user, method, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"bearer {token}",
            # "Authorization": f"bearer {self.get_token(user)}"
        }
        request_method = getattr(requests, method)
        if method == "get":
            response = request_method(
                urljoin(self.base_url, url), headers=headers, params=data
            )
            return response
        response = request_method(url, headers=headers, json=data)
        return response


gpucloud_service = GPUCloudService()


if __name__ == "__main__":
    response = gpucloud_service.request_data(
        url="/api/users/credit-cards", user=None, method="get", data={}
    )
    print(response.json())
