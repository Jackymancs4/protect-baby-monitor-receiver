import socket
import pyaudio
import wave
import time

def save_socket_stream(host, port, base_output_file):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((host, port))
            print(f"Connected to {host}:{port}")
            
            file_count = 0
            start_time = time.time()

            while True:
                # Create a new WAV file every minute
                output_file = f"{base_output_file}_{file_count}.wav"

                with wave.open(output_file, 'wb') as wf:
                    # Set the parameters for the WAV file
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(11025)

                    while True:
                        # Receive data from the socket
                        data = s.recv(1024)
                        if not data:
                            break

                        # Write the received data to the WAV file
                        wf.writeframes(data)
                        current_time = time.time()

                        # Check if a minute has passed
                        if current_time - start_time >= 60:
                            start_time = current_time
                            file_count += 1
                            break

                        print(f"Received and wrote {len(data)} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    # Define the audio stream parameters
    frequency = 11025
    channels = 1
    audio_format = pyaudio.paInt16
    buffer_size = 1024  # Adjust as necessary, similar to bufferSize*2

    host = "192.168.2.35"
    port = 40468  # your_server_port
    output_file = "output_stream"
    
    save_socket_stream(host, port, output_file)