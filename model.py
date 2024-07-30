import google.generativeai as genai
from config import GEMENI_API_KEY

genai.configure(api_key=GEMENI_API_KEY)

chat_history = []

def generate_response(prompt):
    global chat_history
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat(history=chat_history)

        ##response = model.generate_content(prompt)
        response = chat.send_message(prompt)
        if response and hasattr(response, 'text'):
            chat_history.append({'role': 'user', 'parts': [{'text': prompt}]})
            chat_history.append({'role': 'model', 'parts': [{'text': response.text}]})
            return response.text
        else:
            return None
    except Exception as e:
        return str(e)