import socket


target = input("Enter target IP or domain: ")


try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()

print(f"\nScanning target: {target_ip}")
print("Scanning ports...\n")


for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    
    s.close()

print("\nScan complete.")