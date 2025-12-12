#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 12
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    chunks = v.split('\n\n')
    PS = [chunk.split('\n')[1:] for chunk in chunks[:-1]]

    A = []
    for p in PS:
        a = 0
        for r in p:
            for c in r:
                if c == '#':
                    a += 1
        A.append(a)

    lns = chunks[-1].split('\n')
    ans = 0
    f = 0
    u = 0
    for ln in lns:
        arr = ln.split()
        w,h = map(int, arr[0][:-1].split('x'))
        use = [int(x) for x in arr[1:]]
        su = sum(use)
        area = sum(A[i]*k for i, k in enumerate(use))
        if w//3*h//3 >= su:
            ans += 1
        elif area > w*h:
            f += 1
        else:
            u += 1

    print(ans, f, u)
    return ans

def p2(v):
    return 'Press the button'

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
