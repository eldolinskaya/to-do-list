from django.contrib import admin
from django.urls import path
from list.views import ListHome, ListDetailView, AllListView, ListCreateView, ListUpdateView, ListDeleteView

urlpatterns = [
    path('list/', ListHome.as_view(), name='list-home'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='task'),
    path('list/alllist/', AllListView.as_view(), name='all-list'),
    path('list/create/', ListCreateView.as_view(), name='create-list'),
    path('list/update/<int:pk>/', ListUpdateView.as_view(), name='update-list'),
    path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='delete-list'),
]
