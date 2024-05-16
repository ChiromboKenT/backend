import os
from flask import Flask, request,jsonify, send_file #type: ignore
from services.transformers_service import transcribe_with_language_detection
from services.translation_service import translate_text
from services.content_generation_service import generate_content
from services.image_generation_service import generate_benin_background_image
from services.poster_generation_service import render_poster




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

    @app.route('/generate-content', methods=['POST'])
    def generate_content_route():
        data = request.json
        text = data.get('text')
        language = data.get('language', 'en')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        generated_content = generate_content(text, language)
        return jsonify(generated_content)

    @app.route('/generate-background-image', methods=['POST'])
    def generate_background_image_route():
        data = request.json
        query = data.get('query', '')
        image_url = generate_benin_background_image(query)
        if image_url:
            return jsonify({"image_url": image_url})
        else:
            return jsonify({"error": "Error generating image"}), 500

    @app.route('/generate-poster', methods=['POST'])
    def generate_poster_route():
        data = request.json
        poster_data = data.get('poster', {})
        background_image = data.get('background_image')

        if not poster_data or not background_image:
            return jsonify({"error": "Poster data or background image URL is missing"}), 400

        # Add the background image to the poster data
        poster_data['background_image'] = background_image

        # Render the poster and get the HTML content
        poster_html = render_poster(poster_data)

        # Return the rendered HTML content
        return poster_html



# Other existing routes...


