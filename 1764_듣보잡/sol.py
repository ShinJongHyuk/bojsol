import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

A = set()
B = set()
for _ in range(N):
    x = input()
    A.add(x)
for _ in range(M):
    y = input()
    B.add(y)

C = sorted(list(A & B))

print(len(C))

for i in C:
    print(i)