from django.db import models

from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skills = models.TextField()
    additional_info = models.TextField(default='')  # Example default value for additional_info

    def __str__(self):
        return self.full_name

class DonatedDetail(models.Model):
    MEAL_TYPE_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('non-vegetarian', 'Non-Vegetarian'),
    ]
    
    MEAL_PREPARED_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE_CHOICES)
    breakfast = models.BooleanField(default=False)
    breakfast_quantity = models.PositiveIntegerField(default=0)
    breakfast_time = models.CharField(null=True, blank=True,max_length=2)
    lunch = models.BooleanField(default=False)
    lunch_quantity = models.PositiveIntegerField(default=0)
    lunch_time = models.CharField(null=True, blank=True,max_length=2)
    dinner = models.BooleanField(default=False)
    dinner_quantity = models.PositiveIntegerField(default=0)
    dinner_time = models.CharField(null=True, blank=True,max_length=2)
    meal_prepared = models.CharField(max_length=100, choices=MEAL_PREPARED_CHOICES)
    restaurant_name = models.CharField(max_length=200)
    restaurant_address = models.CharField(max_length=300)
    phone_number = models.IntegerField(max_length=10)
    res_email = models.EmailField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation from {self.restaurant_name}"
