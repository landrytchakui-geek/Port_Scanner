from scapy.all import *
import ipaddress

# List of ports to scan
ports = [21, 22, 25, 53, 80, 443, 445, 8080, 8443,2222]

# SYN scan function
def SynScan(host):

    print(f"\nScanning {host}...\n")

    ans, unans = sr(
        IP(dst=host) /
        TCP(sport=RandShort(), dport=ports, flags="S"),
        timeout=2,
        verbose=0
    )

    open_ports = []

    for sent, received in ans:

        # Check if the response contains a TCP layer
        if received.haslayer(TCP):

            # SYN-ACK means the port is open
            if received[TCP].flags == 0x12:
                open_ports.append(sent[TCP].dport)

                # Send RST packet to close the connection properly
                send(
                    IP(dst=host) /
                    TCP(dport=sent[TCP].dport,
                        flags="R"),
                    verbose=0
                )

    if open_ports:
        print("Open TCP ports:")
        for port in open_ports:
            print(f"Port {port} OPEN")
    else:
        print("No open TCP ports detected")


# DNS scan function using UDP
def DNS_Scan(host):

    ans, unans = sr(
        IP(dst=host) /
        UDP(dport=53) /
        DNS(rd=1, qd=DNSQR(qname="google.com")),
        timeout=2,
        verbose=0
    )

    if len(ans) > 0:
        print("\nDNS server detected on port 53")
    else:
        print("\nNo DNS response")


# Main program
host = input("Enter target IP: ")

try:
    ipaddress.ip_address(host)

except ValueError:
    print("Invalid IP format")
    exit()


SynScan(host)
DNS_Scan(host)