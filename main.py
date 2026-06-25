import socket

target = input("Enter target IP or hostname:\n").strip()

start_port = int(input("Enter starting port number:\n"))

end_port = int(input("Enter ending port number:\n"))

if start_port > end_port:
    raise ValueError("Starting port must be less than or equal to ending port")

print(f"Scanning {target} from port {start_port} to {end_port}")

open_ports = []

for port in range(start_port, end_port + 1):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is open")
    except socket.gaierror:
        print(f"Could not resolve target: {target}")
        break
    except PermissionError:
        print("Permission denied while creating a socket. Try running from a normal terminal.")
        break
    finally:
        if sock:
            sock.close()

if not open_ports:
    print("No open ports found in that range.")

print(f"Successfully scanned target {target}")
