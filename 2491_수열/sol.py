import sys
sys.stdin = open('input.txt')

N = int(input())
data = list(map(int,input().split()))
result = []
cnt = 1

for i in range(len(data)-1):
    if data[i] <= data[i+1]:
        cnt += 1
    elif data[i] > data[i+1]:
        result.append(cnt)
        cnt = 1
else:
    result.append(cnt)

cnt = 1
for i in range(len(data)-1):
    if data[i] >= data[i+1]:
        cnt += 1
    elif data[i] < data[i+1]:
        result.append(cnt)
        cnt = 1
else:
    result.append(cnt)
print(result)
print(max(result))