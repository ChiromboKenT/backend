import os
from flask import Flask, request,jsonify #type: ignore
from services.transformers_service import transcribe_with_language_detection
from services.translation_service import translate_text
from services.content_generation_service import generate_poster_and_social_media



def init_routes(app):
    @app.route('/translate', methods=['POST'])
    def translate():
        data = request.json
        text = data.get('text')
        src_lang = data.get('src_lang')
        dest_lang = data.get('dest_lang')
        translated_text = translate_text(text, src_lang, dest_lang)
        return jsonify({"translated_text": translated_text})

    @app.route('/transcribe', methods=['POST'])
    def transcribe():
        if 'audio_file' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files['audio_file']

        # Use a directory that is accessible on Windows
        temp_dir = "C:\\temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        audio_file_path = os.path.join(temp_dir, audio_file.filename)
        audio_file.save(audio_file_path)

        transcribed_text = transcribe_with_language_detection(audio_file_path)
        return jsonify({"transcribed_text": transcribed_text})

# Other existing routes...


