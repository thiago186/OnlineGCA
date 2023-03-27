from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.TestHomeView, name = 'TestHomeView'),
    path('item/', views.TestItem, name = 'TestItemView')
]