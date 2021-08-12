    ```
    1  docker volume ls 
    2  docker volume create my-vol
    3  docker volume ls 
    4  docker volume inspect my-vol
    5  ls -ltr /var/lib/docker/volumes/my-vol/_data/
    6  docker run -it --name vol-test-1 -v my-vol:/app ubuntu:16.04 
    7  docker ps 
    8  docker ps -a
    9  ls -ltr /var/lib/docker/volumes/my-vol/_data/
   10  cat  /var/lib/docker/volumes/my-vol/_data/hello.txt 
   11  docker rm vol-test-1
   12  docker ps 
   13  docker ps -a
   14  docker volume ls 
   15  cat  /var/lib/docker/volumes/my-vol/_data/hello.txt
   16  docker run -it --name vol-test-2 -v my-vol:/app ubuntu:16.04 
   17  ls
   18  docker ps 
   19  docker rm $(docker ps -qa) 
```

```
   20  echo "=========================== Demo 2 ==============================="
   21  docker run -it --name vol-test-3 -v /var/www/html/amit ubuntu:16.04 
   22  docker ps 
   23  docker inspect vol-test-3
   24  docker volume ls 
   25  docker volume inspect 6225ec3b077da96ed49978f9a0354e6154a7ef70a6b6331d522099208235f45d
   26  cat /var/lib/docker/volumes/6225ec3b077da96ed49978f9a0354e6154a7ef70a6b6331d522099208235f45d/_data/hey_amit.txt 
   27  hostname >> /var/lib/docker/volumes/6225ec3b077da96ed49978f9a0354e6154a7ef70a6b6331d522099208235f45d/_data/hey_amit.txt
   28  date >> /var/lib/docker/volumes/6225ec3b077da96ed49978f9a0354e6154a7ef70a6b6331d522099208235f45d/_data/hey_amit.txt
   29  docker ps 
   30  docker attach vol-test-3
```

```   
   31  echo "=========================== Demo 3 ==============================="
   32  ls
   33  pwd
   34  cd Docker-PWC-07-Aug-2021/
   35  ls
   36  pwd
   37  docker run -it --name vol-test-4 -v /root/Docker-PWC-07-Aug-2021:/var/www/html/amit ubuntu:16.04 
   38  ls
   39  docker run -it --name vol-test-5 -v /root/Docker-PWC-07-Aug-2021:/var/www/html/amit:ro ubuntu:16.04 
   40  ls
   41  rm 1.txt 
   42  ls
```   

```
   43  echo "=========================== Demo 4 ==============================="
   44  docker run -itd --name datacontainer -v /var/log/amit -v /var/www/amit -v /etc/amit -v /opt/sp/amit ubuntu:16.04 
   45  docker ps 
   46  docker inspect datacontainer
   47  docker run -itd  --name test-1 --volumes-from datacontainer ubuntu:16.04
   48  docker run -itd  --name test-2 --volumes-from datacontainer ubuntu:16.04
   49  docker run -itd  --name test-3 --volumes-from datacontainer ubuntu:16.04
   50  docker run -itd  --name test-4 --volumes-from datacontainer ubuntu:16.04
   51  docker ps 
   52  docker inspect test-4
   53  docker ps 
   54  docker run -d  --name test-5 --volumes-from datacontainer ubuntu:16.04 sh -c "while true; do $(echo date) >> /opt/sp/amit/date.txt;sleep 1; done"
   55  docker ps 
   56  cat /var/lib/docker/volumes/4bbc9a16ac792a4293a42b1cfe91c41f555f68a4fcca2b3291159d4c5d257530/_data/date.txt 
   57  tail -f  /var/lib/docker/volumes/4bbc9a16ac792a4293a42b1cfe91c41f555f68a4fcca2b3291159d4c5d257530/_data/date.txt 
   58  docker ps 
   59  docker exec -it test-1 cat /opt/sp/amit/date.txt
   60  docker exec -it test-2 cat /opt/sp/amit/date.txt
   61  docker exec -it test-3 cat /opt/sp/amit/date.txt
   62  docker exec -it test-4 tail -f  /opt/sp/amit/date.txt
   63  ls
   64  cd 03-Docker-Volumes/
   65  ls
   66  docker kill $(docker ps -qa)
   67  docker rm $(docker ps -qa)
   68  docker ps -a
   69  docker volume ls 
   70  docker volume ls -q 
   71  docker volume rm $(docker volume ls -q )
   72  docker volume ls 
   73  ls
   74  history >> README.md 
```
