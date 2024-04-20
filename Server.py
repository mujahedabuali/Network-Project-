import socket #the library that the sockets and related methods in and it is used to creat the server
import time #for the 10 seconds timer
import subprocess #the library that contains lock screen method

#defining the method that validates student id the message reseved will only cintain the 7 digits student id
def howManyDigits(id):#this method checks if the id that was sent from client is 7 digits long
    count=len(str(id)) #we count the digits in many ways one of them is this built in function/count represents the number of digits
    return count==7 #will return true if count ==7 else will return false

def isValid(ID):#this method takes a student id as a parameter then decides if it is one of the 3 ids or not after checking if it is 7 didits long
   check=howManyDigits(ID)#we imlemented this method to save time
   groupIdList=[1221098, 1211047, 1202199]
   return check and ID in groupIdList #if number of digets is 7 and the ID is in the range of the three selected ids then return true else return false

#implementing the server
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#a socket object/socket.AF_INET specifies the address (and protocol) family, in this case, IPv4./socket.SOCK_STREAM specifies the socket type, in this case, a TCP socket
#just to know that the socket is created
print("socket created")
#listening on port
port= 9955
#binding the port the bind method taked 2 parameters the ip number and port,ip number is for local host but we can leave it empty to send and reseve from multiple computers
s.bind(('127.0.0.1',port))#the method socket.gethostname() will get the local host ip adress//the used ip adress means:  the server to only accept connections originating from the same machine/we can also use localhost wich has the same meaning
print('socket binded to port')#to know that the socket is bound
#put the socket in listening mode
s.listen(1)#five is the number of connections the socket can handle
print("server is listening")
#we will use an infinite loop until the student id is sent if not sent keep reseving messages
while True:
   
    c_socket , c_adrress=s.accept() #c:client socket , adrr:client adress, the server accepts the connection//.accept() returns two values
    print(f'connected with client{c_adrress}')#will delete
    resevedId = c_socket.recv(1024).decode()# the method .recv(1024) reseves a msg from client and the argument declares the max amount of data reseved ,but client can send less than that
    studentId=int(resevedId)
    #the method decode is to convert the msg from byte stream to character stream
    idValidation=isValid(int(studentId))#first convert from string to in then compare
    if idValidation:
        #these lines can be also implemented in idValidation fanction
        msg=('sever will lock screen after 10 seconds')#the msg that the server will send
        c_socket.send(msg.encode())#this method send msg in form of bytes because of that we used encode method to convert the message
        print(msg)
        time.sleep(10) #the method .sleep is to make the server wait 10 seconds then contenue
        subprocess.run(["/usr/bin/pmset", "displaysleepnow"]) #this is a built method from ctypes that locks a windowes os computer
        #close the connection but after or before shutting down the os?
        c_socket.close()
        s.close()
        break

       
    else:
      print("Invalid student ID received.")#used print because this msg will apear on server side not client
    c_socket.close()
    s.close()
    break

#"C:/Program Files/Python312/python.exe" "c:/Users/HP/Desktop/cyber security/2.nd year/2.1sem/PYTHON/Client.Server/Server.py"




