#!/usr/bin/env python3
import socket
import threading
import sys

# Server configuration constants
SERVER_NAME = "Server of John Q. Smith"
SERVER_PORT = 5001      # Port number (must be greater than 1023)
SERVER_NUM = 50         # The server's predetermined number

def handle_client(client_socket, client_address):
    """
    Handles an individual client connection.
    This function is executed in a separate thread for each client.
    """
    print(f"[INFO] Received connection from {client_address}.")
    try:
        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            print("[ERROR] No data received from the client.")
            client_socket.close()
            return

        # Expected data format: "Client of John Q. Smith;[number]"
        parts = data.strip().split(";")
        if len(parts) != 2:
            print(f"[ERROR] Data format incorrect: {data}")
            client_socket.close()
            return

        # Extract the client's name and number from the message
        client_name = parts[0]
        try:
            client_number = int(parts[1])
        except ValueError:
            print("[ERROR] The client's number is not a valid integer.")
            client_socket.close()
            return

        print(f"[INFO] Received number {client_number} from {client_name}.")
        print(f"[INFO] Server name: {SERVER_NAME}")

        # Check if the received number is within the valid range (1-100)
        if client_number < 1 or client_number > 100:
            print(f"[INFO] Received out-of-range number {client_number}. Shutting down the server.")
            client_socket.close()
            # Shut down the entire server if an invalid number is received
            sys.exit(0)

        # Calculate the sum of the client's number and the server's predetermined number
        total_sum = client_number + SERVER_NUM
        print(f"[INFO] Calculation: {client_number} (client) + {SERVER_NUM} (server) = {total_sum}")

        # Construct the response message in the format: "Server of John Q. Smith;[SERVER_NUM]"
        reply = f"{SERVER_NAME};{SERVER_NUM}"
        client_socket.send(reply.encode("utf-8"))
        print(f"[INFO] Sent reply to client: {reply}")

    except Exception as e:
        print(f"[ERROR] Exception occurred while handling the client: {e}")
    finally:
        # Close the client socket regardless of what happens
        client_socket.close()
        print(f"[INFO] Connection with {client_address} closed.\n")

def start_server():
    """
    Starts the server, binds to a port, and listens for incoming connections.
    Each incoming connection is handled in a separate thread.
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Bind the socket to all available network interfaces on the specified port
        server_socket.bind(("", SERVER_PORT))
    except Exception as e:
        print(f"[ERROR] Could not bind to port {SERVER_PORT}: {e}")
        sys.exit(1)
    
    # Start listening for incoming connections (allow up to 5 queued connections)
    server_socket.listen(5)
    print(f"[INFO] Server is listening on port {SERVER_PORT}...")

    while True:
        try:
            # Accept a new client connection
            client_socket, client_address = server_socket.accept()
            # For each connection, create a new thread to handle it concurrently
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True  # Daemon threads will automatically close when the main program exits
            client_thread.start()
        except KeyboardInterrupt:
            # Allow the server to be stopped with Ctrl+C
            print("\n[INFO] Keyboard interrupt received. Shutting down the server...")
            server_socket.close()
            break

if __name__ == "__main__":
    start_server()
