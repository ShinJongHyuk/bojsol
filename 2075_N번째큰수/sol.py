import sys
sys.stdin = open('input.txt')

N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

result = []
for i in data:
    for j in i:
        result.append(j)
result.sort()
print(result[-5])