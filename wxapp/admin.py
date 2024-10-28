from django.contrib import admin
from wxapp.models import WxAppUserProfile


@admin.register(WxAppUserProfile)
class FlowDataAdmin(admin.ModelAdmin):
    model = WxAppUserProfile
