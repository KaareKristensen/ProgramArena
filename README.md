# ProgramArena


## Description

A game focusing on learning about distributed systems, REST communication and
programming.

## Building and Running

### Build

Either using Docker

```bash
docker build -t programarena:latest .
```

or using docker-compose

```bash
docker-compose build
```

### Running

#### Using Docker

Either using Docker

```bash
docker run -d --name programarena -p 80:80 programarena
```

or using docker-compose

```bash
docker-compose up
```

ProgramArena will be running at `localhost`

#### Using uvicorn

When developing running uvicorn will hotload new changes directly to the server.

```bash
uvicorn programarena.serve:app --reload
```

ProgramArena will be running at `localhost:8000` if using the standard port
provided from uvicorn.

## API documentation

The documentation for every endpoints is created through OpenAPI and can be
found by navigating to `/redoc` endpoint. Through OpenAPI it is also possible to try out
all the endpoints.


## Game logic

Every team creates a `player` and by using the API of the server, creates a
program which uses the different endpoints for moves.
