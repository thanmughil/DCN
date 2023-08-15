import socket

gOfx = '1010'

def xor(imm_val,key):

    div_len=len(key)

    if imm_val[0] == '0':
        imm_val = str(bin(int(imm_val,2) ^ 0))[2:].zfill(div_len)[1:]
    else:
        imm_val = str(bin(int(imm_val,2) ^ int(key,2)))[2:].zfill(div_len)[1:]
    
    return imm_val

def xordiv(div,key):

    div_len = len(gOfx)

    imm_val = div[:div_len]
    for i in range(div_len,len(div)):
        imm_val = xor(imm_val,key) + div[i]
    imm_val = xor(imm_val,key)

    return imm_val

if __name__ == '__main__':

    mOfx = input("Enter Message : ")
    dividend = mOfx + '0'*len(gOfx)
    red_bits = xordiv(dividend,gOfx)

    cOfx = mOfx + red_bits
    print(f"\nRedundant Bits : {red_bits}")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('localhost',5000))

    err = input("\nIntroduce Error? (y/n): ")
    print(f"Sent Message : {cOfx}\n")

    if err.lower() == 'y':
        cOfx = ('1' if cOfx[0] == '0' else '0') + cOfx[1:]

    s.send(cOfx.encode())

    msg,addr = s.recvfrom(1024)
    print("Received :",msg.decode())