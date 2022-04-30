from django.urls import path
from .views import home, registration_two, registration_three, registration_four

urlpatterns = [
    path('', home, name='home'),
    path('registration_two/', registration_two, name='registration_two'),
    path('registration_three/', registration_three, name='registration_three'),
    path('registration_four/', registration_four, name='registration_four'),
]