# This program is a simple IPv4 subnet calculator
# It helps you find network details from an IP address and CIDR

import ipaddress   # Python library that understands IP addresses


def calculate_subnet(ip_cidr):
    # Try to create a network object from the user input
    # strict=False allows normal IPs like 192.168.1.10/24
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
    except ValueError:
        # If the input format is wrong, show an error and stop
        print("Invalid input.")
        print("Example: 192.168.1.10/24")
        return

    # Basic subnet information
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    subnet_mask = network.netmask
    prefix_length = network.prefixlen
    total_addresses = network.num_addresses

    # Calculate usable hosts
    if prefix_length == 32:
        # /32 means only one device
        usable_hosts = 1
        first_usable = network_address
        last_usable = network_address
        note = "/32 is a single host."
    elif prefix_length == 31:
        # /31 is usually used for point-to-point links
        usable_hosts = 2
        first_usable = network_address
        last_usable = broadcast_address
        note = "/31 is used for point-to-point links."
    else:
        # Normal subnets
        usable_hosts = total_addresses - 2
        first_usable = network_address + 1
        last_usable = broadcast_address - 1
        note = ""

    # Print the results
    print("\nIPv4 Subnet Calculator")
    print("----------------------")
    print("Input IP/CIDR:      ", ip_cidr)
    print("Network Address:    ", network_address)
    print("Broadcast Address:  ", broadcast_address)
    print("Subnet Mask:        ", subnet_mask)
    print("CIDR Prefix:        /" + str(prefix_length))
    print("Total Addresses:    ", total_addresses)
    print("Usable Hosts:       ", usable_hosts)
    print("Usable Host Range:  ", first_usable, "-", last_usable)

    if note:
        print("Note:               ", note)

    print()


def main():
    # Ask the user to enter an IP address with CIDR
    print("Simple IPv4 Subnet Calculator")
    print("Enter IP with CIDR notation")
    print("Example: 192.168.1.10/24\n")

    user_input = input("IP/CIDR: ")
    calculate_subnet(user_input)


# This line makes sure the program runs only when this file is executed
if __name__ == "__main__":
    main()
