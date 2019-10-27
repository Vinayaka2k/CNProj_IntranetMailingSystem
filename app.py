from flask import Flask,render_template,request
import sys
app = Flask(__name__)
from socket import *
from _thread import * #Py3K changed it.
serverName = 'localhost'
serverPort = 1200


#def clientthread(clientSocket):

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#start_new_thread(clientthread,(clientSocket,))
	


@app.route("/")
def inbox():
	res = ""
	while (res == ""):	
		res = clientSocket.recv(2048)
	return "<table> <th>From</th> <th>To</th> <th>Body</th>"+  res.decode() + "</table>", {'Content-Type': 'text/html'}
	

@app.route("/form",methods=['POST' , 'GET'])
def form():
	return render_template('form.html')

@app.route("/send",methods=['POST' , 'GET'])
def send():
	if request.method == 'POST':
		result=request.form
		message = result['to'] + '\t' +result['message']
		clientSocket.send(message.encode())
	return render_template('inbox.html')

	
@app.route("/response")
def response():
	return "<h1>Hello, World!</h1>", {'Content-Type': 'text/html'}


