from django.urls import path
from .views import OrderCreateView

# app_name = 'order'
urlpatterns = [
    path('create/', OrderCreateView.as_view()),
]
