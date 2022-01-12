Local development and running in Docker

# Build
```
docker build -t test-volumes .
```

# Run
```
docker run --rm -it -v $(pwd):/ --entrypoint bash test-volumes
```

## Fix

```
docker run --rm -it -p 8000:8000 -v $(pwd):/ --entrypoint bash test-volumes
```