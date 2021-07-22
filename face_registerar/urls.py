from django.urls import path

from .controllers.detections import DetectionView

urlpatterns = [
    path('detect/', DetectionView.as_view(), name='detect'),
]
