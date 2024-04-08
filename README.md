# Audio-to-Text Transcription API

This project implements a simple API for audio-to-text transcription using the OpenAI Whisper model. It allows users to send a WAV audio file and receive the transcribed text along with confidence scores.

## Features

- Accepts WAV audio files via a POST request to the `/api/audio_to_text/` endpoint
- Transcribes the audio using the OpenAI Whisper model
- Supports transcription in Portuguese language
- Returns the transcribed text and confidence scores as a JSON response

## Prerequisites

- Python 3.x
- Django
- Django REST Framework
- OpenAI Whisper

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/racoci/whisper_api.git
   ```

2. Navigate to the project directory:
   ```
   cd whisper_api
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

## Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Send a POST request to the `/api/audio_to_text/` endpoint with a WAV audio file attached as a multipart/form-data file.

3. The API will respond with a JSON object containing the transcribed text and confidence scores.

## Testing

To test the API, you can use the provided `test_api.py` script. Make sure you have a sample WAV file named `sample.wav` in the same directory as the script.

Run the test script:
```
python test_api.py
```

The script will start the Django server, send a POST request to the API endpoint with the sample WAV file, and print the transcription result and confidence score.

## Configuration

- The OpenAI Whisper model is loaded during server initialization to avoid loading it on every request. You can modify the model configuration in the `views.py` file.

- The transcription language is set to Portuguese ("pt") by default. You can change the language by modifying the `language` parameter in the `transcribe` function call in the `views.py` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).