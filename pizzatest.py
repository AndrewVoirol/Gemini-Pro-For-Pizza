import google.generativeai as genai
from pathlib import Path

genai.configure(api_key="")

# Ensure that the model ID is correct and that you have access to it
model = genai.GenerativeModel('gemini-pro-vision')

# Read the image as binary data
image_path = Path('image.png')
image_data = image_path.read_bytes()

# The API may require the image data to be base64 encoded or in a specific JSON structure
# This will depend on the API's expected request format
prompt = "Give me a recipe for this:"
contents = {
    'parts': [
        {'mime_type': 'image/png', 'data': image_data},
        {'text': prompt}
    ]
}

# Send the prompt and image data to the model
response = model.generate_content(contents=contents)

# Print the result
print(response.text)
