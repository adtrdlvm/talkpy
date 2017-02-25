# Copyright 2017 Jesus Perez
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from bottle import get, post, template, request
import speech_recognition as sr
from os import path
import webbrowser

@get('/')
def get_main():
    return template('index')

@post('/audio')
def post_audio():
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
    f = open(AUDIO_FILE, 'wb')
    bytes = request.body.file.raw.read()
    f.write(bytes)
    f.close()
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        if "music" in text:
            webbrowser.open(path.join(path.dirname(path.realpath(__file__)),"Kalimba.mp3"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    return