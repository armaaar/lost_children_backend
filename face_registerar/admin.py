from django.contrib import admin

from .models.kid_image import KidImage
from .models.kid_face import KidFace

admin.site.register(KidImage)
admin.site.register(KidFace)
