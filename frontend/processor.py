import json
import os

def converter():
    cmd = '''curl.exe -X POST -F images=@./frontend/static/dog.png "http://localhost:5000/detections"'''
    stream = os.popen(cmd)
    try:
        data = json.loads(stream.read())
        print(type(data))
        # data = json.loads(stream.read())
    except:
        return []
    print(data,'hola')
    l=[]
    detections=data['response'][0]
    for i in detections['detections']:
        if i['confidence'] > 90:
            l.append(i['class'])
    return list(set(l))