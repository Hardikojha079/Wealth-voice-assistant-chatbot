import pyttsx3
import os
import uuid

engine = pyttsx3.init()

engine.setProperty('rate', 160)   
engine.setProperty('volume', 1.0)   

def text_to_speech(text: str, output_folder="audio_responses") -> str:
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_name = f"{uuid.uuid4().hex}.wav"
        file_path = os.path.join(output_folder, file_name)

        engine.save_to_file(text, file_path)
        engine.runAndWait()
        return file_path
    except Exception as e:
        return f"[Error generating TTS: {str(e)}]"
