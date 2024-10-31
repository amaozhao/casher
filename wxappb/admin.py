from django.contrib import admin

from wxappb.models import WxAppBUserProfile


@admin.register(WxAppBUserProfile)
class WxAppBUserProfileAdmin(admin.ModelAdmin):
    model = WxAppBUserProfile
