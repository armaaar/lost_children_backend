import base64
import io
import uuid
import environ
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

env = environ.Env(
    # set casting, default value
    IMAGE_DIMENSION=(int, 800),
    IMAGE_QUALITY=(int, 75)
)
environ.Env.read_env(env.str('../', '.env'))

BASE_DIMENSION = env('IMAGE_DIMENSION')
BASE_QUALITY = env('IMAGE_QUALITY')

def base64_to_memory_image(base64_string: str):
    """Convert base64 image to an image"""

    # Decode Base64
    imgdata = base64.b64decode(base64_string)
    # Create an RGB image from Base64
    image = Image.open(io.BytesIO(imgdata)).convert('RGB')

    # Resize image to have maximum dimensions of 800px
    wpercent = BASE_DIMENSION / float(image.size[0])
    hsize = int(float(image.size[1]) * float(wpercent))
    image = image.resize((BASE_DIMENSION,hsize), Image.ANTIALIAS)

    # Save image in memory with the new quality
    image_io = io.BytesIO()
    image.save(image_io, format = 'JPEG', quality = BASE_QUALITY)
    return InMemoryUploadedFile(
        image_io,
        field_name=None,
        name=str(uuid.uuid4())+".jpg",
        content_type='image/jpeg',
        size=image_io.tell,
        charset=None
    )
