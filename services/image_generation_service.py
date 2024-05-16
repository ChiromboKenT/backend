from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure your OpenAI API key is set from the environment variable

def generate_background_image(prompt):
    try:
        response = client.images.generate(prompt=prompt,
        n=1,
        size="1024x1024")
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def generate_benin_background_image(query=None):
    prompt = (
        "A beautiful background image for a promotional poster, highlighting the rich cultural heritage of Benin. "
        "The image should be minimalistic, focusing on traditional Benin patterns, colors."
    )
    return generate_background_image(prompt + (f" The query for this image is: {query}" if query else ""))
