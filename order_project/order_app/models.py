from django.db import models
from django.contrib import admin

class Order(models.Model):
    order_id = models.IntegerField(help_text='Enter order is:')
    order_name = models.CharField(max_length=100,help_text='Enter order name:')
    order_description = models.CharField(max_length=100,help_text='Enter order description:')
    quantity = models.IntegerField(help_text='Enter quantity:')
    order_date = models.DateField(help_text='Enter order date:')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_name', 'order_description', 'quantity', 'order_date')    
        
# Create your models here.
