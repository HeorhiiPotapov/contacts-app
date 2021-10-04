from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.ContactsListView.as_view(), name='list'),
    path('delete/<int:pk>/', views.ContactsDestroyView.as_view(), name='delete'),
    path('create/', views.ContactsCreateView.as_view(), name='create')
]
