from enum import Enum
from django.db import models

class KidImageState(Enum):
    """Kid image states"""
    LOST = 'lost'
    SEARCH = 'search'

def kid_image_update_path(instance, filename):
    """Return image upload path"""
    # file will be uploaded to MEDIA_ROOT/kids/<datetime>_<filename>
    return 'kids/{0}_{1}'.format(instance.date_time.strftime("%Y%m%dT%H%M%S"), filename)

class KidImage(models.Model):
    """Model for children images"""

    STATES = (
        (KidImageState.LOST.value, 'Lost'),
        (KidImageState.SEARCH.value, 'Search'),
    )

    image = models.ImageField(upload_to = kid_image_update_path)
    date_time = models.DateTimeField('date the image was uploaded in')
    state = models.CharField(max_length = 10, choices=STATES, default=STATES[0][0])
    latitude = models.FloatField(default=None, null=True)
    longitude = models.FloatField(default=None, null=True)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(KidImage, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
