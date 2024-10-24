import nmap
import socket
from concurrent.futures import ThreadPoolExecutor
import ipaddress


# Function to scan a specific port and detect services and operating system
def scan_port(ip, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Set timeout for the connection
    result = sock.connect_ex((ip, port))  # Attempt to connect to the IP and port
    if result == 0:
        nm = nmap.PortScanner()
        nm.scan(ip, str(port))
        if 'tcp' in nm[ip] and port in nm[ip]['tcp']:
            service = nm[ip]['tcp'][port]['name']
        else:
            service = 'unknown'
        results[ip].append({'port': port, 'service': service})
        print(f"IP: {ip} Port {port} is open | Service: {service}")
        # If port 80 or 443 is open (commonly used for web servers), attempt OS detection
        if port == 80 or port == 443:
            os_detection = nm.scan(ip, arguments='-O')
            if 'osclass' in os_detection['scan'][ip]:
                os_class = os_detection['scan'][ip]['osclass'][0]
                os_family = os_class['osfamily']
                os_vendor = os_class['vendor']
                os_gen = os_class['osgen']
                results[ip][-1]['os'] = {'family': os_family, 'vendor': os_vendor, 'gen': os_gen}
                print(f"OS Family: {os_family}, Vendor: {os_vendor}, OS Generation: {os_gen}")
            else:
                results[ip][-1]['os'] = 'Not available'
                print("OS Detection not available")
    sock.close()


# Function to scan an IP range
def scan_ip_range(ip_range):
    results = {}
    # Use a thread pool to scan multiple ports concurrently
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in ipaddress.IPv4Network(ip_range):
            ip = str(ip)
            results[ip] = []
            # Scan ports 1-1023
            for port in range(1, 1024):
                executor.submit(scan_port, ip, port, results)
    return results


# Main function
def main():
    print("""
    ████████╗██████╗ ██╗███████╗███████╗██╗██╗     ███████╗
    ╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝██║██║     ██╔════╝
       ██║   ██████╔╝██║███████╗█████╗  ██║██║     █████╗  
       ██║   ██╔══██╗██║╚════██║██╔══╝  ██║██║     ██╔══╝  
       ██║   ██║  ██║██║███████║███████╗██║███████╗███████╗
       ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝╚══════╝

    Welcome to TRISEILE Scan Tool!
    Developed by Theofanis Kantzaris
    Version 1.0
    """)

    target_ip_range = input("Enter the IP address or range to scan: ")  # Prompt the user for an IP address or subnet
    results = scan_ip_range(target_ip_range)

    print("Scan complete.")


# Run the main function
if __name__ == "__main__":
    main()
