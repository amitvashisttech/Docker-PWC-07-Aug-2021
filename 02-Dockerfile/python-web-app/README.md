```
   34  mkdir python-web-app
   35  cd python-web-app/
   36  ls
   37  vim app.py
   38  ls
   39  vim req.txt
   40  ls
   41  mkdir app-code
   42  ls
   43  mv * app-code/
   44  ls
   45  vim Dockerfile
   46  ls
   47  mkdir v1
   48  ls
   49  mv * v1
   50  ls
   51  cd v1/
   52  ls
   53  docker build -t mypython-web-app:v1 .
   54  vim Dockerfile
   55  docker build -t mypython-web-app:v1 .
   56  vim Dockerfile
   57  ls
   58  docker build -t mypython-web-app:v1 .
   59  docker image
   60  docker images
   61  docker run -d --name test-py-1 mypython-web-app:v1
   62  docker ps
   63  docker ps -a
   64  docker logs 3a6f383a5a00
   65  ls
   66  cd app-code/
   67  ls
   68  vim app.py
   69  ls
   70  cd ..
   71  ls
   72  docker build -t mypython-web-app:v1 .
   73  docker run -d --name test-py-2 mypython-web-app:v1
   74  docker ps
   75  docker inspect 93823f1432b8
   76  curl 172.17.0.3
   77  curl 172.17.0.3:8081
```
