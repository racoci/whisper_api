import os
import requests
import subprocess
import time

# Start the Django server in a separate process
server_process = subprocess.Popen(['python', 'whisper_api/manage.py', 'runserver'])

# Wait for the server to start
time.sleep(5)

# Set the API endpoint URL
url = 'http://localhost:8000/api/audio_to_text/'

# Set the path to your sample WAV file
audio_file_path = 'sample.wav'

# Prepare the file for upload
files = {'audio_file': open(audio_file_path, 'rb')}

try:
    # Send a POST request to the API endpoint with the audio file
    response = requests.post(url, files=files)

    # Check the response status code
    if response.status_code == 200:
        # Print the transcription result
        result = response.json()
        print('Transcription:', result['text'])
        print('Confidence:', result)
    else:
        print('Error:', response.status_code)
finally:
    # Terminate the Django server process
    server_process.terminate()