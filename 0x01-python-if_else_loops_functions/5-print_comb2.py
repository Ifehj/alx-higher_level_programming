#!/usr/bin/python3

for ch in range(0, 100):
    if ch == 99:
        print("{}".format(ch), end='\n')
    else:
        print("{0:02d}".format(ch), end=', ')
