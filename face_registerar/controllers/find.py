import json
import numpy
import face_recognition
from django.views import View
from helpers.model_to_serializable import models_to_serializable
from ..models.kid_face import KidFace
from ..models.kid_image import KidImage, KidImageState
from ..utils.serialize_encodings import deserialize_encoding
from ..responses import error, success

class FindView(View):
    """View for fetching lost kids data"""
    def post(self, request):
        """Select subset of detected faces"""
        data: dict = json.loads(request.body.decode('utf-8'))

        # get searched image and faces
        try:
            search_image: KidImage = KidImage.objects.get(pk = data['imageId'])
            search_faces: list[KidFace] = search_image.kidface_set.filter(is_confirmed = True).all()
        except KidImage.DoesNotExist:
            return error('no_image_by_id')

        search_faces_encodings: list[numpy.ndarray] = []
        for search_face in search_faces:
            search_faces_encodings.append(deserialize_encoding(search_face.encoding))

        # get lost images
        try:
            lost_images = KidImage.objects.filter(state = KidImageState.LOST.value)
        except KidImage.DoesNotExist:
            lost_images = []

        images: list[KidFace] = []

        for lost_image in lost_images:
            lost_faces: list[KidFace] = lost_image.kidface_set.filter(is_confirmed = True).all()
            for lost_face in lost_faces:
                results: list[bool] = face_recognition.compare_faces(
                    search_faces_encodings,
                    deserialize_encoding(lost_face.encoding)
                )
                if True in results:
                    images.append(lost_image)
                    break

        print(models_to_serializable(images))

        return success(fields = { 'images': models_to_serializable(images) })
