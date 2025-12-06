#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 6
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    lns = get_lines(v)
    ans = 0
    rows = []
    for ln in lns:
        row = parse(ln)
        rows.append(row)
    ops = rows[-1]
    matrix = [[rows[i][j] for i in range(len(rows) - 1)] for j in range(len(rows[0]))]
    for op, nums in zip(ops, matrix):
        if op == '+':
            v = 0
            for x in nums:
                v += x
            ans += v
        else:
            v = 1
            for x in nums:
                v *= x
            ans += v
    return ans
    

def p2(v):
    lns = get_lines(v)
    ans = 0
    ln = lns[-1]
    pos = []
    ops = []
    for i, ch in enumerate(ln):
        if ch != ' ':
            pos.append(i)
            ops.append(ch)
    pos.append(len(ln))
    matrix = []
    for i, j in zip(pos, pos[1:]):
        grid = []
        for ln in lns[:-1]:
            grid.append(ln[i:j])
        nums = []
        for i in range(len(grid[0])):
            s = ''.join(row[i] for row in grid if row[i] != ' ')
            if s:
                x = int(s)
                nums.append(x)

        matrix.append(nums)
    
    for op, nums in zip(ops, matrix):
        if op == '+':
            v = 0
            for x in nums:
                v += x
            ans += v
        else:
            v = 1
            for x in nums:
                v *= x
            ans += v

    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
