#!/usr/bin/python3

def go(a):
    if a <= 1:
        return 1
    else:
        return go(a-1) + go(a-2)

print(str(go(9)))
