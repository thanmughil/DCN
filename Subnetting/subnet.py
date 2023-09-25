def inp():
    no_of_users = int(input("Enter No. of Users: "))
    hostList = []
    for i in range(no_of_users):
        hostList.append((i+1,int(input(f"Enter No. of Hosts for User {i}: "))))
    hostList.sort(reverse=True,key=lambda x : x[1])
    IP_Addr = input("Enter IP with Subnet Mask (Ex : 192.1.0.0/25) : ")
    ip,subnet_mask = IP_Addr.split('/')

    return (hostList,ip,subnet_mask)

def find_fixed_ip(ip,subnet_mask):
    bin_ip = ''.join([str(bin(int(i)))[2:].zfill(8) for i in list(ip.split('.'))])
    fixed_ip = bin_ip[:subnet_mask]
    start_ip = bin_ip[subnet_mask:]
    return (fixed_ip,start_ip)

def subnet(hostList,subnet_mask,fixed_ip,start_ip):
    curr_ip = start_ip
    for i,j in hostList:
        bit_len_j = j.bit_length()
        print(f"\nUser {i} with {j} hosts : ")
        full_start_ip = '.'.join([str(int((fixed_ip+curr_ip)[k:k+8],2)) for k in range(0,25,8)])
        print(f"\tStart IP : {full_start_ip}/{32-bit_len_j}")
        curr_ip = str(bin(int(curr_ip,2)+int(2**(bit_len_j))))[2:]
        full_end_ip = '.'.join([str(int((fixed_ip+str(bin(int(curr_ip,2)-1))[2:].zfill(subnet_mask))[k:k+8],2)) for k in range(0,25,8)])
        print(f"\tEnd IP : {full_end_ip}/{32-bit_len_j}")
        print(f"\tAddress Depletion : {2**bit_len_j-j}")

hl,ip,sm = inp()
ma = 32-int(sm)
print(f"\nTotal Available Host Addresses : {2**ma}\n")
subnet(hl,ma,*find_fixed_ip(ip,int(sm)))
