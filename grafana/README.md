# Grafana
- https://grafana.com/docs/grafana/latest/installation/docker/
- https://grafana.com/grafana/download?pg=get&plcmt=selfmanaged-box1-cta1&platform=docker
- https://prometheus.io/docs/visualization/grafana/
  - use `host.docker.internal` or container name instead of `localhost` when setting Prometheus data source.  
    for instance `http://host.docker.internal:9090/`  
    as per https://docs.docker.com/desktop/mac/networking/#use-cases-and-workarounds
    
# Node exporter
- https://prometheus.io/docs/guides/node-exporter/
- https://github.com/vegasbrianc/prometheus/blob/master/pwd-stack.yml#L40
- https://github.com/prometheus/node_exporter/issues/610#issuecomment-336685496:
```
Here is the command that worked for me on Docker for Mac:

docker service create --name node \
 --mode global \
 --mount type=bind,source=/proc,target=/host/proc \
 --mount type=bind,source=/sys,target=/host/sys \
 --mount type=bind,source=/,target=/rootfs \
 --network prom \
 prom/node-exporter \
  --path.procfs /host/proc \
  --path.sysfs /host/sys \
  --collector.filesystem.ignored-mount-points "^/(sys|proc|dev|host|etc)($|/)"

prom is a separately created overlay network.
```