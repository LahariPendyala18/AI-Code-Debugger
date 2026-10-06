import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    raise ValueError("GEMINI_API_KEY is not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def debug_code(code, language):

    prompt = f"""
You are an AI Code Debugging Assistant.

Analyze the following {language} code:

{code}

Give the answer in simple language.

Include:
1. Error Found
2. Why the error occurred
3. Corrected Code
4. Changes Made
5. Suggestions
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text