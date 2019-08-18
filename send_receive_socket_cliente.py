HEADER_LENGTH = 10
def send(message,client_socket):
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + message)


def receive(client_socket):
    username_header = client_socket.recv(HEADER_LENGTH)
    

    # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
    if not len(username_header):
        print('Connection closed by the server')
        sys.exit()

    # Convert header to int value
    username_length = int(username_header.decode('utf-8').strip())

    # Receive and decode username
    username = client_socket.recv(username_length).decode('utf-8')

    # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
    message_header = client_socket.recv(HEADER_LENGTH)
    message_length = int(message_header.decode('utf-8').strip())
    message = client_socket.recv(message_length).decode('utf-8')
    return (username,message)

def receive2(client_socket):
    message = client_socket.recv(9).decode('utf-8')
    return (message)
