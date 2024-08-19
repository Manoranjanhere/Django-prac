from django.url import path
from . import views 
urlpatterns = [
    path('hello/', views.say_hello),
]