from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AudioFileSerializer
import whisper


class AudioToTextView(APIView):
    def post(self, request, format=None):
        serializer = AudioFileSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.validated_data['audio_file']
            model = whisper.load_model("base")
            result = model.transcribe(audio_file)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
