import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 5000))

    print("Server is ready to receive messages...\n\n")

    expected_sequence_number = 0

    while True:
        data, addr = server_socket.recvfrom(1024)
        frame = data.decode()
        sequence_number, message = frame.split("|")
        if message == 'exit':
            break

        # Simulate processing the message (sleep for 1 second)
        import time
        time.sleep(1)

        # Simulate packet loss (50% chance of dropping the frame)
        import random
        rand = random.random()
        # print(f"\n{rand}")

        if rand <= 0.09:
            print(f"Frame {sequence_number} lost!")
            continue

        if int(sequence_number) == expected_sequence_number:
            print(f"Received Frame {sequence_number}: {message}")

            if rand <= 0.18:
                ack = str(expected_sequence_number)
                server_socket.sendto(ack.encode(), addr)
                print(f"Sending Delayed ACK!")

            ack = str((expected_sequence_number + 1) % 2)
            if rand <= 0.18:
                time.sleep(0.5)

            if rand <= 0.91:
                server_socket.sendto(ack.encode(), addr)

            print(f"ACK {ack} Sent!")
            if rand > 0.91:
                print(f"ACK {ack} Lost!")
            print("\n")
                            
            expected_sequence_number = (expected_sequence_number + 1) % 2
        
        else:
            # Sending duplicate ACK for the last correctly received frame
            print(f"Duplicate Frame {sequence_number} Discarded! Resending ACK {expected_sequence_number}\n")
            ack = str(expected_sequence_number)
            server_socket.sendto(ack.encode(), addr)

if __name__ == "__main__":
    server()