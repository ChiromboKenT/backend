from google.cloud import translate_v2 as translate
import os

# Set the environment variable for the Google Cloud credentials

def translate_text(text, src_lang, dest_lang):
    translate_client = translate.Client()

    # Define language codes for Yoruba and Fon
    language_codes = {
        "Yoruba": "yo",
        "Fon": "fon",
        "English": "en",
        "French": "fr"
    }

    # Translate the text
    translation = translate_client.translate(
        text,
        source_language=language_codes.get(src_lang, src_lang),
        target_language=language_codes.get(dest_lang, dest_lang)
    )

    return translation['translatedText']
