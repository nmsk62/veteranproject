from django.urls import path
from .import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('remember/', views.RememberListView.as_view(), name='remember-list'),
    path('remember/<int:pk>', views.RememberDetailView.as_view(), name='remember-detail'),
    path('ad', views.AdView.as_view(), name='ad-list'),
    path('<int:pk>/', views.AdDetail.as_view(), name='ad-detail'),
]
