from django.urls import path

from ai import views

app_name = 'ai'

urlpatterns = [
    path('upload_photo', views.upload_photo, name='upload_photo'),
]
