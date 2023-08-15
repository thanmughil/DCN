import socket

def client():
    random_items = ["Apple","Banana","Laptop","Sunglasses","Chair","Book","Umbrella","Soccer ball","Coffee mug","Headphones",
                    "Backpack","Pillow","Guitar","Water bottle","Notebook","T-shirt","Camera","Watch","Keychain","Chocolate"]
    import msvcrt
    i = 0

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 5000)

    frame_number = 0

    while True:
        message = random_items[i]

        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key == 'q':
                message = 'exit'

        # Create the frame with sequence number and message
        frame = f"{frame_number}|{message}"

        # Sending the frame to the server
        client_socket.sendto(frame.encode(), server_address)
        if message.lower() == "exit":
            break
        print(f"Frame {frame_number} Sent: {message}")

        # Waiting for ACK from the server
        ack_received = False
        client_socket.settimeout(2)  # Set a timeout for ACK reception
        while not ack_received:
            try:                
                data, _ = client_socket.recvfrom(1024)
                ack = data.decode()
                if int(ack) == (frame_number + 1) % 2:
                    print(f"ACK {ack} received for Frame {frame_number}\n")
                    ack_received = True
                else:
                    print(f"ACK {ack} received for Frame {frame_number}.\nDelayed Acknowledgement ACK {ack} discarded!")
                    continue

            except socket.timeout:
                print("Timeout occurred. Resending frame...")
                client_socket.sendto(frame.encode(), server_address)

        frame_number = (frame_number + 1) % 2
        i = (i+1)%20

    client_socket.close()

if __name__ == "__main__":
    client()