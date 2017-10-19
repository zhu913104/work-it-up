# coding: utf-8
import sys, os, time


import paho.mqtt.client as mqtt

# If broker asks client ID.
client_id = "8787"

client = mqtt.Client(client_id=client_id)

# If broker asks user/password.
user = ""
password = ""
client.username_pw_set(user, password)

client.connect("localhost")

topic = "hello"
payload = "hello mqtt"

for i in range(10):
    client.publish(topic, "%s - %d" % (payload, i))
    time.sleep(0.01)
    # 當 qos = 0, 若訊息間隔太短，就可能會漏發訊息。這是正常現象。