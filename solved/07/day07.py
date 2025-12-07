#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 7
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    lns = get_lines(v)
    x = lns[0].index('S')
    beams = set([x])
    splits = 0
    for ln in lns[1:]:
        beams2 = set()
        for i in beams:
            if ln[i] == '^':
                beams2.add(i-1)
                beams2.add(i+1)
                splits += 1
            else:
                beams2.add(i)
        beams = beams2
    return splits

def p2(v):
    lns = get_lines(v)
    x = lns[0].index('S')
    beams = {x : 1}
    for ln in lns[1:]:
        beams2 = Counter()
        for i, cnt in beams.items():
            if ln[i] == '^':
                beams2[i-1] += cnt
                beams2[i+1] += cnt
            else:
                beams2[i] += cnt
        beams = beams2
    return sum(beams.values())

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
