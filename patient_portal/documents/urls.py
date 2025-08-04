

from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentListView.as_view(), name='document-list'),
    path('upload/', views.DocumentUploadView.as_view(), name='document-upload'),
    path('<int:pk>/', views.DocumentDownloadView.as_view(), name='document-download'),
    path('<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document-delete'),
]
