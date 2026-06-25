import socket

target = input("Enter target IP or hostname")

start_port = int(input("Enter starting port number"))

end_port = int(input("Enter ending port number"))

print(f"Scanning {target} from port {start_port} to {end_port}")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port} is open")
        
    sock.close()
