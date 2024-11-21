import requests
from datetime import datetime, timedelta
from allauth.socialaccount.models import SocialAccount
from wxappb.models import WxAppBUserProfile
from gpucloud.models import GPUAccount
from urllib.parse import urljoin


class GPUCloudService:
    base_url = "http://www.deploycloud.cn"

    def signin(self, data):
        return requests.post(urljoin(self.base_url, "/api/users/login"), json=data)

    def get_user_profile(self, user):
        wx_user = WxAppBUserProfile.objects.filter(user=user).first()
        data = {"id": user.id}
        if wx_user:
            data.update(
                {
                    "login_type": "wechat",
                    "name": wx_user.nick_name,
                    "avatar": wx_user.avatarUrl,
                    "wechat_union_id": wx_user.unionid,
                    "wechat_open_id": wx_user.user.username,
                }
            )
            unique_target = wx_user.unionid
        else:
            social_account = SocialAccount.objects.filter(user=user).first()
            extra_data = social_account.extra_data
            if social_account.provider == 'google':
                data.update(
                    {
                        "login_type": "google",
                        "name": extra_data.get('name'),
                        "avatar": extra_data.get('picture'),
                        "google_id": social_account.uid,
                        "google_email": extra_data.get('email'),
                    }
                )
            else:
                data.update(
                    {
                        "login_type": "wechat",
                        "name": extra_data.get('nickname'),
                        "avatar": extra_data.get('headimgurl'),
                        "wechat_union_id": extra_data.get('unionid'),
                        "wechat_open_id": extra_data.get('openid'),
                    }
                )
            unique_target = social_account.extra_data.get(
                "unionid"
            ) or social_account.extra_data.get("email")
        return data, unique_target

    def get_token(self, user, refresh=False):
        account = GPUAccount.objects.filter(user=user).first()
        data, unique_target = self.get_user_profile(user)
        if not account:
            response = self.signin(data)
            token = response.json().get("data").get("token")
            GPUAccount.objects.create(
                user=user,
                unique_target=unique_target,
                token=token,
                expired=datetime.now() + timedelta(hours=5),
            )
            return token
        if refresh:
            response = self.signin(data)
            token = response.json().get("data").get("token")
            account.token = token
            account.expired = datetime.now() + timedelta(hours=5)
            account.save()
            return token
        return account.token

    def request_data(self, url, user, method, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"bearer {self.get_token(user, True)}"
        }
        request_method = getattr(requests, method)
        if method == "get":
            response = request_method(
                urljoin(self.base_url, url), headers=headers, params=data
            )
            return response
        response = request_method(urljoin(self.base_url, url), headers=headers, json=data)
        return response

    def get_longest_gpu(self, user):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"bearer {self.get_token(user, True)}"
        }
        response = requests.get(
            urljoin(self.base_url, '/api/capps'), headers=headers, params={}
        )
        containers = response.json().get('data', {}).get('containers', [])

        def compare_time(a):
            start = a.get('StartTime')
            start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            end = a.get('EndTime')
            end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            return (end - start).total_seconds() > 30 * 24 * 3600
        containers = [c for c in containers if compare_time(c)]
        return containers[0] if containers else None


gpucloud_service = GPUCloudService()


if __name__ == "__main__":
    response = gpucloud_service.request_data(
        url="/api/users/credit-cards", user=None, method="get", data={}
    )
    print(response.json())
