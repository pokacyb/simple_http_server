from socket import *


def createServer():
    # Create and endpoint
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        # Can receive connections on port 9000
        serversocket.bind(('localhost',9000))
        # Queue incoming connections
        serversocket.listen(5)
        # Wait for incoming requests
        while(1):
            # Sits and wait for connections
            (clientsocket, address) = serversocket.accept()

            # Read some data
            rd = clientsocket.recv(5000).decode()
            # Split it based on newlines
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            # Response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset-utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            # Close connection
            clientsocket.shutdown(SHUT_WR)

    # Error handling and clean up
    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()