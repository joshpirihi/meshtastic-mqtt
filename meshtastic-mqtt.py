# python3.6

from portnums_pb2 import POSITION_APP
import random
import json

import mesh_pb2 as mesh_pb2
import mqtt_pb2 as mqtt_pb2

from paho.mqtt import client as mqtt_client


broker = '10.147.253.250'
port = 1883
topic = "msh/1/c/LongSlow/#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
#    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        se = mqtt_pb2.ServiceEnvelope()
        se.ParseFromString(msg.payload)
        
        #print(se)
        mp = se.packet
        if mp.decoded.portnum == POSITION_APP:
            pos = mesh_pb2.Position()
            pos.ParseFromString(mp.decoded.payload)
            print(getattr(mp, "from"))
            print(pos)
            owntracks_payload = {
                "_type": "location",
                "lat": pos.latitude_i * 1e-7,
                "lon": pos.longitude_i * 1e-7,
                "tst": pos.time,
                "batt": pos.battery_level
            }
            if owntracks_payload["lat"] != 0 and owntracks_payload["lon"] != 0:
                client.publish("owntracks/"+str(getattr(mp, "from"))+"/meshtastic_node", json.dumps(owntracks_payload))
        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
