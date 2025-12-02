#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 1
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))


def p1(v):
    lns = get_lines(v)
    dial = 50
    ans = 0
    for ln in lns:
        amount = int(ln[1:])
        if ln[0] == 'L':
            for _ in range(amount):
                dial -= 1
                if dial < 0:
                    dial += 100
        else:
            for _ in range(amount):
                dial += 1
                if dial >= 100:
                    dial -= 100
        if dial == 0:
            ans += 1
    return ans

def p2(v):
    lns = get_lines(v)
    dial = 50
    ans = 0
    for ln in lns:
        amount = int(ln[1:])
        if ln[0] == 'L':
            for _ in range(amount):
                dial -= 1
                if dial == 0:
                    ans += 1
                if dial < 0:
                    dial += 100
        else:
            for _ in range(amount):
                dial += 1
                if dial >= 100:
                    dial -= 100
                if dial == 0:
                    ans += 1
    return ans
    
LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
