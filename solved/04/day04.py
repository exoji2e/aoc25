#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 4
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    save_input(v)
    G = [list(ln) for ln in get_lines(v)]
    ans = 0
    R, C = len(G), len(G[0])
    for r in range(R):
        for c in range(C):
            if G[r][c] != '@': continue
            cnt = 0
            for nr, nc in grid8nf(r, c, R, C):
                if G[nr][nc] == '@':
                    cnt += 1
            if cnt < 4:
                ans += 1
    return ans

def p2(v):
    G = [list(ln) for ln in get_lines(v)]
    ans = 0
    ch = True
    R, C = len(G), len(G[0])
    while ch:
        ch = False
        for r in range(R):
            for c in range(C):
                if G[r][c] != '@': continue
                cnt = 0
                for nr, nc in grid8nf(r, c, R, C):
                    if G[nr][nc] == '@':
                        cnt += 1
                if cnt < 4:
                    ans += 1
                    G[r][c] = '.'
                    ch = True
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
