from django.db import models

def kid_image_update_path(instance, filename):
    """Return image upload path"""
    # file will be uploaded to MEDIA_ROOT/kids/<datetime>_<filename>
    return 'kids/{0}_{1}'.format(instance.date_time.strftime("%Y%m%dT%H%M%S"), filename)

class KidImage(models.Model):
    """Model for children images"""
    image = models.ImageField(upload_to = kid_image_update_path)
    date_time = models.DateTimeField('date the image was uploaded in')