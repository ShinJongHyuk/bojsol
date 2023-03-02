import sys
sys.stdin = open('input.txt')

K = int(input())
data = []
for _ in range(6):
    D = list(map(int,input().split())) # 1 = 동, 2 = 서, 3 = 남, 4 = 북
    data.append(D)
# print(data)

maxw = 0
maxh = 0
minw = 500
minh = 500

for i in range(len(data)):
    if data[i][0] == 1 or data[i][0] == 2:
        if data[i][1] > maxw:
            maxw = data[i][1]
        if data[i][1] < minw:
            minw = data[i][1]
for i in range(len(data)):
    if data[i][0] == 3 or data[i][0] == 4:
        if data[i][1] > maxh:
            maxh = data[i][1]
        if data[i][1] < minh:
            minh = data[i][1]

# print(maxw,maxh,minw,minh)
X = (maxw * maxh) - (minw * minh)
print(X*K)