import socket

def save_socket_stream(host, port, output_file):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((host, port))
            print(f"Connected to {host}:{port}")
            
            # Open the output file in write-binary mode
            with open(output_file, 'wb') as f:
                print(f"Saving stream to {output_file}")
                while True:
                    # Receive data from the socket
                    data = s.recv(1024)
                    if not data:
                        break
                    # Write the received data to the file
                    f.write(data)
                    print(f"Received and wrote {len(data)} bytes")
                    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = "192.168.2.35"
    port = 41560  # your_server_port
    output_file = "output_stream.bin"
    
    save_socket_stream(host, port, output_file)