import io
import sys
_INPUT = """\
3
1 2
1 3
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

N = int(input())
M = [[] for i in range(N+1)]
for _ in range(N-1):
  a, b = map(int,input().split())
  M[a].append(b)
  M[b].append(a)
# print(M)

deep = [0 for i in range(N+1)]
color = [0 for i in range(N+1)]

def dfs(n, d):
  color[n] = 1
  deep[n] = d
  for id in M[n]:
    if(color[id] == 0):
      dfs(id, d+1)
dfs(1, 0)

id = deep.index(max(deep))
deep = [0 for i in range(N+1)]
color = [0 for i in range(N+1)]
dfs(id, 0)

print(max(deep)+1)