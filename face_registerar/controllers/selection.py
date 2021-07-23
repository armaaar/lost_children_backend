import json
from django.views import View
from ..models.kid_image import KidImage
from ..models.kid_face import KidFace
from ..responses import error, success

class SelectionView(View):
    """View for selecting faces from uploaded images"""
    def patch(self, request):
        """Select subset of detected faces"""
        data: dict = json.loads(request.body.decode('utf-8'))

        # fetch image
        try:
            kid_image: KidImage = KidImage.objects.get(pk=data['imageId'])
        except KidImage.DoesNotExist:
            return error('no_image_by_id')

        # fetch faces
        faces: list[KidFace] = kid_image.kidface_set.all()

        # delete unselected faces
        for face in faces:
            if face.id in data['faceIds']:
                face.is_confirmed = True
                face.save()
            else:
                face.delete()

        # confirm or delete image
        message: str = 'faces_confirmed'
        if kid_image.kidface_set.count() == 0:
            kid_image.delete()
            message = 'image_deleted'

        # Send response
        return success(message)
