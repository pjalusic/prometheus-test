Local development and running in Docker

# Build
```
docker build -t test-volumes .
```

# Run
```
docker run --rm -it -p 8000:8000 -v $(pwd):/app test-volumes
```

# Check folder structure

```
docker run --rm -it -p 8000:8000 -v $(pwd):/app --entrypoint bash test-volumes
```