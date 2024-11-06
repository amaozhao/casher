from django.contrib import admin

from flow.models import WorkFlowBanner, WorkFlowData, WorkFlowImage


@admin.register(WorkFlowData)
class FlowDataAdmin(admin.ModelAdmin):
    model = WorkFlowData


@admin.register(WorkFlowImage)
class WorkFlowImageAdmin(admin.ModelAdmin):
    model = WorkFlowImage


@admin.register(WorkFlowBanner)
class WorkFlowBannerAdmin(admin.ModelAdmin):
    model = WorkFlowBanner
