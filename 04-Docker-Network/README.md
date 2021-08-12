```
    2  mkdir 04-Docker-Network
    3  ls
    4  cd 04-Docker-Network/
    5  ls
    6  docker ps 
    7  docker ps -a
    8  cd 
    9  ls
   10  docker network ls 
   11  docker network inspect bridge
   12  ip addr 
   13  docker run -itd --name test-nw-1 ubuntu:16.04
   14  docker ps 
   15  docker inspect test-nw-1
   16  docker run -itd --name test-nw-2 ubuntu:16.04
   17  docker inspect test-nw-2
   18  docker network inspect bridge
   19  docker images 
   20  docker run -d --name test-nw-3 mypython-web-app:v3
   21  docker ps 
   22  docker network inspect bridge
   23  curl 172.17.0.4:8081/info
   24  curl localhost:8081/info
   25  route -n 
   26  ip addr 
   27  docker ps 
   28  netstat -tulnp 
   29  docker run -d --name test-nw-4 -p 8080:8081 mypython-web-app:v3
   30  docker ps 
   31  netstat -tulnp 
   32  curl localhost:8081/info
   33  curl localhost:8080/info
   34  systemctl status docker
   35  curl localhost:8080/info
   36  ip addr 
   37  docker run -d --name test-nw-5 -p 8080:8081 mypython-web-app:v3
   38  netstat -tulnp 
   39  docker run -d --name test-nw-6 -p 8082:8081 mypython-web-app:v3
   40  docker run -d --name test-nw-7 -p 8083:8081 mypython-web-app:v3
   41  docker ps 
   42  docker run -d --name test-nw-10 -P mypython-web-app:v3
   43  docker run -d --name test-nw-11 -P mypython-web-app:v3
   44  docker ps 
   45  docker network inspect bridge
   46  docker ps 
   47  ls
   48  cd Docker-PWC-07-Aug-2021/
   49  ls
   50  cd 04-Docker-Network/
   51  ls
   52  history > README.md
```
