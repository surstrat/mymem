from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    RECIPIENT_TYPE = [
        ('self', 'Себе'),
        ('user', 'Другому пользователю'),
        ('public', 'Публичная запись'),
    ]
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    recipient_type = models.CharField(max_length=10, choices=RECIPIENT_TYPE, default='self')
    recipient_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='incoming_reminders')
    send_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_reminders')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} -> {self.send_at}"