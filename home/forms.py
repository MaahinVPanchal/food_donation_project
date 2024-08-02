from django import forms
from .models import Volunteer
from .models import DonatedDetail

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'email', 'phone', 'address', 'skills', 'additional_info']

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonatedDetail
        fields = ['meal_type', 'breakfast', 'breakfast_quantity', 'breakfast_time', 
                  'lunch', 'lunch_quantity', 'lunch_time', 
                  'dinner', 'dinner_quantity', 'dinner_time', 
                  'meal_prepared', 'restaurant_name', 'restaurant_address', 
                  'phone_number', 'res_email']