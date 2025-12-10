#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 10
def get_year(): return 2025

def parse(ln):
    arr = ln.split()
    T = [ch == '#' for ch in arr[0][1:-1]]
    T2 = lazy_ints(arr[-1][1:-1].split(','))
    btns = [lazy_ints(x[1:-1].split(',')) for x in arr[1:-1]]

    return T, T2, btns

import z3
def solve2(T, btns):
    s = z3.Optimize()
    vars = [z3.Int(f'x_{i}') for i in range(len(btns))]
    for v in vars:
        s.add(v >= 0)
    for i, x in enumerate(T):
        compute = 0
        for j, b in enumerate(btns):
            if i in b:
                compute += vars[j]
        s.add(compute == x)
    su = z3.Int('su')
    s.add(su == sum(vars))
    h = s.minimize(su)
    s.check()
    model = s.model()
    ans = model.evaluate(su).as_long()
    return ans

def solve(T, btns):
    ans = len(btns)
    for mask in range(2**len(btns)):
        arr = []
        for j in range(len(btns)):
            if mask & 2**j:
                arr.append(j)
        togs = [False]*len(T)
        for ix in arr:
            for ix2 in btns[ix]:
                togs[ix2] = not togs[ix2]
        if T == togs:
            ans = min(ans, len(arr))
    return ans


def p1(v):
    save_input(v)
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        T, _, btns = parse(ln)
        x = solve(T, btns)
        ans += x
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        _, T, btns = parse(ln)
        x = solve2(T, btns)
        ans += x
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
