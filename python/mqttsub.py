# coding: utf-8
import sys, os, time, signal
import paho.mqtt.client as mqtt

client = None
mqtt_looping = False
TOPIC_ROOT = "test"

def status_reading():
    while True:
        #status = gate.read()
        time.sleep(1)   # 假設讀取狀態
        status = "noop"

        if mqtt_looping:
            client.publish(TOPIC_ROOT + '/status', status, qos=1)
        else:
            print ("quit status reading thread")
            return



def on_connect(mq, userdata, rc, _):
    # subscribe when connected.
    mq.subscribe(TOPIC_ROOT + '/#')

def on_message(mq, userdata, msg):
    print ("topic: %s" % msg.topic)
    print ("payload: %s" % msg.payload)
    print ("qos: %d" % msg.qos)

    chn = msg.topic.rpartition('/')[-1]
    if chn == 'command':
        print ("receive %s" % msg.payload)

        # client.publish(TOPIC_ROOT + '/response', "computing", qos=0)
        # time.sleep(0.5)
        client.publish(TOPIC_ROOT + '/response', "hello world", qos=0)


def mqtt_client_thread():
    global client, mqtt_looping
    client_id = "KMDRIOD" # If broker asks client ID.
    client = mqtt.Client(client_id=client_id)

    # If broker asks user/password.
    user = ""
    password = ""
    client.username_pw_set(user, password)

    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("localhost")
    except:
        print ("MQTT Broker is not online. Connect later.")

    mqtt_looping = True
    print ("Looping...")

    #mqtt_loop.loop_forever()
    cnt = 0
    while mqtt_looping:
        client.loop()

        cnt += 1
        if cnt > 20:
            try:
                client.reconnect() # to avoid 'Broken pipe' error.
            except:
                time.sleep(1)
            cnt = 0

    print ("quit mqtt thread")
    client.disconnect()

def stop_all(*args):
    global mqtt_looping
    mqtt_looping = False

if __name__ == '__main__':
    mqtt_client_thread()
    reading_thread.join()
    print ("exit program")
    sys.exit(0)