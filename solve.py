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

class Day4(Day):
    def __init__(self):
        Day.__init__(self,4)
    def solve1(self):
        print("Day4 challlenge1: {}".format(''))
    def solve2(self):
        print("Day4 challlenge2: {}".format(''))

class Day5(Day):
    def __init__(self):
        Day.__init__(self,5)
    def solve1(self):
        result=[]
        for ch in "dabAcCaCBAcCcaDA":
            
            print("Day5 challlenge1: {}".format(''))
    def solve2(self):
        print("Day5 challlenge2: {}".format(''))

class Day6(Day):
    def __init__(self):
        Day.__init__(self,6)
    def solve1(self):
        print("Day6 challlenge1: {}".format(''))
    def solve2(self):
        print("Day6 challlenge2: {}".format(''))

class Day7(Day):
    def __init__(self):
        Day.__init__(self,7)
    def solve1(self):
        print("Day7 challlenge1: {}".format(''))
    def solve2(self):
        print("Day7 challlenge2: {}".format(''))

class Day8(Day):
    def __init__(self):
        Day.__init__(self,8)
    def solve1(self):
        print("Day8 challlenge1: {}".format(''))
    def solve2(self):
        print("Day8 challlenge2: {}".format(''))

class Day9(Day):
    def __init__(self):
        Day.__init__(self,9)
    def solve(self,challenge):
        m = re.match("(?P<players>[0-9]+)\splayers.*worth\s(?P<last_marble>[0-9]+)\spoints",self.data[0])#"30 players worth 5807 points")
        if m:
            players = int(m.group('players'))
            last_marble = int(m.group('last_marble')) * (1 if challenge == 1 else 2)
            circle=[0]
            current_pos=0
            player_points={}
            for i in range(0,last_marble):
                marble=i+1
                player=(i % players) +1
                if marble%23 == 0:
                    current_pos = (current_pos - 7) % len(circle)
                    points = circle.pop(current_pos)+marble
                    player_points[player]=player_points.setdefault(player,0)+points
                else:    
                    current_pos = current_pos + 2
                    if current_pos > len(circle):
                        current_pos = 1
                    circle.insert(current_pos,marble)
            high_score=0
            for player,score in player_points.items():
                if score > high_score:
                    high_score = score
        print("Day9 challlenge{}: {}".format(challenge,high_score))
    def solve1(self):
        self.solve(1)
    def solve2(self):
        self.solve(2)

class Day10(Day):
    def __init__(self):
        Day.__init__(self,10)
    def solve1(self):
        print("Day10 challlenge1: {}".format(''))
    def solve2(self):
        print("Day10 challlenge2: {}".format(''))

def main(args):
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('day', metavar='DAY', type=int, choices=range(1,25), help="day to solve")
    parser.add_argument('challenge', metavar='CHALLENGE', type=int, choices=range(1,3), help="challenge to solve")
    args = parser.parse_args(args)
    
    day = getattr(sys.modules[__name__],"Day{}".format(args.day))()
    if args.challenge == 1:
        day.solve1()
    else:
        day.solve2()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
        

