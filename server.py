import socket

def server_program():
    host = 'localhost'
    port = 2100  # initiate port number above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("Server application is running...")
    print("Server is waiting for client...")

    conn, address = server_socket.accept()  # accept new connection
    print("Server gets successfully connected...")
    print("Marvellous Messenger started...")
    print("Connection from: " + str(address))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Client says: " + str(data))
        message = input('Enter message for client: ')  # take input

        conn.send(message.encode())  # send data to the client

    conn.close()  # close the connection
    print("Thank you for using Marvellous Messenger..")

if __name__ == '__main__':
    server_program()
