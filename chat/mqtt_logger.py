import json
import paho.mqtt.client as mqtt
import mysql.connector
import time

DB = {
    "host": "localhost",
    "user": "mqttuser",
    "password": "xxxx",
    "database": "mqttchat"
}

def save_message(nickname, message, timestamp):
    conn = mysql.connector.connect(**DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (nickname, message, timestamp) VALUES (%s, %s, %s)",
        (nickname, message, timestamp)
    )
    conn.commit()
    cur.close()
    conn.close()

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        save_message(data["nickname"], data["text"], data["timestamp"])
        print("Saved:", data)
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("chat/messages")
client.on_message = on_message

print("MQTT logger started...")
client.loop_forever()
