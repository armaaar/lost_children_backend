from django.views import View
from ..models.kid_image import KidImage, KidImageState
from ..responses import success

class LostView(View):
    """View for fetching lost kids data"""
    def get(self, request):
        """Select subset of detected faces"""
        try:
            images = KidImage.objects.filter(state=KidImageState.LOST.value).order_by('-id').values()
        except KidImage.DoesNotExist:
            images = []
        return success(fields = { 'images': list(images) })
