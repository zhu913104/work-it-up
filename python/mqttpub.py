import paho.mqtt.publish as publish

# publish a message then disconnect.
host = "localhost"
topic = "tw/rocksaying/command"
payload = "open"

# If broker asks user/password.


# If broker asks client ID.


publish.single(topic, payload, qos=1, hostname=host)

#publish.single(topic, payload, qos=1, host=host,
#    auth=auth, client_id=client_id)