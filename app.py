#!/usr/bin/env python

import os,socket
from flask import Flask,jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

def query_server(server):
    """Query the minecraft server"""
    server = MinecraftServer.lookup(server)
    return server.query()


@app.route("/<server>", methods=['GET'])
def server_main(server):
    """Get full response of minecraft query"""
    query = query_server(server)
    return jsonify(raw=query.raw,players=query.players.names)


@app.route("/<server>/players", methods=['GET'])
def players(server):
    """Query online players from server"""
    query = query_server(server)
    return jsonify(players=list(query.players.names))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))

    if os.environ.get('DEBUG', '0') == '1':
        app.debug = True

    timeout_secs = float(os.environ.get('TIMEOUT', '3'))
    socket.setdefaulttimeout(timeout_secs)

    app.run(host='0.0.0.0', port=port)

