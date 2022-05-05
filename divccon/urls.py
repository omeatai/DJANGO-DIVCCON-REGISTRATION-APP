from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration_two/', views.registration_two, name='registration_two'),
    path('registration_three/', views.registration_three, name='registration_three'),
    path('registration_four/', views.registration_four, name='registration_four'),
    path('registration_five/', views.registration_five, name='registration_five'),
    path('registration_six/', views.registration_six, name='registration_six'),
    path('registration_seven/', views.PhotoCreateView.as_view(), name='registration_seven'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)