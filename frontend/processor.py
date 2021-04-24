import json
import os

def converter():
    cmd = '''curl.exe -X POST -F images=@./frontend/static/image.png "http://localhost:5000/detections"'''
    stream = os.popen(cmd)
    try:
        data = json.loads(stream.read())
    except:
        return []
    l=[]
    detections=data['response'][0]
    for i in detections['detections']:
        if i['confidence']:
            l.append(i['class'])
    return list(set(l))