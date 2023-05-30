from django.db import models
from users.models import User
from datetime import datetime

class AlertStatus(models.Model):
    status = models.CharField(max_length=200, blank=False, default="Created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "alert_status"

    def __str__(self):
        return { "status" : self.status }

class Alert(models.Model):
    price = models.IntegerField(blank=False,)
    type = models.BooleanField(default=True)
    status = models.ForeignKey(AlertStatus, verbose_name="status", null=True, db_index=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, to_field="username", verbose_name="User", null=True, db_index=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "alert"

    def __str__(self):
        return { "user_id" : self.created_by, "price":self.price }
    