from flask import Flask 
import os 
import socket


app = Flask(__name__)

@app.route("/")
def hello():
  html= "<h2>Hello World</h1>"
  return html


@app.route("/hello")
def hello_test():
  html= "<h2>Welcome to docker based python Web Application</h1>"
  return html


@app.route("/info")
def hello_info():
  html= "<h2>Hello World</h1>"\
         "<b>Hostname: </b> {hostname}<br/>"\
         "<b>FQDN: </b> {fqdn}<br/>"
  return html.format(hostname=socket.gethostname(),fqdn=socket.getfqdn())



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8081)
