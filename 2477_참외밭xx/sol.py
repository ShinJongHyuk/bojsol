import sys
sys.stdin = open('input.txt')

arr = [[0]*500 for _ in range(500)]
K = int(input())
data = []
for _ in range(6):
    D, L = map(int,input().split()) # 1 = 동, 2 = 서, 3 = 남, 4 = 북
    data.append(D)
    data.append(L)
print(data)
start = 0
for i in range(6):
    if data[i*2] == 1 or 2:
        if data[i*2+1] > start:
            start = data[i*2+1]

for i in range(data[1]):
    arr[i][0] = 1
for i in range(data[3]):
    arr[data[1]][i] = 1
for i in range(data[1]-data[5], data[1]):
    arr[i][data[3]] = 1

for i in arr:
    print(i)