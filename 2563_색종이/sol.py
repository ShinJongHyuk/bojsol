import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    a, b = map(int,input().split())

    for i in range(b, b + 10):
        for j in range(a, a + 10):
            arr[i][j] += 1
result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            result += 1
print(result)