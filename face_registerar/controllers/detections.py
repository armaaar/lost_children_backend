import json
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from helpers.base64_to_memory_image import base64_to_memory_image
from ..models.kid_image import KidImage

class DetectionView(View):
    """View for uploading and detecting images"""
    def post(self, request):
        """Upload image and detect faces in it"""
        data: dict = json.loads(request.body.decode('utf-8'))
        kid_image = KidImage(
            date_time = timezone.now(),
            state = data['state'],
            image = base64_to_memory_image(data['image']),
        )

        kid_image.save()

        return JsonResponse({
            'status': 'OK'
        })
