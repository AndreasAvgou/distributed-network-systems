import socket
import threading
import time

# Node configuration
class EchoNode:
    def __init__(self, host, port, neighbors):
        self.host = host
        self.port = port
        self.neighbors = neighbors  # List of (host, port) tuples
        self.parent = None
        self.ack_count = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.lock = threading.Lock()

    def send_message(self, message, neighbor):
        """Sends a message to a specific neighbor."""
        self.server_socket.sendto(message.encode(), neighbor)
        print(f"Node {self.port} sent message to {neighbor}")

    def listen(self):
        """Listens for incoming messages."""
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode()
            print(f"Node {self.port} received message: {message} from {addr}")
            self.process_message(message, addr)

    def process_message(self, message, sender):
        """Processes incoming messages."""
        with self.lock:
            if message == "INIT":
                if self.parent is None:
                    self.parent = sender
                    for neighbor in self.neighbors:
                        if neighbor != sender:
                            self.send_message("ECHO", neighbor)
            elif message == "ECHO":
                self.ack_count += 1
                if self.ack_count == len(self.neighbors) - (1 if self.parent else 0):
                    if self.parent:
                        self.send_message("ECHO", self.parent)
                    print(f"Node {self.port} has completed the echo process.")

    def start(self):
        """Starts the node's server thread."""
        threading.Thread(target=self.listen, daemon=True).start()

# Example setup
if __name__ == "__main__":
    # Define nodes and their neighbors (for simplicity, using localhost)
    node1 = EchoNode('127.0.0.1', 6000, [('127.0.0.1', 6001), ('127.0.0.1', 6002)])
    node2 = EchoNode('127.0.0.1', 6001, [('127.0.0.1', 6000), ('127.0.0.1', 6002)])
    node3 = EchoNode('127.0.0.1', 6002, [('127.0.0.1', 6000), ('127.0.0.1', 6001)])

    # Start nodes
    node1.start()
    node2.start()
    node3.start()
    
    time.sleep(2)  # Allow nodes to start listening

    # Initiate echo algorithm from Node 1
    print("Node 1 initiating echo...")
    node1.send_message("INIT", ('127.0.0.1', 6000))

    while True:
        time.sleep(1)  # Keep the script running
