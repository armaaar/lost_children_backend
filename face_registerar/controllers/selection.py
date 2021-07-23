import json
from django.views import View
from django.http import JsonResponse
from ..models.kid_image import KidImage
from ..models.kid_face import KidFace
from ..errors import err

class SelectionView(View):
    """View for selecting faces from uploaded images"""
    def patch(self, request):
        """Select subset of detected faces"""
        data: dict = json.loads(request.body.decode('utf-8'))

        # fetch image
        try:
            kid_image: KidImage = KidImage.objects.get(pk=data['imageId'])
        except KidImage.DoesNotExist:
            return err('no_image_by_id')

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
        state: str = 'confirmed'
        if kid_image.kidface_set.count() == 0:
            kid_image.delete()
            state = 'deleted'

        # Send response
        return JsonResponse({
            'state': state,
        })
