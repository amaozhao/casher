# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import time

from django.http import Http404, response
from django.test.utils import override_settings
from django.urls import reverse
import six
from six.moves.urllib.parse import urlencode
from wechatpy.client.api import WeChatJSAPI

from ..models import WeChatApp
from ..sites.wechat import WeChatSite, WeChatView, wechat_view
from .base import mock, WeChatTestCase


class WeChatSiteTestCase(WeChatTestCase):
    def test_app_queryset(self):
        """测试app_queryset正确"""
        that = self

        class TestSite(WeChatSite):
            @property
            def app_queryset(self):
                return WeChatApp.objects.filter(name=that.app.name)

        class TestView(WeChatView):
            def get(self, request, appname):
                return response.HttpResponse(status=204)

            def _get_appname(self, request, appname):
                return appname

        # 在app_queryset中的公众号可访问,否则404
        site = TestSite()
        view = site._create_view(TestView)
        resp = view(self.rf().get("/"), self.app.name)
        self.assertEqual(resp.status_code, 204)
        self.assertRaises(Http404, view, self.rf().get("/"), self.another_app.name)

    def test_wechat_view(self):
        """测试wechat_view"""
        that = self

        class View(WeChatView):
            app_queryset = WeChatApp.objects.filter(name=self.app.name)

            def post(self, request):
                that.assertEqual(request.wechat.app.id, that.app.id)
                that.assertEqual(request.wechat.appname, that.app.name)
                return response.HttpResponse(status=204)

            def _get_appname(self, request, *args, **kwargs):
                return that.app.name

        # 测试app_queryset
        with mock.patch.object(View, "_get_appname"):
            View._get_appname.return_value = self.another_app.name
            view = View.as_view()
            self.assertRaises(Http404, view, self.rf().post("/"))

        # 测试http method正确
        view = View.as_view()
        resp = view(self.rf().get("/"))
        self.assertEqual(resp.status_code, 405)
        resp = view(self.rf().post("/"))
        self.assertEqual(resp.status_code, 204)

        # 测试装饰器
        @wechat_view("^$", methods=["POST"])
        def View(request, appname):
            return response.HttpResponse(status=204)

        resp = View.as_view()(self.rf().get("/"), self.app.name)
        self.assertEqual(resp.status_code, 405)
        resp = View.as_view()(self.rf().post("/"), self.app.name)
        self.assertEqual(resp.status_code, 204)

    def test_jsapi(self):
        """测试jsapi"""
        with mock.patch.object(WeChatJSAPI, "get_jsapi_ticket"):
            ticket = "ticket"
            WeChatJSAPI.get_jsapi_ticket.return_value = "ticket"
            jsapi_list = ["onMenuShareTimeline", "onMenuShareAppMessage"]

            src = reverse("wechat_django:jsconfig", kwargs=dict(appname=self.app.name))
            querystr = urlencode(dict(jsApiList=",".join(jsapi_list)))
            referrer = "https://baidu.com/abc"

            resp = self.client.get(src + "?" + querystr, HTTP_REFERER=referrer)
            pattern = r"wx\.config\(JSON\.parse\('(.+)'\)\);"
            match = re.match(pattern, resp.content.decode())
            self.assertTrue(match)

            json_str = match.group(1)
            data = json.loads(json_str)

            debug = data.get("debug")
            appid = data["appId"]
            timestamp = data["timestamp"]
            noncestr = data["nonceStr"]
            js_api_list = data["jsApiList"]
            client = self.app.client
            signature = client.jsapi.get_jsapi_signature(
                noncestr, ticket, timestamp, referrer
            )

            self.assertFalse(debug)
            self.assertEqual(appid, self.app.appid)
            self.assertAlmostEqual(timestamp, time.time(), delta=3)
            self.assertIsInstance(timestamp, int)
            self.assertIsInstance(noncestr, six.string_types)
            self.assertTrue(noncestr)
            self.assertEqual(js_api_list, jsapi_list)
            self.assertEqual(signature, data["signature"])

            with override_settings(DEBUG=False):
                querystr = urlencode(dict(debug=True))
                resp = self.client.get(src + "?" + querystr, HTTP_REFERER=referrer)
                match = re.match(pattern, resp.content.decode())
                self.assertTrue(match)
                json_str = match.group(1)
                data = json.loads(json_str)

                self.assertFalse(data.get("debug"))

            with override_settings(DEBUG=True):
                resp = self.client.get(src + "?" + querystr, HTTP_REFERER=referrer)
                match = re.match(pattern, resp.content.decode())
                self.assertTrue(match)
                json_str = match.group(1)
                data = json.loads(json_str)

                self.assertTrue(data.get("debug"))

    def test_request(self):
        """测试请求响应正常,路由匹配正常"""
        pass
