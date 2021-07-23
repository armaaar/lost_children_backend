from django.urls import path
from .controllers.detections import DetectionView
from .controllers.selection import SelectionView


urlpatterns = [
    path('detect/', DetectionView.as_view(), name='detect'),
    path('select/', SelectionView.as_view(), name='select'),
]
