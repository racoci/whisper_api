import requests
import subprocess
import time

# Start the Django server in a separate process
server_process = subprocess.Popen(['python', 'whisper_api/manage.py', 'runserver'])

# Wait for the server to start
time.sleep(10)

# Set the API endpoint URLs
model_url = 'http://localhost:8000/api/model/'
audio_to_text_url = 'http://localhost:8000/api/audio_to_text/'

# Set the path to your sample WAV file
audio_file_path = 'sample.wav'

try:
    # Set up the model
    model_data = {'model': 'medium'}
    model_response = requests.post(model_url, json=model_data)

    if model_response.status_code == 200:
        print('Model set up successfully')
    else:
        print('Error setting up the model:', model_response.status_code)
        raise Exception('Model setup failed')

    # Prepare the file for upload
    files = {'audio_file': open(audio_file_path, 'rb')}

    # Send a POST request to the API endpoint with the audio file
    response = requests.post(audio_to_text_url, files=files)

    # Check the response status code
    if response.status_code == 200:
        # Print the transcription result
        result = response.json()
        print('Transcription:', result['text'])
        print('Confidence:', result)
    else:
        print('Error:', response.status_code)

except Exception as e:
    print('An error occurred:', str(e))

finally:
    # Terminate the Django server process
    server_process.terminate()