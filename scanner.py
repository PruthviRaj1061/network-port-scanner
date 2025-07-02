import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
    except:
        print(f"[-] Port {port} is CLOSED")
    finally:
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [20, 21, 22, 23, 25, 53, 80, 443]
    
    print(f"\n[~] Scanning {target}...\n")
    for port in ports:
        scan_port(target, port)
    print("\n[~] Scan complete.")