import socket
import threading
import time
import uuid

class RealTimeFloodingNode:
    def __init__(self, host, port, neighbors):
        self.host = host
        self.port = port
        self.neighbors = neighbors  # List of (host, port) tuples
        self.received_messages = set()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.running = True
        
    def send_message(self, message, neighbor):
        """Sends a message to a specific neighbor."""
        self.server_socket.sendto(message.encode(), neighbor)
        print(f"Node {self.port} sent message to {neighbor}")

    def flood_message(self, message, sender):
        """Forwards the message to all neighbors except the sender."""
        if message not in self.received_messages:
            self.received_messages.add(message)
            for neighbor in self.neighbors:
                if neighbor != sender:
                    self.send_message(message, neighbor)

    def listen(self):
        """Listens for incoming messages."""
        while self.running:
            try:
                data, addr = self.server_socket.recvfrom(1024)
                message = data.decode()
                print(f"Node {self.port} received message: {message} from {addr}")
                self.flood_message(message, addr)
            except Exception as e:
                print(f"Error in node {self.port}: {e}")

    def user_input(self):
        """Allows the user to send messages dynamically."""
        while self.running:
            message = input(f"Enter message to flood from Node {self.port}: ")
            unique_message = f"{uuid.uuid4()}:{message}"  # Unique ID to avoid loops
            self.flood_message(unique_message, None)

    def start(self):
        """Starts the node's server threads for listening and user input."""
        threading.Thread(target=self.listen, daemon=True).start()
        threading.Thread(target=self.user_input, daemon=True).start()

if __name__ == "__main__":
    node1 = RealTimeFloodingNode('127.0.0.1', 8000, [('127.0.0.1', 8001), ('127.0.0.1', 8002)])
    node2 = RealTimeFloodingNode('127.0.0.1', 8001, [('127.0.0.1', 8000), ('127.0.0.1', 8002)])
    node3 = RealTimeFloodingNode('127.0.0.1', 8002, [('127.0.0.1', 8000), ('127.0.0.1', 8001)])

    node1.start()
    node2.start()
    node3.start()
    
    time.sleep(2)  # Allow nodes to start listening
    print("Real-time Flooding nodes are running. Enter messages to flood.")
    
    while True:
        time.sleep(1)  # Keep the script running
