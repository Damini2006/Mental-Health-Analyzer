
import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def generate_response(message):
    try:
        response = model.generate_content(message)
        return response.text
    except:
        return "I'm here for you. Tell me more."

