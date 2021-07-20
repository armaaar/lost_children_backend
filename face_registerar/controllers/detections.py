import json
import face_recognition
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from helpers.base64_to_memory_image import base64_to_memory_image
from ..utils.serialize_encodings import serialize_encoding
from ..models.kid_image import KidImage
from ..models.kid_face import KidFace
from ..errors import err

class DetectionView(View):
    """View for uploading and detecting images"""
    def post(self, request):
        """Upload image and detect faces in it"""
        data: dict = json.loads(request.body.decode('utf-8'))
        # Create image
        kid_image = KidImage(
            date_time = timezone.now(),
            state = data['state'],
            image = base64_to_memory_image(data['image']),
        )

        # Get face encodings
        image = face_recognition.load_image_file(kid_image.image)
        face_locations: list = face_recognition.face_locations(image)

        if len(face_locations) == 0:
            return err('no_face')

        face_encodings: list = face_recognition.face_encodings(image)
        faces: list[KidFace] = []
        for index in range(len(face_locations)):
            faces.append(KidFace(
                image = kid_image,
                location = json.dumps(face_locations[index]),
                encoding = serialize_encoding(face_encodings[index])
            ))

        # Commit changes since there is no errors so far
        kid_image.save()
        for face in faces:
            face.save()

        # Send response
        return JsonResponse({
            'status': 'OK'
        })
