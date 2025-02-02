#!/usr/bin/env python3
import socket

def start_client():
    # Prompt the user for an integer input between 1 and 100
    user_input = input("Please enter an integer between 1 and 100: ")
    try:
        client_number = int(user_input)
    except ValueError:
        print("[ERROR] Invalid input. Please enter a valid integer.")
        return

    # Format the message as "Client of John Q. Smith;[number]"
    message = f"Client of John Q. Smith;{client_number}"

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP and port (using localhost for testing)
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5001

    try:
        # Connect to the server
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"[INFO] Connected to server at {SERVER_IP}:{SERVER_PORT}")

        # Send the formatted message to the server
        client_socket.send(message.encode("utf-8"))
        print(f"[INFO] Sent message: {message}")

        # Wait for the server's response (up to 1024 bytes)
        response = client_socket.recv(1024).decode("utf-8")
        if not response:
            print("[ERROR] No response received from the server.")
            return

        # Expected response format: "Server of John Q. Smith;[server_number]"
        parts = response.strip().split(";")
        if len(parts) != 2:
            print("[ERROR] Server response format is incorrect.")
            return

        # Extract the server's name and number
        server_name = parts[0]
        try:
            server_number = int(parts[1])
        except ValueError:
            print("[ERROR] The server's number is not a valid integer.")
            return

        # Calculate the sum of the client's number and the server's number
        total_sum = client_number + server_number

        # Display the server's information and the sum
        print(f"[INFO] Received response from {server_name} with number {server_number}.")
        print(f"[INFO] Calculation: {client_number} (client) + {server_number} (server) = {total_sum}")

    except Exception as e:
        print(f"[ERROR] Exception during communication: {e}")
    finally:
        # Always close the socket after the communication is done
        client_socket.close()
        print("[INFO] Client socket closed.")

if __name__ == "__main__":
    start_client()
#!/usr/bin/env python3
import socket

def start_client():
    # Prompt the user for an integer input between 1 and 100
    user_input = input("Please enter an integer between 1 and 100: ")
    try:
        client_number = int(user_input)
    except ValueError:
        print("[ERROR] Invalid input. Please enter a valid integer.")
        return

    # Format the message as "Client of John Q. Smith;[number]"
    message = f"Client of John Q. Smith;{client_number}"

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP and port (using localhost for testing)
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5001

    try:
        # Connect to the server
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"[INFO] Connected to server at {SERVER_IP}:{SERVER_PORT}")

        # Send the formatted message to the server
        client_socket.send(message.encode("utf-8"))
        print(f"[INFO] Sent message: {message}")

        # Wait for the server's response (up to 1024 bytes)
        response = client_socket.recv(1024).decode("utf-8")
        if not response:
            print("[ERROR] No response received from the server.")
            return

        # Expected response format: "Server of John Q. Smith;[server_number]"
        parts = response.strip().split(";")
        if len(parts) != 2:
            print("[ERROR] Server response format is incorrect.")
            return

        # Extract the server's name and number
        server_name = parts[0]
        try:
            server_number = int(parts[1])
        except ValueError:
            print("[ERROR] The server's number is not a valid integer.")
            return

        # Calculate the sum of the client's number and the server's number
        total_sum = client_number + server_number

        # Display the server's information and the sum
        print(f"[INFO] Received response from {server_name} with number {server_number}.")
        print(f"[INFO] Calculation: {client_number} (client) + {server_number} (server) = {total_sum}")

    except Exception as e:
        print(f"[ERROR] Exception during communication: {e}")
    finally:
        # Always close the socket after the communication is done
        client_socket.close()
        print("[INFO] Client socket closed.")

if __name__ == "__main__":
    start_client()
