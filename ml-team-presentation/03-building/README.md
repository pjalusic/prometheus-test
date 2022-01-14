Building 'production' image

# Build

```
docker build -t test-build .
```

# Run

```
docker run --rm -it -p 8000:8000 -v database_volume:/app/database test-build 
```

# Run 'production'
Run in detached mode, container runs in background.
```
docker run -d -p 8000:8000 -v database_volume:/app/database --name test-production test-build
```

## Attach to running container

```
docker container attach test-production
```

### Fix keyboard interrupt
- Remove container:
    ```
    docker container rm -f test-production
    ```
- start again with:
    ```
    docker run -dt -p 8000:8000 -v database_volume:/app/database --name test-production test-build
    ```
    Note the added `-t` flag.

## View running containers
```
docker container ls -as
```
`-s` flag shows size on disk

## Start, stop, restart
```
docker container stop -t0 test-production
```
```
docker container start test-production
```
```
docker container restart -t0 test-production
```

## View process log
```
docker container logs test-production
```
### Nicer logs
```
docker container logs test-production -tf --since 20s
```

## Resource monitor basic
```
docker container stats test-production --no-stream
```

## Enter (connect to) running container
```
docker container exec -it test-production bash
```

## Review Docker disk usage
```
docker system df -a
```
