from django.urls import path
from .views import home, registration_two

urlpatterns = [
    path('', home, name='home'),
    path('registration_two/', registration_two, name='registration_two'),
]