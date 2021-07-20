from django.db import models
from .kid_image import KidImage

class KidFace(models.Model):
    """Model for detected faces"""

    image = models.ForeignKey(KidImage, on_delete=models.CASCADE)
    location = models.TextField('face location array')
    encoding = models.TextField('face encoding array')
    is_confirmed = models.BooleanField(default=False)
