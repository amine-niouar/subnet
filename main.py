#!/usr/bin/python

import random


def add_range(masks,ranges):
    mask = ""
    for oct in masks:
        mask += str(oct) + "."
    mask = mask.rstrip(".")
    ranges.append(mask)


def fill_range(ranges,masks):
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
        i += 1
    add_range(masks,ranges)

def get_rand_range(ranges):
    lenRanges = len(ranges)
    index = random.randint(0,lenRanges)
    range = ranges[index]
    return (range)

def get_rand_oct_mask(octet_mask):
    #128 (0,127) (129,255)
    ranges = []
    range_size = 256 - octet_mask
    rounds = int(256 / range_size)
    start = 0
    end   = 0
    i = 0
    while (i < rounds):
        if i > 0:
            start = end + 1
        range = []
        end += range_size
        if(i > 0):
            range.append(start-1)
        else:
            range.append(start)
        range.append(end-1)
        ranges.append(range)
        i += 1
    print (ranges)
    return(str(range_size) + " " + str(rounds))


def get_rand_ip(range):
    octets_mask = range.split(".")
    ip = ""
    for octet in  octets_mask:
        if octet == "255":
            octet_ip = random.randint(1,255)
            ip += str(octet_ip) + "."
        else:
            ip += str(0) + "."
    ip.rstrip(".")
    return (ip)

def main():
    ranges = []
    bit = numberOctet = 0
    masks = [0,0,0,0]
    fill_range(ranges,masks)
    range = get_rand_range(ranges)
    ip = get_rand_ip(range)
    example = get_rand_oct_mask(192)
    print(example)
    #print(range + " " + ip)

    

    #for range in ranges:
        #print (range)

main()