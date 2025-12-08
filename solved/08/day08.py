#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 8
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ','))

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.sz = [1]*N
    def find(self, i):
        path = []
        while i != self.parent[i]:
            path.append(i)
            i = self.parent[i]
        for u in path: self.parent[u] = i
        return i
    def union(self, u, v):
        uR, vR = map(self.find, (u, v))
        if uR == vR: return False
        if self.sz[uR] < self.sz[vR]:
            self.parent[uR] = vR
            self.sz[vR] += self.sz[uR]
        else:
            self.parent[vR] = uR
            self.sz[uR] += self.sz[vR]
        return True

def dist(p1, p2):
    x, y, z = p1
    x2,y2,z2 = p2
    return (x - x2)**2 + (y-y2)**2 + (z-z2)**2

def p1(v):
    lns = get_lines(v)
    items = []
    for ln in lns:
        item = parse(ln)
        items.append(item)
    N = len(items)
    uf = UnionFind(N)
    dists = []
    for i in range(N):
        for j in range(i+1, N):
            dists.append((dist(items[i], items[j]), i, j))
    dists.sort()
    for _, i, j in dists[:1000]:
        uf.union(i, j)
    C = Counter()
    for x in range(N):
        C[uf.find(x)] += 1
    lst = sorted(list(C.values()))
    return lst[-1]*lst[-2]*lst[-3]


def p2(v):
    lns = get_lines(v)
    items = []
    for ln in lns:
        item = parse(ln)
        items.append(item)
    N = len(items)
    uf = UnionFind(N)
    dists = []
    for i in range(N):
        for j in range(i+1, N):
            dists.append((dist(items[i], items[j]), i, j))
    dists.sort()
    left = N-1
    for _, i, j in dists:
        if uf.union(i, j):
            left -= 1
        if left == 0:
            return items[i][0] * items[j][0]

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
