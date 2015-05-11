#!/usr/bin/env python

import os
from flask import Flask,jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

def query_server(server):
    """Query the minecraft server"""
    server = MinecraftServer.lookup(server)
    return server.query()


@app.route("/<server>/players", methods=['GET'])
def players(server):
    """Query online players from server"""
    query = query_server(server)
    return jsonify(players=list(query.players.names))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)

