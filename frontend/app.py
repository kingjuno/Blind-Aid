from flask import Flask, render_template, request
import requests
import shlex
import os
from gtts import gTTS
from processor import converter
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def audio():
    if request.method == 'POST':
        st=request.form['nm']
        im = Image.open(BytesIO(base64.b64decode(st[23:])))
        im.save('frontend/static/image.png', 'PNG')
        items=converter()
        print(items)
        if(len(items)>=2):
            items.insert(len(items)-1,'and')
        if items:
            tts = gTTS('detected objects are :'+ ','.join(items),slow=True)
        else:
            tts = gTTS('Nothing is detected')
            
        tts.save(f'frontend/static/object.mp3')
        return render_template('index.html')
    items=converter()
    print(items)
    if(len(items)>=2):
        items.insert(len(items)-1,'and')
    if items:
        tts = gTTS('detected objects are :'+ ','.join(items),slow=True)
    else:
        tts = gTTS('Nothing is detected')
        
    tts.save(f'frontend/static/object.mp3')
    while 1:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True,port=3050)