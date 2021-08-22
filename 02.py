import io
import itertools
import sys
_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

if(N%2 == 1):
  print()
  exit()

A = [0 for _ in range(N//2)] + [1 for _ in range(N//2)]

for i in range(2**N-1, -1, -1):
  f = 0
  ans = ""
  Flag = True
  for j in range(N-1, -1, -1):
    if(i>>j&1):
      f += 1
      ans += "("
    else:
      f -= 1
      ans += ")"
    if(f<0):
      Flag = False
      break
  if Flag and f==0:
    # print(i)
    print(ans)