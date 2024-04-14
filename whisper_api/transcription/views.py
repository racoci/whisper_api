import numpy as np
import soundfile as sf
import whisper
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from librosa import resample
from .serializers import AudioFileSerializer


def normalized(x):
    x_min = np.min(x)
    x_max = np.max(x)
    x_norm = x / (x_max - x_min)
    return x_norm


model = None


class ModelView(APIView):
    def post(self, request, format=None):
        global model
        model_name = request.data.get('model', 'base')
        try:
            model = whisper.load_model(model_name)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class AudioToTextView(APIView):
    def post(self, request, format=None):
        global model
        if model is None:
            return Response("Model not set up. Please set up the model using the /model route.",
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = AudioFileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        audio_file = serializer.validated_data['audio_file']
        audio_data, sample_rate = sf.read(audio_file)
        #model = whisper.load_model("tiny")
        audio_data = audio_data.astype(np.float32)
        audio_data = resample(audio_data, orig_sr=sample_rate, target_sr=whisper.audio.SAMPLE_RATE)

        result = model.transcribe(
            audio=normalized(audio_data),
            task="transcribe",
            language="pt"
        )

        return Response(result, status=status.HTTP_200_OK)
