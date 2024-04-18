#!/usr/bin/env python3

import binascii
import socket
import sys

if len(sys.argv) < 3:
    print ("Usage: wakeonlan.py <ADR> <MAC>     (example: 192.168.1.255 FF:FF:FF:FF:FF:FF)")
    sys.exit(1)

mac = sys.argv[2]
_data = ''.join(['FF' * 6, mac.replace(':', '') * 16])

data = binascii.unhexlify(_data)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(data, (sys.argv[1], 9))