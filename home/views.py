from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json

from .forms import VolunteerForm, DonationForm
from .models import DonatedDetail


from django.shortcuts import render, redirect
from django.conf import settings

def login_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        
        valid_passwords = [
            settings.PASSWORD1,
            settings.PASSWORD2,
            settings.PASSWORD3
        ]
        
        if password in valid_passwords:
            # Simulating user login (session handling)
            request.session['user'] = 'authenticated'
            return redirect('donated_details')
        else:
            return render(request, 'login.html', {'error': 'Invalid password'})
    
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('login')

@login_required(login_url='/login/')
def donated_details(request):
    donations = DonatedDetail.objects.all()
    return render(request, 'donated_details.html', {'donations': donations})

@csrf_exempt
def confirm_donation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            donation_id = data.get('donation_id')
            print(f"Received donation_id: {donation_id}")  # Debugging statement
            
            donation = get_object_or_404(DonatedDetail, id=donation_id)
            print(f"Found donation: {donation}")  # Debugging statement

            donation.is_confirmed = True
            donation.save()
            # Send email
            send_mail(
                'Donation Confirmed',
                'Thank you for your donation. It has been confirmed.',
                settings.EMAIL_HOST_USER,
                [donation.res_email],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except DonatedDetail.DoesNotExist:
            print("Donation not found")  # Debugging statement
            return JsonResponse({'success': False, 'error': 'Donation not found'})
        except Exception as e:
            print(f"Unexpected error: {e}")  # Debugging statement
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def index(request):
    initial_reviews = [
        {'text': "Great service, loved the food!", 'author': "John Doe"},
        {'text': "Very impressed with their commitment to reducing food wastage.", 'author': "Jane Smith"},
        {'text': "Helpful staff and quick response.", 'author': "Michael Brown"},
        {'text': "Amazing initiative to fight hunger!", 'author': "Emily Johnson"},
    ]
    return render(request, 'index.html', {'reviews': initial_reviews})

def about_us(request):
    return render(request, 'about_us.html')

def donate_food(request):
    if request.method == "POST":
        # Retrieve form data
        meal_type = request.POST.get('meal-type')
        breakfast = 'breakfast' in request.POST.getlist('meal-time')
        breakfast_quantity = request.POST.get('breakfast-quantity')
        breakfast_time = request.POST.get('breakfast-time')
        lunch = 'lunch' in request.POST.getlist('meal-time')
        lunch_quantity = request.POST.get('lunch-quantity')
        lunch_time = request.POST.get('lunch-time')
        dinner = 'dinner' in request.POST.getlist('meal-time')
        dinner_quantity = request.POST.get('dinner-quantity')
        dinner_time = request.POST.get('dinner-time')
        meal_prepared = request.POST.get('meal-prepared')

        # Save form data to session
        request.session['donation'] = {
            'meal_type': meal_type,
            'breakfast': breakfast,
            'breakfast_quantity': breakfast_quantity,
            'breakfast_time': breakfast_time,
            'lunch': lunch,
            'lunch_quantity': lunch_quantity,
            'lunch_time': lunch_time,
            'dinner': dinner,
            'dinner_quantity': dinner_quantity,
            'dinner_time': dinner_time,
            'meal_prepared': meal_prepared,
        }

        return redirect('donated_us')
    return render(request, 'donate_food.html')

def donated_us(request):
    donation = request.session.get('donation', {})
    if request.method == 'POST':
        form = DonationForm(request.POST)
        restaurant_name = request.POST.get('restaurant_name')
        restaurant_address = request.POST.get('restaurant_address')
        phone_number = request.POST.get('phone_number')
        res_email = request.POST.get('res_email')
                        
        donation.update({
        'restaurant_name': restaurant_name,
        'restaurant_address': restaurant_address,
        'phone_number': phone_number,
        'res_email': res_email,
        })
        donation_data = DonatedDetail(**donation)
        donation_data.save()
        return redirect('thanksu')
    else:
        form = DonationForm()

    return render(request, 'donated_us.html', {'form': form, 'donation': donation})

def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            # Save form with availability
            volunteer = form.save(commit=False)
            volunteer.save()

            print("Form saved successfully!")  # Debugging statement
            return redirect('thanku')  # Ensure 'thanku' matches URL pattern name
        else:
            print("Form is not valid")  # Debugging statement
    else:
        form = VolunteerForm()

    return render(request, 'volunteer.html', {'form': form})

def contact_us(request):
    return render(request, 'contact_us.html')

def article(request):
    return render(request, 'article.html')

def services(request):
    return render(request, 'services.html')

def thanku(request):
    return render(request, 'thanku.html')

def thanksu(request):
    return render(request, 'thanksu.html')
