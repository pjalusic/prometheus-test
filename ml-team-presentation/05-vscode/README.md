# Requirements
- Install VSCode
- Install extensions:
  - Docker
  - Remote - SSH
    
![img.png](img.png)

# Exercise

## Connect to container graphically

### Forward port
```
ssh -NL 3000:localhost:3000 <user>@<ip>
```

### Open browser on [localhost:3000](http://localhost:3000/)

## Connect to container in terminal

![img_1.png](img_1.png)  
(it will automatically fetch all hosts from default `~/.ssh/config`)

- once you are connected to host click on docker icon:  

![img_2.png](img_2.png)
  
- review containers:  

![img_3.png](img_3.png)
  
- even open in browser without any explicit port forward command:  

![img_4.png](img_4.png)