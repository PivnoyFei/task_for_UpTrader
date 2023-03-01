from app.views import MenuView
from django.urls import path

urlpatterns = [
    path('', MenuView.as_view()),
    path('<slug:slug>', MenuView.as_view(), name='slug'),
]
