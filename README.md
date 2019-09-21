# ProgramArena


## Description

A game focusing on learning about distributed systems, REST communication and
programming.

## Building and Running

### Build

```bash
docker build -t programarena:latest .
```

### Running

#### Using Docker

```bash
docker run -d --name programarena -p 80:80 programarena
```

ProgramArena will be running at [localhost](localhost)

#### Using uvicorn

```bash
uvicorn programarena.serve:app --reload
```

ProgramArena will be running at [localhost:8000](localhost:8000)

## API documentation

The documentation for every endpoints is created through swagger and can be
found by navigating to `/docs`. Through swagger it is also possible to try out
all the endpoints.


## Game logic

Every team creates a `player` and by using the API of the server, creates a
program which uses the different endpoints for moves.
