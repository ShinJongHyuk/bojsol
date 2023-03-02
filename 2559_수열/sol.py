import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
data = [0] + list(map(int,input().split()))

result = []
for i in range(1,N+1):
    data[i] += data[i-1]
for i in range(K,N+1):
    result.append(data[i] - data[i-K])
print(max(result))