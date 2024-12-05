from flask import Flask, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['GET'])
def record():
    recognizer = sr.Recognizer()
    try:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
            audio = recognizer.listen(source)  # Listen for speech

            # Convert speech to text using Google's speech recognition service
            text = recognizer.recognize_google(audio)
            return jsonify({'status': 'success', 'text': text})

    except sr.UnknownValueError:
        return jsonify({'status': 'error', 'message': 'Sorry, I could not understand the speech.'})
    except sr.RequestError:
        return jsonify({'status': 'error', 'message': 'Sorry, there was an issue with the speech service.'})

if __name__ == '__main__':
    app.run(debug=True)
