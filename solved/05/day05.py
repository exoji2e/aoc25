#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 5
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, '-'))

def p1(v):
    chunks = v.split('\n\n')
    fresh = [parse(ln) for ln in chunks[0].split('\n')]
    ans = 0
    for ln in chunks[1].split('\n'):
        x = int(ln)
        ok = False
        for lo, hi in fresh:
            if lo <= x <= hi:
                ok = True
        if ok: ans += 1
    return ans

def p2(v):
    chunks = v.split('\n\n')
    fresh = [parse(ln) for ln in chunks[0].split('\n')]
    found = 0
    last = 0
    for lo, hi in sorted(fresh):
        if lo <= last:
            lo = last + 1
        found += max(hi - lo + 1, 0)
        last = max(hi, last)

    return found

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
