from django.urls import path

from landingpage import views

app_name = 'landingpage'

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landingpage'),
    path('login/', views.Login.as_view(), name='login'),
    path('terms/', views.Terms.as_view(), name='terms'),
    path('privacy/', views.Privacy.as_view(), name='privacy'),
]
