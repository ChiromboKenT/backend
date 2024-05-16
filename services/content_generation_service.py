from utils.vertex_ai_utils import generate_content
from utils.prompt_engineering import generate_poster_prompt

def generate_poster_and_social_media(translated_text):
    prompt = generate_poster_prompt(translated_text)
    summary = generate_content(prompt)
    return summary
