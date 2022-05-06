from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeCreateView.as_view(), name='home'),
    path('registration_two/', views.RegistrationTwoCreateView.as_view(), name='registration_two'),
    path('registration_three/', views.RegistrationThreeCreateView.as_view(), name='registration_three'),
    path('registration_four/', views.DioceseFormCreateView.as_view(), name='registration_four'),
    path('registration_five/', views.ChurchCreateView.as_view(), name='registration_five'),
    path('registration_six/', views.DesignationCreateView.as_view(), name='registration_six'),
    path('registration_seven/', views.PhotoCreateView.as_view(), name='registration_seven'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)