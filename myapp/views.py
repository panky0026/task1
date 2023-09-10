from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UploadedImage

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    image = request.FILES.get('image')
    name = image.name
    UploadedImage.objects.create(name=name, image=image)
    return Response({'message': 'Image uploaded successfully'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_image_names(request):
    image_names = UploadedImage.objects.values_list('name', flat=True)
    return Response({'image_names': image_names})
