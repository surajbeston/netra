import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import GPS, Fleet, Obstruction
import math
import time
import datetime


class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']
        self.id_name = 'relay_%s' % self.id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.id_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({"accepted": self.id}))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.id_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        print (text_data_json)

        _id = text_data_json["_id"]
        latitude = text_data_json["latitude"]
        longitude = text_data_json["longitude"]
        altitude = text_data_json["altitude"]
        temperature = text_data_json["temperature"]
        obstruction = text_data_json["obstruction"] 
 
        # Send message to room group
        time.sleep(1)
        async_to_sync(self.channel_layer.group_send)(
            self.id_name,{'type': 'messenger', "_id": _id,"latitude": latitude, "longitude": longitude, "temperature": temperature, "altitude": altitude, "obstruction": obstruction}
        )

    # Receive message from room group
    def messenger(self, event):
 
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))


class ConnectionConsumer(WebsocketConsumer):
    def connect(self):
        _id = self.scope['url_route']['kwargs']['connection']
        all = GPS.objects.all()
        delta = datetime.timedelta(minutes=30)
        for gps in all:
            if (datetime.datetime.now() - gps.datetime) > delta:
                print (gps._id)
                gps.delete()
        if len(all) > 5:
            all[:2].delete()
        gps = GPS(_id = _id)
        print (_id)    
        gps.save()
        self.accept()
        
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        gps = GPS.objects.get(_id = data["_id"])
        gps.latitude = float(data["latitude"])
        gps.longitude = float(data["longitude"])
        gps.temperature = float(data["temperature"])
        gps.altitude = float(data["altitude"])
        gps.obstruction = float(data["obstruction"])
        gps.save()

        lat1 = float(data["latitude"])
        lon1 = float(data["longitude"]) 

        dist_arr = []
        _id_arr = []
        all_gps = GPS.objects.all()
        for gps in all_gps:
            try:
                lat2 = float(gps.latitude)
                lon2 = float(gps.longitude)
                _rand, d = 6,371.0*1000*math.acos((math.sin(lat1)*math.sin(lat2)) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2 - lon1))
                dist_arr.append(d)
                _id_arr.append(gps._id)
            except:
                continue
        
        id_arr = [x for _, x in sorted(zip(dist_arr, _id_arr))]
        dist_arr.sort()
        self.send(text_data=json.dumps({
            "user_arr" : id_arr[:5],
            "user_dist": dist_arr[:5]
        }))
        
class FleetConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']
        self.fleet_id = self.scope['url_route']['kwargs']['fleet_id']
        self.id_name = 'relay_%s' % self.fleet_id

        print(self.fleet_id)
        print(self.id)

        fleet = Fleet.objects.get(fleet_id = self.fleet_id)
        id_arr = fleet.ids.split(",")
        if self.id in id_arr:
            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.id_name,
                self.channel_name
            )

            self.accept()

            self.send(text_data=json.dumps({"_id": self.id, "fleet_id": self.fleet_id }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.id_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        print (text_data_json)

        fleet_id = text_data_json["fleet_id"]
        _id = text_data_json["_id"]
        latitude = text_data_json["latitude"]
        longitude = text_data_json["longitude"]
        altitude = text_data_json["altitude"]
        temperature = text_data_json["temperature"] 
        obstruction = text_data_json["obstruction"]

        time.sleep(1)
        async_to_sync(self.channel_layer.group_send)(
            self.id_name,{'type': 'messenger', "fleet_id": fleet_id, "_id": _id,"latitude": latitude, "longitude": longitude, "temperature": temperature, "altitude": altitude, obstruction: "obstruction"}
        )

    # Receive message from room group
    def messenger(self, event):
 
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
