#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 2
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    save_input(v)
    rns = v.split(',')
    invalid = []
    for r in rns:
        lo, hi = map(int, r.split('-'))
        for i in range(lo, hi + 1):
            s = str(i)
            L = len(s)//2
            if s[:L] == s[L:]:
                invalid.append(i)
    print(invalid)
    return sum(invalid)

def p2(v):
    rns = v.split(',')
    invalid = []
    for r in rns:
        lo, hi = map(int, r.split('-'))
        for i in range(lo, hi + 1):
            s = str(i)
            ok = False
            for L in range(1,len(s)):
                if len(s) % L == 0:
                    pre = s[:L]
                    if all(pre == s[k*L:(k+1)*L] for k in range(len(s)//L)):
                        ok = True
            #L = len(s)//2
            if ok: #s[:L] == s[L:]:
                invalid.append(i)
    print(invalid)
    return sum(invalid)

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
