#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 11
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ' :'))

def parseGraph(v):
    lns = get_lines(v)
    nodes = set()
    G = defaultdict(list)
    ps = Counter()
    for ln in lns:
        item = parse(ln)
        nodes |= set(item)
        G[item[0]] = item[1:]
        for x in item[1:]:
            ps[x] += 1
    
    order = [name for name in nodes if ps[name] == 0]
    for u in order:
        for v in G[u]:
            ps[v] -= 1
            if ps[v] == 0:
                order.append(v)
    return G, order

def p1(v):
    G, order = parseGraph(v)
    dp = Counter()
    dp['you'] = 1
    for u in order:
        for v in G[u]:
            dp[v] += dp[u]
    return dp['out']

def p2(v):
    G, order = parseGraph(v)
    paths = [
        ['svr', 'fft', 'dac', 'out'],
        ['svr', 'dac', 'fft', 'out'],
    ]

    ans = 0
    for path in paths:
        mul = 1
        for S, T in zip(path, path[1:]):
            dp = Counter()
            dp[S] = 1
            for u in order:
                for v in G[u]:
                    dp[v] += dp[u]
            mul *= dp[T]
        ans += mul
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
