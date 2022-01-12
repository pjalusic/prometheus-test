Local development and running in Docker

# Build
```
docker build -t test-bind-mound .
```

# Run
```
docker run --rm -it -v $(pwd):/usr/src/project --entrypoint bash test-bind-mound
```

## Fix

```
docker run --rm -it -p 8000:8000 -v $(pwd):/usr/src/project --entrypoint bash test-bind-mound
```