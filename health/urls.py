from django.urls import path
from .controllers.status import StatusView

urlpatterns = [
    path('', StatusView.as_view(), name='status'),
]
