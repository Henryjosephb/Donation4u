from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donor_form_view, name='donate'),
    path('thank-you/', lambda request: render(request, 'donations/thank_you.html'), name='thank_you'),

]
