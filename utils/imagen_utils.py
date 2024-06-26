import openai

def generate_random_image(prompt):
    openai.api_key = 'your-openai-api-key'
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']
