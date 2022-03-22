
from typing import Type


def get_ip_bin(ip):
    '''convert ip from decimal to binary'''
    ip_list_bin = [bin(int(i)) for i in ip.split('.')]
    ip_list_bin = [block_ip[2:len(block_ip)].rjust(8, '0') for block_ip in ip_list_bin]

    return ''.join(ip_list_bin)


def mask_subnet(mask):
    '''return subnet mask in decimal and binary'''
    try:
        mask = int(mask)
    except TypeError as e:
        print("Insert a valid mask (just a number)")
        return
    number_mask = ('1'*mask).ljust(32, '0')
    mask_list_bin = [number_mask[i-7:i+1] for i in range(7, len(number_mask), 8)]
    mask_list_str = [str(int(number, 2)) for number in mask_list_bin]

    return '.'.join(mask_list_bin), '.'.join(mask_list_str)

def get_number_hosts(number_mask):
    '''return numbers of hosts possible on network'''
    b = number_mask.count('0')
    number_hosts = 2**b - 2 

    return number_hosts

def get_network_ip(ip, mask):
    '''return network ip in binary and decimal'''
    number_0 = mask.count('0')
    ip = ip.strip('.')
    ip =  list(ip)
    ip[-number_0:len(ip)] = list('0'*number_0)

    for i in range(8,len(ip),9):
        ip.insert(i, '.')

    network_ip_bin = ''.join(ip)
    network_ip_decimal = [str(int(block_ip, 2)) for block_ip in network_ip_bin.split('.')]


    return '.'.join(network_ip_decimal)
    

def get_broadcast_ip(ip, mask):
    '''return broadcast ip in binary and decimal'''
    number_0 = mask.count('0')
    ip = ip.strip('.')
    ip =  list(ip)
    ip[-number_0:len(ip)] = list('1'*number_0)

    for i in range(8,len(ip),9):
        ip.insert(i, '.')

    broadcast_ip_bin = ''.join(ip)
    broadcast_ip_decimal = [str(int(block_ip, 2)) for block_ip in broadcast_ip_bin.split('.')]


    return  '.'.join(broadcast_ip_decimal)

def valid_ip(ip):

    if ip.count('.') != 3:
        print("Insert a valid ip number: 1111.1111.1111.1111")
        return False
    try:
        ip = ip.split('.')
        for block_ip in ip:
            block_ip_int = int(block_ip)
            if block_ip_int > 255:
                print("Insert a valid ip number: 1111.1111.1111.1111")
                return False
    except TypeError as e:
        print("Insert a valid ip number: 1111.1111.1111.1111")
        return False

    print('IP number ok')
    return True

def get_first_ip(net_ip):
    net_ip = net_ip.split('.')
    net_ip[3] = str(int(net_ip[3]) + 1)
    return '.'.join(net_ip)

def get_last_ip(broad_ip):
    broad_ip = broad_ip.split('.')
    broad_ip[3] = str(int(broad_ip[3]) - 1)
    return '.'.join(broad_ip)

    