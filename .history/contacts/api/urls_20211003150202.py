from django.urls import path
from . import views

urlpatterns = [
    path('contacts/list', views.ContactsListView.as_view(), name='api-list'),
    path('contacts/destroy/<int:pk>/',
         views.ContactsDestroyView.as_view(), name='api-distroy'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='api-create')
]
