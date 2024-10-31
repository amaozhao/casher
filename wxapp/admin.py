from django.contrib import admin

from wxapp.models import WxAppUserProfile


@admin.register(WxAppUserProfile)
class WxAppUserProfileAdmin(admin.ModelAdmin):
    model = WxAppUserProfile
