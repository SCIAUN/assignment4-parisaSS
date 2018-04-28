import nmap

def port_scanner(ports):
    nm = nmap.PortScanner()
    nm.scan(ports, '21-1000')
    for host_names in nm.all_hosts():
        ports = nm[host_names].get('tcp')
        write_into_file(ports)

    return ports


def write_into_file(contents):
    f = open('result', 'w')
    ff = str(contents)
    f.write(ff)

    pass


def main():
    hosts = [
        'w3schools.com',
        'hadipoor.ir'
        'google.com',
        'hibibhoora.com',
        'fileniko.com',
        'tvniko.com'
    ]

    for host_name in hosts:
        port_scanner(host_name)

main()
