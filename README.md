-SCANNER-

A simple Python IP & Port Scanner that finds open ports and their services.

----------------------------------------
FEATURES
----------------------------------------
- Scan ports from 1 to 1024 (can be adjusted in the code)
- Identify open ports and their common services
- Show a summary of all open ports found
- Display total scan duration
- No external libraries required

----------------------------------------
INSTALLATION
----------------------------------------
git clone 

----------------------------------------
USING
----------------------------------------
1. Run the scanner:
   python port_scanner.py

2. Enter the target IP when prompted:
   Enter target IP: 192.168.1.5

3. The scanner will check ports from 1 to 1024 by default

4. The output will display:
   - Open ports
   - Common service names
   - Total scan duration

----------------------------------------
OPTIONAL
----------------------------------------
- To change the port range, edit the script:
   start_port = 1
   end_port = 1024

