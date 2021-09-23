import io
import sys
_INPUT = """\
140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
mod = 10**9+7
A = [0 for _ in range(7)]

at = ["a", "t", "c", "o", "d", "e", "r"]
ans = 0
for i in range(N):
  for j in range(len(at)):
    if S[i] == at[j]:
      if j == 0:
        A[0] += 1
      else:
        A[j] += A[j-1]
        A[j] %= mod

print(A[-1])