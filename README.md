# TRISEILE Scan Tool
Welcome to the TRISEILE Scan Tool, a powerful multi-threaded network scanning utility for scanning ports, detecting services, and identifying operating systems on a given IP address or IP range.

Features
- Port Scanning: Scans ports in the range of 1-1023 for open services.
- Service Detection: Identifies the service running on open ports.
- OS Detection: Attempts to detect the operating system running on machines with open web services (port 80 or 443).
- Multi-threaded Scanning: Leverages Python’s ThreadPoolExecutor to scan multiple ports and IPs concurrently for faster results.

# Installation
To use this tool, you need Python 3.x and the following dependencies:

nmap: The Python nmap library for port and OS detection.
socket: The built-in Python library for network communication.
ipaddress: The built-in Python library to handle IP ranges.
concurrent.futures: For multi-threading functionality.
Install the required Python modules using pip:

bash
Copy code
pip install python-nmap
Ensure you have nmap installed on your system. On Linux, install with:

bash
Copy code
sudo apt-get install nmap
Usage
To run the TRISEILE Scan Tool, follow these steps:

Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/TRISEILE-Scan-Tool.git
cd TRISEILE-Scan-Tool
Run the script:

bash
Copy code
python triseile_scan.py
Enter the IP address or range you want to scan when prompted.

# Example
bash
Copy code
Enter the IP address or range to scan: 192.168.1.0/24
The tool will start scanning all IPs in the range 192.168.1.0 to 192.168.1.255 for open ports, services, and if applicable, detect the operating system.

# Output
The tool will display open ports, detected services, and OS details for web servers if available. Example output:

yaml
Copy code
IP: 192.168.1.5 Port 80 is open | Service: http
OS Family: Linux, Vendor: Debian, OS Generation: 10

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing
Feel free to submit issues or pull requests for improvements.

# Author
Developed by Theofanis Kantzaris
For any inquiries, contact: faniskantz@gmail.com
