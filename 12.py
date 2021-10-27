import io
import sys
_INPUT = """\
1 1
3
2 1 1 1 1
1 1 1
2 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

H, W = map(int, input().split())
Q = int(input())
M = [[0 for _ in range(W)] for _ in range(H)]# 0: white, 1: red
P = [i for i in range(H*W)]#parent

def solve1(Com):
  x0 = Com[1]-1
  y0 = Com[2]-1
  M[x0][y0] = 1
  toX = [0, 1, 0, -1]
  toY = [1, 0, -1, 0]
  for i in range(4):
    x = x0 +toX[i]
    y = y0 +toY[i]
    if(0<=x and x<H and 0<=y and y<W and M[x][y]==1):
      unite((x0, y0), (x, y))

def unite(a, b):
  aP = a[0]*W + a[1]
  bP = b[0]*W + b[1]
  P[find(aP)] = find(bP)

def same(a, b):
  aP = a[0]*W + a[1]
  bP = b[0]*W + b[1]
  return find(aP) == find(bP)

def find(x):
  if P[x] == x:
    return x
  else:
    P[x] = find(P[x])
    return  P[x]

def solve2(Com):
  x0, y0 = Com[1]-1, Com[2]-1
  x1, y1 = Com[3]-1, Com[4]-1
  toX = [0, 1, 0, -1]
  toY = [1, 0, -1, 0]
  if(M[x0][y0] == 1):
    for i in range(4):
      x = x0 +toX[i]
      y = y0 +toY[i]
      if(0<=x and x<H and 0<=y and y<W and M[x][y]==1):
        unite((x0, y0), (x, y))
  if(M[x1][y1] == 1):
    for i in range(4):
      x = x1 +toX[i]
      y = y1 +toY[i]
      if(0<=x and x<H and 0<=y and y<W and M[x][y]==1):
        unite((x1, y1), (x, y))
  if M[x0][y0]==1 and M[x1][y1]==1 and same((x0, y0), (x1, y1)):
    print("Yes")
  else:
    print("No")

for i in range(Q):
  Com = list(map(int,input().split()))
  if(Com[0] == 1):
    solve1(Com)
  else:
    solve2(Com)
