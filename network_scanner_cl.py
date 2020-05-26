#!/usr/bin/env python

import scapy.all as scapy
import optparse


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list= []
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\t\t\tMAC Address\n-------------------------------------------------------------------------")
    for result in results_list:
        print(result["IP"] + "\t\t\t\t" + result["MAC"] + "\t\t")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--ip", "--IP", dest="IP", help="IP Address")
    (options, arguments) = parser.parse_args()
    if not options.IP:
        parser.error("Please specify an IP address or range")
    return options

options = get_arguments()
scan_result = scan(options.IP)
print_result(scan_result)
