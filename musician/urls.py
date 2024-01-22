from django.urls import path
from . import views
urlpatterns = [
    path('add_musician/',views.musician, name='musician')
]
