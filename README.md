# OpenAI Text Generator API

This project provides a Flask-based API for generating text using OpenAI's GPT models. It allows users to submit descriptions and optionally specify the type of text they want to generate.

## Features

- Generate text based on user-provided descriptions
- Option to specify the type of text to generate ("formal","informal")
- RESTful API endpoint for easy integration
- Logging for debugging and monitoring

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An OpenAI API key

## Installation

1. Clone this repository:
  

2. Install the required packages:
   ```
   pip install flask openai
   ```

3. Set up your OpenAI API key:
   - Open the `app.py` file
   - Replace `'your-api-key-here'` with your actual OpenAI API key
   
   Note: For security reasons, it's recommended to use environment variables for API keys in production environments.

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000/generate`

3. Send a POST request to the `/generate` endpoint with a JSON payload:
   ```json
   {
     "description": "letter to the principal",
     "choice": "formal"
   }
   ```
   The `choice` field is optional. If not provided, the API will generate general text based on the description.

4. The API will respond with generated text:
   ```json
   {
     "generated_text": "Generated text content here..."
   }
   ```

## API Reference

### Generate Text

**Endpoint:** `POST /generate`

**Request Body:**
- `description` (string, required): The input description for text generation
- `choice` (string, optional): The type of text to generate ()

**Response:**
- `generated_text` (string): The generated text based on the input

**Error Response:**
- If the description is missing, the API will return a 400 error with an error message.

## Logging

The application uses Python's built-in logging module. Logs are printed to the console and include timestamps, log levels, and messages for debugging and monitoring purposes.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the OpenAI API for text generation.
- Flask is used for creating the API server.

## Disclaimer

This is a sample project and should not be used in production without proper security measures, especially regarding the handling of API keys and potential misuse of the text generation capabilities.
