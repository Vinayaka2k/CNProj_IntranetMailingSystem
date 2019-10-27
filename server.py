from socket import *
import select , sqlite3
import random,sys
import string

#from thread import *
from _thread import * #Py3K changed it.
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
serverSocket.listen(1)
list_of_clients=[]


def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))


print("The server is ready to receive")

def clientthread(conn,uname):
	while True:
		data = conn.recv(2048)    
		if data :	
			data = data.decode()
			li = data.split('\t')	
			storeMessage(uname,li[0],li[1])

def storeMessage(cfrom,cto,message) :
	db_conn = sqlite3.connect('a.db')
	#conn.execute('''CREATE TABLE CLIENT
	#	(CFROM TEXT NOT NULL,
	#	CTO TEXT NOT NULL,
	#	CMESSAGE TEXT NOT NULL );''')
	db_conn.execute("INSERT INTO CLIENT VALUES (?,?,?)",(cfrom,cto,message));
	db_conn.commit()  
	db_conn.close()

'''
def sendTo(conn,data):
	for client in list_of_clients:
		if client != conn :
			client.send(data)		
'''

def foo(conn,cto) :
	#sent = 0
	#while(True) :
		s = ""	
		db_conn = sqlite3.connect('a.db')
		cursor = db_conn.execute("SELECT * FROM CLIENT WHERE CTO = (?)",(cto,))
		for row in cursor:
			s += "<tr>" + "<td>" + row[0] + "</td>" + "<td>" + row[1] + "</td>"  + "<td>" + row[2] + "</td>" + "</tr>"
		db_conn.close()
		r = conn.send(s.encode())
		if(r):
			break

user = {}		
while True:
	conn, addr = serverSocket.accept()
	list_of_clients.append(conn)
	host , port = conn.getpeername()	
	uname = conn.recv(2048)	
	user[uname] = port	    
	print(user)
	start_new_thread(foo,(conn,uname))
	start_new_thread(clientthread,(conn,uname))
	
conn.close()
server.close()
