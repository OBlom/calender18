#!/usr/bin/env python3

""" Simple script to solve https://adventofcode.com/2018
    
"""

from __future__ import print_function
import re
import os
import sys
import argparse

class Day(object):
    def __init__(self,day):
        with open('input_day{}.txt'.format(day),'r') as f:
            self.data = f.readlines()

class Day1(Day):
    def __init__(self):
        Day.__init__(self,1)

    def solve1(self):
        sum=0
        for line in self.data:
            sum = sum + int(line)
        print("Day1 challenge1: {}".format(sum))

    def solve2(self):
        freq_set = set([0])
        freq = 0
        found=False
        while not found:
            for line in self.data:
                freq = freq + int(line)
                if freq in freq_set:
                    found = True
                    break
                else:
                    print(freq)
                    freq_set.add(freq)
        print("Day1 challenge2: {}".format(freq)) 
def main(args):
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('day', metavar='DAY', type=int, choices=range(1,8), help="day to solve")
    parser.add_argument('challenge', metavar='CHALLENGE', type=int, choices=range(1,3), help="challenge to solve")
    args = parser.parse_args(args)
    
    day = getattr(sys.modules[__name__],"Day{}".format(args.day))()
    if args.challenge == 1:
        day.solve1()
    else:
        day.solve2()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
        
