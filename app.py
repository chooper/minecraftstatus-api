#!/usr/bin/env python

import os
from flask import Flask,jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

@app.route("/playersonline/<server>", methods=['GET'])
def playersonline(server):
    server = MinecraftServer.lookup(server)
    query = server.query()
    return jsonify(players=list(query.players.names))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)

