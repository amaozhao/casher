from django.contrib import admin
from task.models import TaskResult, UserTask


@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    model = UserTask


@admin.register(TaskResult)
class TaskResultAdmin(admin.ModelAdmin):
    model = TaskResult
