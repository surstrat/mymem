from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'send_at', 'recipient_type', 'is_sent', 'created_by')
    list_filter = ('recipient_type', 'is_sent', 'send_at')
    search_fields = ('title', 'text')