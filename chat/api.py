#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "host": "localhost",
    "user": "mqttuser",
    "password": "xxxx",
    "database": "mqttchat"
}

@app.route("/api/messages", methods=["GET"])
def get_messages():
    limit = request.args.get("limit", 10, type=int)

    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT id, nickname, message, timestamp
        FROM messages
        ORDER BY id DESC
        LIMIT %s
    """, (limit,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Palautetaan vanhimmat ensin
    rows.reverse()

    # Muutetaan kenttien nimet fronttia varten
    msgs = [
        {
            "nickname": r["nickname"],
            "text": r["message"],
            "timestamp": r["timestamp"]
        }
        for r in rows
    ]

    return jsonify(msgs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
