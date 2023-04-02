from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.TestItem, name = 'TestItemView'),
    path('home/', views.TestHomeView, name = 'TestHomeView'),
    path('food/', views.TestItem, name = 'TestItemView'),
    path('<int:item_id>/', views.TestDetailView, name = 'TestItemDetails'),
    path('addItem/', views.TestAddItem, name= 'AddItem'),
    path('updateItem/<int:item_id>/', views.TestUpdateItem, name= 'UpdateItem')
]
