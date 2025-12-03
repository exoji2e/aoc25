#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 3
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    save_input(v)
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        fr = ln[:-1]
        d, i = max([(ch, -i) for i, ch in enumerate(fr)])
        i = -i
        fr = ln[i+1:]
        d2 = max(fr)
        ans += int(d + d2)
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        dgs = []
        last = -1
        for i in range(12):
            fr = ln[last+1:len(ln) - 11 + i]
            d, i = max([(ch, -i) for i, ch in enumerate(fr)])
            dgs.append(d)
            last = -i + last + 1
        s = ''.join(dgs)
        ans += int(s)
    return ans
LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
