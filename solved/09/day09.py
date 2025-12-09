#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 9
def get_year(): return 2025

def parse(ln):
    return lazy_ints(multi_split(ln, ','))

def makeLine(p1, p2):
    pts = []
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            pts.append((x1, y))
        if y2 < y1:
            pts = pts[::-1]
    else:
        assert y1 == y2
        for x in range(min(x1, x2), max(x1, x2) + 1):
            pts.append((x, y1))
        if x2 < x1:
            pts = pts[::-1]
    return pts

def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def sign(x):
    if x < 0: return -1
    return 1 if x > 0 else 0

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def overlap(s1, s2):
    dx1, dy1 = vec(*s1)
    dx2, dy2 = vec(*s2)
    assert dx1 == 0 or dy1 == 0
    assert dx2 == 0 or dy2 == 0, f'{dx2} {dy2}'
    if dx1 == dx2 == 0 or dy1 == dy2 == 0:
        return False
    if dx1 == 0:
        s1, s2 = s2, s1
    x1 = s1[0][0]
    x2 = s1[1][0]
    x1, x2 = min(x1, x2), max(x1, x2)
    xs = s2[0][0]
    y1 = s2[0][1]
    y2 = s2[1][1]
    y1, y2 = min(y1, y2), max(y1, y2)
    ys = s1[0][1]
    return x1 <= xs <= x2 and y1 <= ys <= y2

def area(polygon):
    A = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i-1]
        x2, y2 = polygon[i]
        A += (x1 + x2) * (y2 - y1)
    return A/2


def sgn(u):
    return sign(u[0]), sign(u[1])

def p1(v):
    lns = get_lines(v)
    pts = []
    for ln in lns:
        x, y = parse(ln)
        pts.append((x,y))
    mx = 0
    for p in pts:
        for q in pts:
            x1, y1 = p
            x2, y2 = q
            A = (abs(x1-x2) + 1)*(1 + abs(y1-y2))
            if A > mx:
                mx = A
    return mx

def p2(v):
    lns = get_lines(v)
    pts = []
    for ln in lns:
        x, y = parse(ln)
        pts.append((x,y))
    if area(pts) < 0:
        pts = pts[::-1]

    left = set()
    for p1, p2, p3 in zip(pts, pts[1:] + pts[:1], pts[2:]+ pts[:2]):
        u, v = sgn(vec(p2, p1)), sgn(vec(p3, p2))
        if cross(u, v) < 0:
            left.add(p2)
    forbidden = []
    for p1, p2 in zip(pts, pts[1:]):
        dx, dy = sgn(vec(p1, p2))
        ROT = {
            (0, 1) : (1, 0),
            (1, 0) : (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        out_x, out_y = ROT[dx, dy]
        S = p1[0] + out_x, p1[1] + out_y
        E = p2[0] + out_x, p2[1] + out_y
        if p1 in left:
            S = S[0] + dx, S[1] + dy
        if p2 in left:
            E = E[0] - dx, E[1] - dy
        forbidden.append((S, E))
    mx = 0
    for p in pts:
        for q in pts:
            px, py = p
            qx, qy = q
            xl, xh = min(px, qx), max(px, qx)
            yl, yh = min(py, qy), max(py, qy)
            sqsegs = [
                ((xl, yl), (xl, yh)),
                ((xl, yl), (xh, yl)),
                ((xh, yh), (xl, yh)),
                ((xh, yh), (xh, yl)),
            ]

            ok = True
            for s2 in sqsegs:
                for s in forbidden:
                    if overlap(s, s2):
                        ok = False
                        break
                if not ok: break
            if ok:
                x1, y1 = p
                x2, y2 = q
                A = (abs(x1-x2) + 1)*(1 + abs(y1-y2))
                if A > mx:
                    mx = A
    return mx

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
