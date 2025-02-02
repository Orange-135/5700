# Programming Assignment 1: Socket Programming

## Overview

This project implements a client-server application using Python sockets. The server handles multiple clients concurrently using Python's `threading` module. The project demonstrates the concepts of TCP communication, concurrency, and input validation.

---

## Concurrent Server Configuration

### How It Works

The server is designed to handle multiple clients simultaneously by creating a new thread for each incoming client connection. Here's how the concurrency is achieved:

1. **Threading Module**:  
   The Python `threading` module is used to spawn a new thread for each client connection. The main server process listens for incoming connections and delegates each client request to a separate thread.

2. **Thread Lifecycle**:  
   - Each thread runs the `handle_client` function, which processes the request from an individual client.
   - The threads are marked as "daemon threads," which means they automatically terminate when the main server process exits.

3. **Concurrency Implementation**:  
   - The server uses a `while True` loop to continuously accept new client connections.
   - For each connection, the following code creates and starts a new thread:
     ```python
     client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
     client_thread.daemon = True
     client_thread.start()
     ```

4. **Thread Safety**:  
   - Since each thread operates independently, there are no shared resources in this implementation that require thread synchronization.
   - Python's Global Interpreter Lock (GIL) ensures thread safety for basic socket operations.

---

### Libraries Used

1. **`socket` Module**:  
   - The `socket` module is a standard Python library used to create and manage the TCP connection.
   - Functions such as `socket.socket()`, `bind()`, `listen()`, and `accept()` are used to handle server operations.

2. **`threading` Module**:  
   - This standard library is used to implement concurrency in the server.
   - The `Thread` class is used to create and manage threads for each client connection.

---

## Features

1. **Concurrent Server**:
   - Handles multiple clients at the same time without blocking other connections.
   - Each client request is processed in a separate thread.

2. **Input Validation**:
   - The server validates client input to ensure it is within the allowed range (1-100).
   - If an out-of-range number is received, the server shuts down gracefully.

3. **TCP Communication**:
   - Both client and server use TCP sockets for reliable communication.
