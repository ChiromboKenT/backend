import whisper

def transcribe_audio(audio_file_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Load and transcribe the audio file using Whisper's built-in function
    result = model.transcribe(audio_file_path)
    return result['text']
