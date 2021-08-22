import io
import sys
_INPUT = """\
20
2 90
1 67
2 9
2 17
2 85
2 43
2 11
1 32
2 16
1 19
2 65
1 14
1 51
2 94
1 4
1 55
2 90
1 89
1 35
2 81
20
3 17
5 5
11 11
8 10
3 13
2 6
3 7
3 5
12 18
4 8
3 16
6 8
3 20
1 12
1 6
5 16
3 10
17 19
4 4
7 15
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []

for i in range(N):
  A.append(list(map(int,input().split())))

sum1 = 0
sum2 = 0
M1 = [0]
M2 = [0]
for i in range(N):
  if(A[i][0] == 1):
    sum1 += A[i][1]
  else:
    sum2 += A[i][1]
  M1.append(sum1)
  M2.append(sum2)

Q = int(input())
for i in range(Q):
  l, r = map(int,input().split())
  ans1 = M1[r] - M1[max(0, l-1)]
  ans2 = M2[r] - M2[max(0, l-1)]
  print(ans1, ans2)