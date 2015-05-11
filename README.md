# minecraftstatus-api

A silly flask API wrapper for
[mcstatus](https://github.com/Dinnerbone/mcstatus). If a Minecraft server has
enabled server querying, then this API can be used to get the list of players
online plus some other basic information.

## Usage/Example

### Docker Compose

This project uses Docker and Docker Compose if you choose to use it. You can
run the project like so:

```bash
$ docker-compose build
$ docker-compose run app python tests.py
...
$ docker-compose up
Recreating minecraftstatusapi_app_1...
Attaching to minecraftstatusapi_app_1
app_1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
app_1 |  * Restarting with stat
```

### Without Docker Compose

Without docker-compose, you should use virtualenv and start this project like so:

```bash
$ mkvirtualenv mcstatus
$ pip install -r requirements.txt
$ python tests.py
$ python app.py
app_1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
app_1 |  * Restarting with stat
```

### Querying the API

And to query the server:

```bash
$ curl http://api/minecraft.server.net
{
  "players": [
    "Solouroboros"
  ],
  "raw": {
    "game_id": "MINECRAFT",
    "gametype": "SMP",
    "hostip": "127.0.0.1",
    "hostname": "A Minecraft Server",
    "hostport": "25565",
    "map": "world",
    "maxplayers": "20",
    "numplayers": "1",
    "plugins": "",
    "version": "1.7.10"
  }
}
$ curl http://api.minecraft.server.net/players
{
  "players": [
    "Solouroboros",
    "japherwocky"
  ]
}
```

## API

Today, there are only two routes registered:

* `GET /<server>` - Used to return the full query payload. A response looks like this:

    ```
    {
      "players": [
        "Solouroboros"
      ],
      "raw": {
        "game_id": "MINECRAFT",
        "gametype": "SMP",
        "hostip": "127.0.0.1",
        "hostname": "A Minecraft Server",
        "hostport": "25565",
        "map": "world",
        "maxplayers": "20",
        "numplayers": "1",
        "plugins": "",
        "version": "1.7.10"
      }
    }
    ```

* `GET /<server>/players` - Used to return only the list of online players. A response looks like this:

    ```
    {
      "players": [
        "Solouroboros",
        "japherwocky"
      ]
    }
    ```

