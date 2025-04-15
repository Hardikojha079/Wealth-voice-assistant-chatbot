from flask import Flask, request, jsonify, send_file
from model_handler import generate_response, classify_intent
from tts_handler import text_to_speech
import os
import speech_recognition as sr

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def chat():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files['file']
    audio_path = "input.wav"
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        user_input = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return jsonify({"error": "Speech not recognized"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Speech recognition error: {str(e)}"}), 500

    print(f"[User]: {user_input}")

    intent = classify_intent(user_input)
    print(f"[Intent]: {intent}")

    prompt = f"Intent: {intent}\nUser: {user_input}\nResponse:"

    # llm_response = generate_response(prompt)
    # print(f"[LLM]: {llm_response}")

    response_audio_path = text_to_speech(intent)
    # response_audio_path = text_to_speech(llm_response)


    if not os.path.isfile(response_audio_path):
        return jsonify({"error": "Failed to generate audio"}), 500

    return send_file(response_audio_path, mimetype='audio/wav', as_attachment=True)

@app.route('/', methods=['GET'])
def index():
    return "AI Voice Assistant Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
