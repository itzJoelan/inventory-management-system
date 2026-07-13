from django.contrib import admin
from .models import ActivityLog, Notification

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'model', 'timestamp']
    list_filter = ['timestamp', 'model']
    search_fields = ['user__username', 'action']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'notification_type', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read', 'created_at']
    search_fields = ['user__username', 'title']
