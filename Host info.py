#!/user/bin/env python
import urllib3.request
import socket as sok
from datetime import datetime
import sys
from pyfiglet import figlet_format as form
from termcolor import cprint

# All modules imported

restart = 'y'
exit = ['n', 'N', 'no', 'NO', 'nO', 'No']


def get_host():
    url = str(
        input("Enter your site url to obtain host name (host name is required to carry out all sorts of functions) : "))
    host = urllib3.get_host(url)
    format_host = list(host)
    format_host.pop(0)
    format_host.pop(1)
    host = tuple(format_host)
    cprint(f"Host name = {host}", 'green')


def banner():
    cprint(form('I N FO    F i n d e r    B Y    IP   OR    DOMAIN      NAME'), 'red')
    cprint('\t\t\t\tThis host info finder is created by Real Coder\n', 'green')


def main():
    restart = 'y'
    while restart not in exit:
        option = int(
            input("\nSelect 1 for finding ip or 2 for finding hostname by ip or select 3 for getting address info or 4 to exit[1/2/3/4] : "))

        if option == 1:
            url = str(input("Enter the host name : "))
            host_name = sok.gethostbyname(url)
            cprint(host_name, 'green')
            cprint(datetime.now(), 'green')
            cprint(type(host_name), 'green')
            restart = input("Want to go back to main menu [y/n] :")
            if restart not in exit:
                main()

        elif option == 2:
            url = str(input("Enter the ip address : "))
            host_ip = sok.gethostbyaddr(url)
            cprint(host_ip, 'blue')
            cprint(datetime.now, 'blue')
            cprint(type(host_ip), 'blue')
            restart = input("Want to go back to main menu [y/n] :")
            if restart not in exit:
                main()
        elif option == 3:
            url = str(input("Enter either ip or hostname : "))
            addr_info = sok.getaddrinfo(url, 443)
            print('\n')
            cprint(addr_info,'red')
            cprint(datetime.now, 'red')
            cprint(type(addr_info), 'red')
            restart = input("Want to go back to main menu [y/n] :")
            if restart not in exit:
                main()
        elif option == 4:
            cprint("\nPlease Wait Exiting.....",'red')
            sys.exit()

"""Since it's not a big code it can only let you get domain ip address and hostname and 
even their socket info.
Please follow me on github for Super amazing python scripts
My next projects is Gmail creation Script"""

if __name__ == '__main__':
    banner()
    get_host()
    main()
