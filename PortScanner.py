'''
    Python file used to learn Python Network Hacking
    Encoding = 'UTB-8'
    Data = 2017.8.27
'''

# use library "optparse" to parse command line arguments

import optparse
import socket

parser = optparse.OptionParser('Usage %prog -H ' + \
                               '<target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', \
                  help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', \
                  help='specify target port')

(options, args) = parser.parse_args()

print("tgtHost is %s" % options.tgtHost)
print("tgtPort is %d" % options.tgtPort)

tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost is None) | (tgtPort is None):
    print(parser.usage)
    exit(0)

print('Test 1 \n')

# use library "socket" to scan these posts


def connScan(tgtHost, tgtPort):
    try:
        connSkt = (socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect = ((tgtHost, tgtPort))
        print('[+]%d/tcp open' % tgtPort)
        connSkt.close()
    except:
        print('[-]%d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):

    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan results for : ' + tgtName[0])
    except:
        print('\n[+] Scanresults for :' + tgtIP)

    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


connScan('119.75.216.20', 20)
portScan('119.75.216.20', ['10', '20', '30'])
