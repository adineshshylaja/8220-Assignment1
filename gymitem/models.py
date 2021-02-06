from django.db import models
from django.utils import timezone
# Create your models here.

class Gymitem(models.Model):
    Gymitem_name = models.CharField(max_length=100)
    Gymitem_id = models.CharField(max_length=100, blank=True)
    Gymitem_description = models.TextField()
    Gymitem_category = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Gymitem_name)