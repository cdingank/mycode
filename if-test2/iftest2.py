#!/usr/bin/env python3
ipchk = input('what is the IP:')

if ipchk == '192.168.70.1':
   print ('Gateway IP')
elif ipchk:
   print('Looks like the IP address was set: ' + ipchk)
else:
   print('no input')

