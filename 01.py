import io
import sys
_INPUT = """\
3 34
1
8 13 26
"""
sys.stdin = io.StringIO(_INPUT)


N, L = map(int, input().split())
K = int(input())

A = list(map(int,input().split()))
M = [A[0]]
for i in range(1, N):
  M.append(A[i] - A[i-1])
M.append( L- A[-1])
# print(M)

#n以上可能か判定
def check(n):
  global K, N
  tmp = 0
  flag = 0
  for i in range(N+1):
    tmp += M[i]
    # print(tmp)
    if(tmp>=n):
      tmp = 0
      flag += 1
  # print(flag)
  if(flag>=K+1):
    return True
  else:
    return False

# print(check(13))

l = -1
r = L+1
while(l<r):
  mid = (l + r)//2
  if check(mid):
    l = mid + 1
  else:
    r = mid

print(l-1)

