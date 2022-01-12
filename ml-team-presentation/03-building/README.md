Building 'production' image

# Build

```
docker build -t test-build .
```

# Run

```
docker run --rm -it -p 8000:8000 -v database_volume:/database test-build 
```
