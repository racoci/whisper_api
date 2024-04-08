from django.urls import path
from .views import AudioToTextView

urlpatterns = [
    path('audio_to_text/', AudioToTextView.as_view(), name='audio_to_text'),
]
