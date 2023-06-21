from django.urls import path
from .views import home, profile, RegisterView,prompt

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('prompt/', prompt, name='users-prompt'),
    path('profile/', profile, name='users-profile'),
]
