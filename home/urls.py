from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('donate_food/', views.donate_food, name='donate_food'),
    path('donated_us/', views.donated_us, name='donated_us'),
    path('donated-details/', views.donated_details, name='donated_details'),
    path('confirm-donation/', views.confirm_donation, name='confirm_donation'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('article/', views.article, name='article'),
    path('services/', views.services, name='services'),
    path('thanku/', views.thanku, name='thanku'),
    path('thanksu/', views.thanksu, name='thanksu'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
