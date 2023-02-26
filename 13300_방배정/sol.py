import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
arr = [[0]*7 for _ in range(2)]
for _ in range(N):
    S, Y = map(int,input().split())
    arr[S][Y] += 1

result = 0
for i in range(2):
    for j in range(1,7):
        if arr[i][j] != 0 and arr[i][j] <= K:
            result += 1
        elif arr[i][j] > K and arr[i][j] % K == 1:
            result = result + arr[i][j]//2 + 1
        elif arr[i][j] > K and arr[i][j] % K == 0:
            result = result + arr[i][j] // 2
print(result)



