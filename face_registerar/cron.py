from django_cron import CronJobBase, Schedule
from .models.kid_image import KidImage, KidImageState
from .models.kid_face import KidFace

class CleanUndetectedFacesCronJob(CronJobBase):
    """Cron job to crean all undetected faces and image periodically from system"""
    RUN_EVERY_MINS = 60 # every 1 hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'face_registerar.clean_undetected_faces_cron_job' # a unique code

    # pylint: disable=no-self-use,invalid-name
    def do(self):
        """Cron job Method"""
        # get unconfirmed faces
        try:
            unconfirmed_faces: list[KidFace] = KidFace.objects.filter(is_confirmed=False)
        except KidFace.DoesNotExist:
            unconfirmed_faces = []

        # Delete unconfirmed faces
        for unconfirmed_face in unconfirmed_faces:
            # get necessary data first
            face_image: KidImage = unconfirmed_face.image
            # delete unconfirmed face
            unconfirmed_face.delete()
            # delete image if it has no confirmed faces
            if face_image.kidface_set.count() == 0:
                face_image.delete()

        # get searched images
        try:
            searched_images: list[KidImage] = KidImage.objects.filter(
                state=KidImageState.SEARCH.value
            )
        except KidFace.DoesNotExist:
            searched_images = []

        # Delete searched images
        for searched_image in searched_images:
            # delete image
            searched_image.delete()
