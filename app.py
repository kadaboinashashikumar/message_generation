import openai
import os
import logging
from flask import Flask, request, jsonify

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate(description, choice):
    try:
        prompt = description
        logger.info(f"Generating text with description: {description} and choice: {choice}")
        response = openai.chat.completions.create(
            model='gpt-4-mini-2024-07-18',
            messages=[
                {'role': 'system', 'content': f"You will be provided with statements, and generate a {choice} writing of 3 different versions with no grammatical errors."},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=4000,
            temperature=0.5
        )
        generated_content = response.choices[0].message.content.strip()
        logger.info("Text generation successful")
        return generated_content
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        return "An error occurred while generating text."

def generate_text(description):
    try:
        prompt = description
        logger.info(f"Generating text with description: {description}")
        response = openai.chat.completions.create(
            model='gpt-4-mini-2024-07-18',
            messages=[
                {'role': 'system', 'content': f"You will be provided with statements, and generate a writing of 3 different versions with no grammatical errors."},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=4000,
            temperature=0.5
        )
        generated_content = response.choices[0].message.content.strip()
        logger.info("Text generation successful")
        return generated_content
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        return "An error occurred while generating text."

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def api_generate():
    data = request.json
    description = data.get('description', '')
    choice = data.get('choice', '')
    
    if description and choice:
        logger.debug(f"Received POST request with description: {description} and choice: {choice}")
        generated_text = generate(description, choice)
    elif description:
        logger.debug(f"Received POST request with description: {description}")
        generated_text = generate_text(description)
    else:
        logger.warning("Description is missing in POST request.")
        return jsonify({"error": "Description is required"}), 400
    
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run()