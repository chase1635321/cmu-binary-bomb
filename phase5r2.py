#!/usr/bin/python3

import r2pipe

r = r2pipe.open("bomb")

r.cmd("aa; ood phase5.txt")
r.cmd("dcu 0x8048d43; dr eax = 6")

r.cmd("db 0x8048d66")
values = {}

for c in "abcdefghijklmnopqrstuvwxyz":
    r.cmd("dc")
    eax = r.cmd("dr eax")
    string = r.cmd("? " + eax + "~string")
    r.cmd("dr eip = 0x8048d57")
    print(" > " + c + " -> " + string.strip()[9:10])
    values[string.strip()[9:10]] = c


print("\ngiants translates to:")
for c in "giants":
    print(values[c], end='')

print("")
