import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
data = []
for i in range(1,N+1):
    data.append(i)
print(data)
result = []
stack = []
cnt = 0
while data:
    for i in range(len(data)-1):
        cnt += 1
        if cnt >= 3 and cnt % 3 == 0:
            result.append(data.pop(i-1))
            break
        data.append(data.pop(i-1))

print(result)

