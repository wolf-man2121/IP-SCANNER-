import socket
import sys
from datetime import datetime

# Help message
help_msg = """
Mini Port & Service Scanner - Usage:

python scanner.py [target]

Options:
  -h, --help    Show this help message and exit

Features:
  - Scans a target IP/domain for open ports
  - Identifies common services (HTTP, FTP, SSH, etc.)
  - Mini version of Nmap
"""

# Check arguments
if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
    print(help_msg)
    sys.exit()

target = sys.argv[1]

# Define ports to scan
start_port = 1
end_port = 1024

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
open_ports = []

start_time = datetime.now()

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"Port {port} is open - Service: {service}")
        open_ports.append(port)
    s.close()

end_time = datetime.now()

if open_ports:
    print(f"\nOpen ports on {target}: {open_ports}")
else:
    print("\nNo open ports found.")

print(f"\nScan completed in: {end_time - start_time}")

