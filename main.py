import network


def init(): 
    print("Welcome to Network Set Up")
    print("To quit, type 0")
    while True:
        ip = input("Insert ip number: ")
        if ip == '0':
            print("GOOD BYE")
            break
        if not network.valid_ip(ip):
            continue

        mask_subnet = input("insert subnet mask: ")   
        mask_bin, mask_decimal = network.mask_subnet(mask_subnet)
        ip_bin = network.get_ip_bin(ip)
        network_ip = network.get_network_ip(ip_bin, mask_bin)
        broadcast_ip = network.get_broadcast_ip(ip_bin, mask_bin)
        n_hosts = network.get_number_hosts(mask_bin)
        first_ip = network.get_first_ip(network_ip)
        last_ip = network.get_last_ip(broadcast_ip)

        print("\n****NETWORK INFORMATION****\n")
        print(f"IP: {ip}")
        print(f"Subnet Mask: {mask_decimal}")
        print(f"Network IP: {network_ip}")
        print(f"Broadcast IP: {broadcast_ip}")
        print(f"First IP: {first_ip}")
        print(f"Last IP: {last_ip}")
        print(f"Number of hosts: {n_hosts}")

        decision = input("QUIT? [s] or [n] ")
        if decision.lower() == 's':
            break




if __name__ == "__main__":
    init()