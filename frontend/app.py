from flask import Flask, render_template, request
import requests
import shlex
import os
from gtts import gTTS
from processor import converter
app = Flask(__name__)


@app.route('/')
def audio():
    items=converter()
    if(len(items)>=2):
        items.insert(len(items)-1,'and')
    print(items)
    if items:
        tts = gTTS('detected objects are :'+ ','.join(items),slow=True)
    else:
        tts = gTTS('Nothing is detected')
        
    tts.save(f'frontend/static/object.mp3')
    while 1:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True,port=3000)