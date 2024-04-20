from socket import *

servSocket=socket(AF_INET,SOCK_STREAM) #make TCP socket for request,AF_INET-> IPv4,SOCK_STREAM->It provides a reliable, connection-oriented
servSocket.bind(("",9966)) #bind server to port number "serverPort" 
servSocket.listen(1) #open server listen for TCP connection requests,1 connections that can be waiting (in the queue) while the server is busy
print("The web server is ready to receive") 

while True:
    conSocket, addr=servSocket.accept() #waits until a client connects to the server.
    sentence = conSocket.recv(1024).decode()#receives data from the conSocket,1024 byte maxmimum data, decode method is used to convert these bytes into a string
    print(f"address:{addr}") #('127.0.0.1', 53932) ip and port
    print(F"sentenve:{sentence}")
    ip=addr[0]
    port=addr[1]
    object=sentence.split()[1]   #Get the reqested object from client
    print("\nThe HTTP request is:", object)     #print the HTTP request

    if (object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en'): # if statement checks whether the requested object
        conSocket.send("HTTP/1.1 200 OK \r\n".encode()) #it sends an HTTP response with a "200 OK"
        conSocket.send("Content-Type: text/html;charset=UTF-8\r\n".encode()) # send the HTML file
        conSocket.send("\r\n".encode())
        file1=open("main_en.html", "rb") #server should send main_en.html file
        conSocket.send(file1.read()) #read the file that was open

    elif (object == '/ar'): #If object '/ar', it will send the same HTTP status code and content type,
        # but will serve the contents of the file "main_ar.html" instead. --> (sending a similar HTTP response with a different HTML file as the body).
        conSocket.send("HTTP/1.1 200 OK \r\n".encode())
        conSocket.send("Content-Type: text/html \r\n".encode())
        conSocket.send("\r\n".encode())
        file2=open("main_ar.html", "rb")
        conSocket.send(file2.read())

    elif (object.endswith('.html')): # If the object ends with '.html', the server sends an HTTP response with a 200 OK status and a Content-Type
        # The server then opens the file "l1.html" and sends its contents as the response body.
        conSocket.send("HTTP/1.1 200 OK \r\n".encode())
        conSocket.send("Content-Type: text/html; charset=UTF-8 \r\n".encode())
        conSocket.send("\r\n".encode())
        file3=open("l1.html", "rb")
        conSocket.send(file3.read())

    elif (object.endswith('.css')): # If the object ends with '.css', the server sends a similar HTTP response with
        # The server then opens the file "styles.css" and sends its contents as the response body.
        conSocket.send("HTTP/1.1 200 OK \r\n".encode())
        conSocket.send("Content-Type: text/css; charset=UTF-8 \r\n".encode())
        conSocket.send("\r\n".encode())
        file4 = open("style.css", "rb")
        conSocket.send(file4.read())

    elif(object == "/images/p1.png"):
            conSocket.send("HTTP/1.1 200 OK \r\n".encode())
            conSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
            conSocket.send("\r\n".encode())
            f1 = open("images/p1.png", "rb")
            data = f1.read()
            conSocket.send(data)
    
    elif(object == "/images/p2.jpg"):
            conSocket.send("HTTP/1.1 200 OK \r\n".encode())
            conSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
            conSocket.send("\r\n".encode())
            f1 = open("images/p2.jpg", "rb")
            data = f1.read()
            conSocket.send(data)

    elif(object == "/images/flag.png"):
            conSocket.send("HTTP/1.1 200 OK \r\n".encode())
            conSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
            conSocket.send("\r\n".encode())
            f1 = open("images/flag.png", "rb")
            data = f1.read()
            conSocket.send(data)       
    
    elif (object.endswith('.png')): # files with the extensions '.png'
        conSocket.send("HTTP/1.1 200 OK \r\n".encode())
        conSocket.send("Content-Type: image/png \r\n".encode())
        conSocket.send("\r\n".encode())
        file5 = open("images/birzeit.png", "rb")
        conSocket.send(file5.read())

    elif (object.endswith('.jpg')):#The same process occurs for '.jpg' files,
        conSocket.send("HTTP/1.1 200 OK \r\n".encode())
        conSocket.send("Content-Type: image/jpeg \r\n".encode())
        conSocket.send("\r\n".encode())
        file6 = open("images/aqsa.jpg", "rb")
        conSocket.send(file6.read())

    elif (object == '/cr'): #status code 307 Temporary Redirect: If the request is for '/cr',
        # the Location header set to cornell
        conSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        conSocket.send("Content-Type: text/html \r\n".encode())
        conSocket.send("Location: https://cornell.edu \r\n".encode())
        conSocket.send("\r\n".encode())

    elif (object == '/so'): #if the request is for '/so', the server sends a 307 Temporary Redirect
        # instructing the client to make a new request to Stack Overflow.
        conSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        conSocket.send("Content-Type: text/html \r\n".encode())
        conSocket.send("Location: https://stackoverflow.com \r\n".encode())
        conSocket.send("\r\n".encode())

    elif (object == '/rt'):#HTTP request that includes the string "/bzu" in the URL. If this string is present.
        conSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode()) #HTTP response to the client with a "307 Temporary Redirect" status code
        conSocket.send("Content-Type: text/html \r\n".encode())
        conSocket.send("Location: https://ritaj.birzeit.edu \r\n".encode())# HTTP response with the Location header set to birzeit edu
        conSocket.send("\r\n".encode())

    else: # where a requested resource is not found .
        conSocket.send("HTTP/1.1 404 Not Found \r\n".encode())#the server sends a 404 Not Found HTTP response to the client
        conSocket.send("Content-Type: text/html \r\n".encode()) #type text HTML
        conSocket.send("\r\n".encode())
        notFoundHtmlString = "<html>"\
                              "<head>"\
                              "<title>Error 404</title>"\
                               "</head>"\
                               "<body style='background-color: white;'>"\
                               "<div>"\
                               "HTTP/1.1 404 Not Found <hr>"\
                               "<p style='font-size: 30px; background-color: black; color:white; text-align: center; border-style: ridge;border-color: white; border-width: thick; text-align: center;padding-bottom:8px'>"\
                               "Sorry The request is WRONG !!!!</p> <hr>"\
                               "<p style ='font-size: 45px; font-family: georgia;text-align:center; color:Red'>"\
                               "<strong>"\
                                "The file is not found </strong> </p>"\
                               "<pre style ='font-size: 25px; font-family: arial ;text-align:center; color:Black'> <br>"\
                               "<b>     Name: Mujahed Abuali #121107 <br/>"\
                                "Name: Ziad masalma #1202199<br/>"\
                                "Name: manal nidal #1221098<br/><br/><br/>"\
                                "</b>"\
                                "</pre>"\
                                "<pre style='font-size: 40px; font-family: arial;text-align:center; color:Black'><br>"\
                                 f"IP: {ip}     "\
                                 f"Port: {port}"\
                                 "</pre>"\
                                 "</div>"\
                                 "</body>"\
                                 "</html>"
        #if the request is wrong or the file doesnt exist the server should return a simple HTML webpage that contains with
        #some design and color needed
        notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
        conSocket.send(notFoundHtmlBytes)

    conSocket.close() #close the connection
