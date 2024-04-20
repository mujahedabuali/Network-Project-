#creat the client 
import socket

c_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#this is an object for the client
c_socket.connect(('127.0.0.1',9955)) #here we are not going to bind as we did in the server but we will connect it with the server using the method .connect(('server ip adress',server port number))
#we used double brackets because this method takes only one argument so when using double brackets the tow arguments will apear as one
client_message=input('Enter student id: ')#the client will enter the id
c_socket.send(client_message.encode())#the id sent to server// do not forget ()
fromServerToClient=c_socket.recv(1024).decode()#client reseved a message from server that OS will lock screen after 10 seconds or will not reseve any thing because the error msg will only show at server side
print(fromServerToClient)
c_socket.close#it is very important to close this connection

#"C:/Program Files/Python312/python.exe" "c:/Users/HP/Desktop/cyber security/2.nd year/2.1sem/PYTHON/Client.Server/Client.py"
#/Users/mujahedabuali/Documents/Network/Network_Proj1/part2