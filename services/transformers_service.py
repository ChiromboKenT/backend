from transformers import pipeline
import langid

# Function to transcribe general audio using a general model (Whisper, Wav2Vec2, etc.)
def transcribe_general(audio_file_path):
    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    transcription = pipe(audio_file_path)
    return transcription['text']

# Function to transcribe Fon audio
def transcribe_fon(audio_file_path):
    pipe = pipeline("automatic-speech-recognition", model="chrisjay/fonxlsr")
    transcription = pipe(audio_file_path)
    return transcription['text']

# Function to transcribe Yoruba audio
def transcribe_yoruba(audio_file_path):
    pipe = pipeline("automatic-speech-recognition", model="neoform-ai/whisper-medium-yoruba")
    transcription = pipe(audio_file_path)
    return transcription['text']

# Function to detect language from text
def detect_language(text):
    lang, _ = langid.classify(text)

    return lang

# Function to handle transcription with language detection
def transcribe_with_language_detection(audio_file_path):
    # First, transcribe the audio using the general model to detect the language
    general_transcription = transcribe_general(audio_file_path)

    # Detect the language of the transcribed text
    detected_language = detect_language(general_transcription)
    print(f"Detected language: {detected_language}")
    # Based on the detected language, use the specific model for transcription
    if detected_language == 'fon':
        return transcribe_fon(audio_file_path)
    elif detected_language == 'yo':
        return transcribe_yoruba(audio_file_path)
    else:
        # If the language is not recognized, return the general transcription
        return general_transcription
