import hashlib
import json
import time
import uuid

from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dj_rest_auth.utils import jwt_encode
from wxappb import service
from wxappb.models import AuthorTechs, WxAppBUserProfile


class WxAppBLogin(APIView):
    authentication_classes = []

    def post(self, request):
        params = request.data
        # 拿到小程序端提交的code
        if params.get("code"):
            # 调用微信code2Session接口,换取用户唯一标识 OpenID 和 会话密钥 session_key
            data = service.login(params.get("code"))
            if data:
                # 将openid 和 session_key拼接
                val = data["openid"] + "&" + data["session_key"]
                key = data["openid"] + str(int(time.time()))
                # 将 openid 加密
                md5 = hashlib.md5()
                md5.update(key.encode("utf-8"))
                key = md5.hexdigest()
                # 保存到redis内存库,因为小程序端后续需要认证的操作会需要频繁校验
                cache.set(key, val)
                raw_data = params.get("rawData") or "{}"
                raw_data = json.loads(raw_data)
                has_user = User.objects.filter(username=data["openid"]).first()
                # 用户不存在则创建用户
                if not has_user:
                    has_user = User.objects.create(
                        username=data["openid"], password=uuid.uuid4()
                    )
                    WxAppBUserProfile.objects.create(
                        user=has_user,
                        nick_name=raw_data.get("nickName"),
                        gender=raw_data.get("gender"),
                        city=raw_data.get("city"),
                        province=raw_data.get("province"),
                        country=raw_data.get("country"),
                        avatarUrl=raw_data.get("avatarUrl"),
                        unionid=data.get("unionid"),
                    )
                has_user.save()
                profile = WxAppBUserProfile.objects.filter(user=has_user).first()
                if not profile:
                    profile = WxAppBUserProfile.objects.create(
                        user=has_user,
                        nick_name=raw_data.get("nickName"),
                        gender=raw_data.get("gender"),
                        city=raw_data.get("city"),
                        province=raw_data.get("province"),
                        country=raw_data.get("country"),
                        avatarUrl=raw_data.get("avatarUrl"),
                        unionid=data.get("unionid"),
                    )
                else:
                    profile.nick_name = raw_data.get("nickName")
                    profile.gender = raw_data.get("gender")
                    profile.city = raw_data.get("city")
                    profile.province = raw_data.get("province")
                    profile.country = raw_data.get("country")
                    profile.avatarUrl = raw_data.get("avatarUrl")
                    profile.save()
                if params.get("techsid"):
                    tesh, _ = AuthorTechs.objects.get_or_create(
                        user=has_user, techsid=params.get("techsid"), provider="weixin"
                    )
                token, _ = jwt_encode(has_user)
                return Response(
                    data={
                        "status": status.HTTP_200_OK,
                        "message": "ok",
                        "data": {
                            "login_key": key,
                            "token": str(token),
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": status.HTTP_401_UNAUTHORIZED,
                        "message": "用户未登陆",
                        "data": {"msg": "code无效"},
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "参数缺失",
                    "data": {"msg": "缺少参数"},
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
