from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

class Button:
    def __init__(self, label, time):
        self.label = label
        self.time = time

@app.route('/')
def choose_audio():
    return render_template('choose_audio.html')

#### The right audio is not played when the buttons are clicked ####

@app.route('/choose_audio', methods=['POST'])
def index():

    value = request.form['value']

    if value == '1':
        audio_file = "admiral_mcraven_speech.mp3"
    elif value == '2':
        audio_file = 'eric_sprott.mp3'
    elif value == '3':
        audio_file = "david_lin_interview_doomberg.mp3"
    else:
        audio_file = 'forward_guidance_micheal_pettis.mp3'


    buttons_list = [
        Button('Skip to 0:00', 0), 
        Button('Skip to 1:00', 60), 
        Button('Skip to 2:00', 120),
        Button('Skip to 3:00', 180),
        Button('Skip to 4:00', 240)
    ]

    buttons = buttons_list
    return render_template('index.html', audio_file=audio_file, buttons=buttons)


@app.route('/audio/speed/<speed>')
def audio_speed(speed):
    audio_speeds = {'1.5': 1.5, '2.0': 2.0}
    audio_speed = audio_speeds.get(speed, 1.0)
    return json.dumps({'status': 'success', 'audio_speed': audio_speed})

@app.route('/audio/forward/')
def audio_forward():
    return json.dumps({'status': 'success', 'forward_time': 10})

@app.route('/audio/backward/')
def audio_backward():
    return json.dumps({'status': 'success', 'backward_time': 10})









if __name__ == '__main__':
    app.run()



