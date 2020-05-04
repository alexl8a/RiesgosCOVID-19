from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('response/list/', views.ResponseList.as_view(), name='response_list'),
    path('response/add/', views.ResponseAdd.as_view(), name='response_add'),
    path('response/detail/<int:pk>/', views.ResponseDetail.as_view(), name='response_detail'),
    path('response/pdf/<int:pk>/',views.ResponsePdf.as_view(), name='response_pdf' ),
]