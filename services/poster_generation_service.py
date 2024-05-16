import os
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def render_poster(data):
    template = env.get_template('poster_template.html')
    html_content = template.render(
        title=data.get('title', ''),
        slogan=data.get('slogan', ''),
        venue=data.get('venue', ''),
        date=data.get('date', ''),
        time=data.get('time', ''),
        contact=data.get('contact', ''),
        call_to_action=data.get('call_to_action', ''),
        background_image=data.get('background_image', '')
    )
    return html_content