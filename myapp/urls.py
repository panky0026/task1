from django.urls import path
from myapp.views import upload_image, get_image_names

urlpatterns = [
    path('api/upload/', upload_image, name='upload_image'),
    path('api/images/', get_image_names, name='get_image_names'),
]
