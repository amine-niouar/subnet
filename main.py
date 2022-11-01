#!/usr/bin/python


def add_range(masks,ranges):
    mask = ""
    for oct in masks:
        mask += str(oct) + "."
    mask = mask.rstrip(".")
    ranges.append(mask)

def main():
    ranges = []
    bit = numberOctet = 0
    masks = [0,0,0,0]

    i = 0
    while i < 4:
        if i > 0:
           add_range(masks,ranges)
        x = 7
        oct = 0
        while x >= 1:
            mask = ""
            bit = 2**x
            masks[i] += bit
            add_range(masks,ranges)
            x -= 1
        masks[i] += 1
        #add_range(masks,ranges)
        i += 1
    add_range(masks,ranges)

    for range in ranges:
        print (range)

main()