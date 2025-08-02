from django.db import models
from django.contrib.auth.models import User

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_ml = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')  