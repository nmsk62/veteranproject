from django.urls import path
from .views import add_user


urlpatterns = [
	path('user/', add_user, name='add_user'),
]
