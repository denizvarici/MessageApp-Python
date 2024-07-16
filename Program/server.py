import socket
import threading

HOST = "127.0.0.1"
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []
clients_lock = threading.Lock()

def send_message_to_client(client, message):
    client.sendall(message.encode())

def send_messages_to_all(message):
    with clients_lock:
        for user in active_clients:
            send_message_to_client(user[1], message)

def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = f"{username}~{message}"
                send_messages_to_all(final_msg)
        except:
            # Client disconnected here
            with clients_lock:
                active_clients.remove((username, client))
            send_messages_to_all(f"SERVER~{username} left the chat.")
            client.close()
            break

def client_first_connected(client):
    try:
        username = client.recv(2048).decode('utf-8')
        if username:
            with clients_lock:
                active_clients.append((username, client))
            server_message = f"SERVER~{username} joined the chat."
            send_messages_to_all(server_message)
            threading.Thread(target=listen_for_messages, args=(client, username)).start()
        else:
            print("Empty username problem")
    except:
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print("Server is running")
    except:
        print("server.bind doesn't work")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Client connected {address}")
        threading.Thread(target=client_first_connected, args=(client,)).start()

if __name__ == "__main__":
    main()