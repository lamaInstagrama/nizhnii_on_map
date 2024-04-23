from django.urls import path
from nizhnii import views

app_name = 'nizhnii'

urlpatterns = [
    path('map/', views.ShowMap.as_view(), name='map')
]