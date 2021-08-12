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


```
 61  echo "========================== Demo 2 =============================="
   62  docker network ls
   63  docker ps
   64  docker kill $(docker ps -qa )
   65  docker rm $(docker ps -qa )
   66  docker network ls
   67  docker network create --help
   68  docker network create --driver=bridge --subnet=172.28.0.0/16 --ip-range=172.28.5.0/24 --gateway=172.28.5.254 mybr0
   69  docker ps
   70  docker network ls
   71  docker network inspect mybr0
   72  docker run -d --name test-nw-12 --network "mybr0" -P mypython-web-app:v3
   73  docker run -d --name test-nw-13 --network "mybr0" -P mypython-web-app:v3
   74  docker network inspect mybr0
   75  docker ps
   76  docker run -itd --name test-1 ubuntu:16.04
   77  docker exec -it test-1 ip addr
   78  docker ps
   79  docker inspect test-1
   80  docker run -d --name test-nw-14 --network none mypython-web-app:v3
   81  docker ps
   82  docker inspect test-nw-14
   83  ls
   84  docker kill $(docker ps -qa )
   85  docker rm $(docker ps -qa )
   86  docker network ls
   87  netstat -tulnp
   88  docker run -d --name test-nw-16 --network host mypython-web-app:v3
   89  docker ps
   90  docker inspect test-nw-16
   91  netstat -tulnp
   92  curl localhost:8081
   93* ps -ef
   94  curl localhost:8081 | grep -i python
   95  ps -ef  | grep -i python
   96  ip addr
   97  docker run -d --name test-nw-17 -P  mypython-web-app:v3
   98  docker ps
   99  netstat -tulnp
  100  systemctl status docker
```
