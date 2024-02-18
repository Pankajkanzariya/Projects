#!/usr/bin/python3
import socket
import sys
import threading

usage = "python3 portscan.py Target_IP Port_Start Port_End"

print("-" * 70)
print("Port Scanner")
print("-" * 70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit(1)

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution error")
    sys.exit(1)

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("target scanning ", target)

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            conn = s.connect_ex((target, port))
            if conn == 0:
                service = socket.getservbyport(port)
                print("Port {} is open. Service: {}".format(port, service))
    except Exception as e:
        print("Error:", e)

threads = []
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
