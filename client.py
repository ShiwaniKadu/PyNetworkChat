import socket

def client_program():
    host = 'localhost'  # as both code is running on same pc
    port = 2100  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("Marvellous Messenger started...\nEnter message for server: ")  # take input

    while message.lower().strip() != 'end':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Server says: ' + data)  # show in terminal

        message = input("Enter message for server: ")  # again take input

    client_socket.close()  # close the connection
    print("Thank you for using Marvellous Messenger..")

if __name__ == '__main__':
    client_program()
