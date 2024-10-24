from django.contrib import admin
from flow.models import WorkFlowData


@admin.register(WorkFlowData)
class FlowDataAdmin(admin.ModelAdmin):
    model = WorkFlowData
