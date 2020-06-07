import websocket
import json
import requests
import random


try:
    import thread
except ImportError:
    import _thread as thread
import time

longitude = 0.0
latitude = 0.0
_id = ""


def on_message(ws, message):
    time.sleep(1)
    print(message)

    file = open("data.txt", "r")
    data = file.read()
    data = data.split(",")
    file.close()
    print (data)

    user_id = data[3]
    found = False
    for i in range(10):
        x = requests.get("http://68.183.89.213/isalive/" + user_id)
        data_encoded = x._content
        print (x.__dict__)
        response = json.loads(data_encoded.decode())
        if response["found"] == True:
            if response["status"] == "alive":
                found = True
                print (data)
                times = int(data[4])
                print (times)
                if times < 100:
                    print ("im inside")
                    sendi = json.dumps({'_id': data[0], 
                        'latitude': float(data[1]),
                        'longitude': float(data[2]),
                        'temperature': 12,
                        'altitude': 234,
                        'obstruction': 123})
                    print (sendi)
                    longitude = float(data[2]) + 0.00005
                    latitude = float(data[1]) + 0.00005
                    
                    file = open("data.txt", "w")
                    file.write(data[0])
                    file.write(",")
                    file.write(str(latitude))
                    file.write(",")
                    file.write(str(longitude))
                    file.write(",")
                    file.write(user_id)
                    file.write(",")
                    file.write(str(times+1))
                    print("times", times)
                    file.close()
                    print ("reached here")
                    ws.send(sendi)
                    break
                else:
                    print ("break point 1")
                    ws.close()
            else:
                print ("trying again " + str(i+1))
        else:
            print ("trying again " + str(i+1))
    print ("break point 2")
    if found == False:
        ws.close()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        time.sleep(10)
        print("thread terminating...")
    thread.start_new_thread(run, ())


def run_this():
    run = True
    while run:
        x = requests.get("http://68.183.89.213/latest")
        data_encoded = x._content
        data = json.loads(data_encoded.decode())
        if data["latitude"] != None and data["longitude"] != None:
            run = False

    latitude = data["latitude"]
    longitude = data["longitude"]
    user_id =  data["id"]
    x = requests.get("http://68.183.89.213/id")
    data_encoded = x._content
    _id = json.loads(data_encoded.decode())["_id"]
    
    print (latitude)
    print (longitude)
    print (_id)

    latitude  = float(latitude) + 0.00005
    longitude = float(longitude) + 0.00005 

    file = open("data.txt", "w")
    file.write(_id)
    file.write(",")
    file.write(str(latitude))
    file.write(",")
    file.write(str(longitude))
    file.write(",")
    file.write(user_id)
    file.write(",")
    file.write(str(1))
    file.close()

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://68.183.89.213/ws/data/" + _id + "/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

while True:
    run_this()

