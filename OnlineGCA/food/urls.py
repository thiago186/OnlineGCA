from . import views
from django.urls import path

urlpatterns = [
    path('', views.TestItem, name = 'TestItemView'),
    path('home/', views.TestHomeView, name = 'TestHomeView'),
    path('food/', views.TestItem, name = 'TestItemView'),
    path('<int:item_id>/', views.TestDetailView, name = 'TestItemDetails')
]
