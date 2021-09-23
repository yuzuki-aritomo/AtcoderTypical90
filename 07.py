import io
import sys
_INPUT = """\
10
869120000 998244353 777777777 123456789 100100100 464646464 987654321 252525252 869120001 1000000000
10
4229
20210406
1
268435456
3582
536870912
1000000000
869120
99999999
869120001
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort()
A.insert(0, -10**10)
A.append(10**10)

import bisect
ans = 0
for _ in range(Q):
  b = int(input())
  id = bisect.bisect_left(A, b)
  print(min(abs(b-A[id]), abs(b-A[id-1])))
