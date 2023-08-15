from sender import xordiv,gOfx
import socket

r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r.bind(('localhost',5000))
msg,addr = r.recvfrom(1024)

dividend = msg.decode()
print(f"Received Message : {dividend}\n")
red_bits = xordiv(dividend,gOfx)
print(f"Calculated Redundant Bits : {red_bits}")

if set(red_bits) == {'0'}:
    print("No Error in Transmission!")
    r.sendto("No Error in Transmission!".encode(),addr)

else:
    print("Error in Transmission!")
    r.sendto("Error in Transmission!".encode(),addr)