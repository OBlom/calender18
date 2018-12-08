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
#                    print(freq)
                    freq_set.add(freq)
        print("Day1 challenge2: {}".format(freq)) 

class Day2(Day):
    def __init__(self):
        Day.__init__(self,2)

    def solve1(self):
        sum3letters=0
        sum2letters=0
        for line in self.data:
            letters={}
            threeLetters=0
            twoLetters=0
            for c in line:
                letters.setdefault(c,0)
                letters[c]=letters[c]+1
            for letter,val in letters.items():
                if val == 3:
                    threeLetters=1
                if val == 2:
                    twoLetters=1
            sum3letters = sum3letters + threeLetters
            sum2letters = sum2letters + twoLetters

        print("Day2 challenge1: {}".format(sum2letters*sum3letters))

    def solve2(self):
        match=None
        for i in range(0,len( self.data)-1):      
            for j in range(i+1,len(self.data)):
                diff=0
                for a,b in zip(self.data[i],self.data[j]):
                    if a != b:
                        diff = diff+1
                if diff == 1:
                    match=''
                    for a,b in zip(self.data[i],self.data[j]):
                        if a == b:
                            match = match + a
                    break
                if match is not None:
                    break

        print("Day2 challenge2: {}".format(match if match else 'Oops'))
    
class Day3(Day):
    def __init__(self):
        Day.__init__(self,3)

    def solve1(self):
        claim_re=re.compile("^#(?P<id>[0-9]+)\s*@\s*(?P<x>[0-9]+),(?P<y>[0-9]+):\s*(?P<xlen>[0-9]+)x(?P<ylen>[0-9]+)")
        fabric=set([])
        double_claims=set([])
        for line in self.data:
            m=claim_re.match(line)
            if m:
                x_start = int(m.group('x'))
                x_end   = int(m.group('xlen'))+x_start 
                y_start = int(m.group('y'))
                y_end   = int(m.group('ylen'))+y_start 
                for y in range(y_start,y_end):
                    for x in range(x_start,x_end):
                        pos=(x,y)
                        if pos in fabric:
                            double_claims.add(pos)
                        fabric.add(pos)
                
        print("Day3 challenge1: {}".format(len(double_claims)))

    def solve2(self):
        claim_re=re.compile("^#(?P<id>[0-9]+)\s*@\s*(?P<x>[0-9]+),(?P<y>[0-9]+):\s*(?P<xlen>[0-9]+)x(?P<ylen>[0-9]+)")
        none_overlap_id=set()
        pos2id={}
        for line in self.data:
            m=claim_re.match(line)
            if m:
                x_start = int(m.group('x'))
                x_end   = int(m.group('xlen'))+x_start 
                y_start = int(m.group('y'))
                y_end   = int(m.group('ylen'))+y_start 
                ID      = m.group('id')
                overlap = False
                for y in range(y_start,y_end):
                    for x in range(x_start,x_end):
                        pos=(x,y)
                        if pos in pos2id:
                            none_overlap_id.discard(pos2id[pos])
                            overlap = True
                        pos2id[pos]=ID
                if not overlap:
                    none_overlap_id.add(ID)
        print("Day3 challenge2: {} (length {})".format(none_overlap_id.pop(),len(none_overlap_id)))

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
        

