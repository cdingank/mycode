#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
print(proto[1])

proto.extend('dhcp')

print (proto)
protoa.append ('dhcp')


print (protoa)

proto2 = [ 22, 80, 443, 53 ]
proto.extend (proto2)
print (proto)

protoa.append (proto2)
print (protoa)

print (protoa[4][0])
print (proto[4])        

