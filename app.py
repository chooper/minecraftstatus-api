#!/usr/bin/env python

import os,socket
from flask import Flask,jsonify,abort
from mcstatus import MinecraftServer

app = Flask(__name__)

def query_server(server):
    """Query the minecraft server"""
    server = MinecraftServer.lookup(server)
    try:
        response = server.query()
    except socket.timeout:
      return None
    else:
      return response


@app.route("/<server>", methods=['GET'])
def server_main(server):
    """Get full response of minecraft query"""
    response = query_server(server)
    if not response: abort(503)
    return jsonify(raw=response.raw,players=response.players.names)


@app.route("/<server>/players", methods=['GET'])
def players(server):
    """Query online players from server"""
    response = query_server(server)
    if not response: abort(503)
    return jsonify(players=list(response.players.names))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))

    if os.environ.get('DEBUG', '0') == '1':
        app.debug = True

    timeout_secs = float(os.environ.get('TIMEOUT', '3'))
    socket.setdefaulttimeout(timeout_secs)

    app.run(host='0.0.0.0', port=port)

