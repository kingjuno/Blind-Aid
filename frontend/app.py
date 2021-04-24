from flask import Flask, render_template, request
import requests
import shlex
import os

# import request
app = Flask(__name__)


@app.route('/audio')
def audio():
    return 'audio'

@app.route('/')
def index():
    cmd = '''curl.exe -X POST -F images=@./frontend/meme.jpg "http://localhost:5000/detections"'''
    stream = os.popen(cmd)
    output = stream.read()
    return output or 'hi'

if __name__ == "__main__":
    app.run(debug=True,port=3000)