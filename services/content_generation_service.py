import json
import re
import vertexai # type: ignore
from vertexai.preview.generative_models import GenerativeModel # type: ignore
import os

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = "us-central1"
MODEL_NAME = os.getenv("CONTENT_GENERATION_MODEL_NAME")
LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "yo": "Yoruba",
    "ha": "Hausa",
    "ig": "Igbo",
    "fon": "Fon",
    "sw": "Swahili",
    "ar": "Arabic",
    "he": "Hebrew",
    "hi": "Hindi",
}

vertexai.init(project=PROJECT_ID, location=REGION)

def generate_prompt(text, language):
    lang = LANGUAGES.get(language, language)

    prompt = f"""
    You are an AI that generates promotional content. Please create the content in the following structure:

    {{
        "poster": {{
            "title": "",
            "slogan": "",
            "callToAction": "",
            "venue": "",
            "date": "",
            "time": "",
            "contact": ""
        }},
        "socialMedia": {{
            "facebook": {{
                "title": "",
                "description": ""
            }},
            "twitter": {{
                "title": "",
                "description": ""
            }},
            "instagram": {{
                "title": "",
                "description": ""
            }}
        }}
    }}

    The content should be provided in {lang} where possible, otherwise keep it in the query language. The keys should remain as is, and if no information is given, leave it empty. Descriptions should always be generated according to the query as much as possible. With the values being generated in {lang}, the content should be engaging and informative.
    Here is the text to base the promotional content on:
    {text}

    Generate the content now.
    """

    return prompt

def load_and_fix_json(json_data):
    try:
        # Initial validation and parsing attempt
        data = json.loads(json_data)
        return data  # Return the valid data if successful
    except json.JSONDecodeError as e:
        # Error handling and repair attempts
        error_message = str(e)

        # Handle common errors:
        if "Expecting ',' delimiter" in error_message:
            json_data = json_data.replace("}{", "},{")  # Fix missing comma between objects
        elif "Expecting property name enclosed in double quotes" in error_message:
            # Attempt to fix missing quotes around keys (be cautious)
            json_data = json.dumps(eval(json_data))  # This can be risky if the input is untrusted

        # Re-validate after potential fixes
        try:
            data = json.loads(json_data)
            return data  # Return the repaired data if successful
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format and unable to repair: " + error_message)

def generate_content(text, language):
    prompt = generate_prompt(text, language)

    generative_model = GenerativeModel(model_name=MODEL_NAME)
    response = generative_model.generate_content([prompt])

    # Attempt to extract the generated text from the response
    try:
        generated_text = response.candidates[0].content.parts[0].text
        # Remove the code block markers if present
        if generated_text.startswith("```json") and generated_text.endswith("```"):
            generated_text = generated_text[6:-3].strip()
        # Strip any leading non-JSON characters (e.g., leading "n")
        generated_text = re.sub(r'^[^{]*', '', generated_text)
    except (AttributeError, IndexError) as e:
        print(f"Error extracting content: {e}")
        return {
            "error": "The generated content could not be extracted. Please try again."
        }

    # Fix and validate JSON format
    try:
        content = load_and_fix_json(generated_text)
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        content = {
            "error": "The generated content is not valid JSON. Please try again."
        }

    return content
