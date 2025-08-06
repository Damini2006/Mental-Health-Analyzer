
import google.generativeai as genai

genai.configure(api_key="AIzaSyDwenD_N4-FX6DA-eDufGsTBT-4XT3ujdE")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def generate_response(message):
    try:
        response = model.generate_content(message)
        return response.text
    except:
        return "I'm here for you. Tell me more."
