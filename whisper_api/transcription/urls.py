from django.urls import path
from .views import *

urlpatterns = [
    path('audio_to_text/', AudioToTextView.as_view(), name='audio_to_text'),
    path('model/', ModelView.as_view(), name='model'),
]
