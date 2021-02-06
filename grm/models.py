from django.db import models
from django.utils import timezone
from gymitem.models import Gymitem
# Create your models here.
#class Customer(models.Model):
class Gymmember(models.Model):
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    account_number = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    joining_date = models.DateTimeField(
        default=timezone.now)
    ending_date = models.DateField()
    additional_comment = models.TextField(blank=True)

    def created(self):
        self.joining_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

class Rental(models.Model):
    cust_name = models.ForeignKey(Gymmember, on_delete=models.CASCADE, related_name='rentals')
    Gymitem_name = models.ForeignKey(Gymitem,on_delete=models.CASCADE, related_name='rentals')
    quantity = models.IntegerField(blank=False, null=False)
    Comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=timezone.now)

    def created(self):
       self.created_date = timezone.now()
       self.save()

    def updated(self):
       self.updated_date = timezone.now()
       self.save()

    def __str__(self):
       return str(self.cust_name)