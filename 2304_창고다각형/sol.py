import sys
sys.stdin = open('input.txt')

arr = [[0]*1000 for _ in range(1000)]

data = []
N = int(input())
for _ in range(N):
    a, b = list(map(int, input().split()))
    data.append([a, b])
data.sort()
maxT = 0
maxT_idx = 0

for i in range(len(data)):
    if maxT < data[i][1]:
        maxT = data[i][1]
        maxT_idx = i

result = data[maxT_idx][1]

start = data[0][0]
H = data[0][1]
for i in range(1, maxT_idx+1):
    if data[i][1] >= H:
        result += (data[i][0] - start) * H
        H = data[i][1]
        start = data[i][0]

start2 = data[-1][0]
H2 = data[-1][1]
for i in range(len(data)-1, maxT_idx-1, -1):
    if data[i][1] >= H2:
        result += (start2 - data[i][0]) * H2
        H2 = data[i][1]
        start2 = data[i][0]

print(result)




