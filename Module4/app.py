from scapy.all import IP, TCP, sniff

# reponse = sniff(timeout=10)
# print(response.show())
# value = IP(dst = "google.com")/TCP(dport=[22,3000,80])
# print(value.show())

def save_packet(packet):
    with open("raw.txt", "a") as f:  # Open the file in append mode
        f.write(packet.summary() + "\n")  # Write packet summary
        f.write(str(packet.show(dump=True)) + "\n\n")  # Write detailed packet info

# Sniff 10 packets and process each one using save_packet
sniff(timeout=10, prn=save_packet)

