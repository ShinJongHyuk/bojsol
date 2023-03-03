import sys
sys.stdin = open('input.txt')

K = int(input())
data = []
for _ in range(6):
    D = list(map(int,input().split())) # 1 = 동, 2 = 서, 3 = 남, 4 = 북
    data.append(D)
# print(data)

w = 0
h = 0
for i in range(len(data)):
    if data[i][0] == 1 or data[i][0] == 2:
        if data[i][1] > w:
            w = data[i][1]
    if data[i][0] == 3 or data[i][0] == 4:
        if data[i][1] > h:
            h = data[i][1]

w_idx = 0
h_idx = 0
for i in range(len(data)):
    if data[i][1] == w:
        w_idx = i
    if data[i][1] == h:
        h_idx = i
minw = 0
minh = 0
if w_idx == 0:
    minw = abs(data[-1][1] - data[w_idx+1][1])
elif w_idx == len(data)-1:
    minw = abs(data[0][1] - data[w_idx - 1][1])
else:
    minw = abs(data[w_idx - 1][1] - data[w_idx + 1][1])

if h_idx == 0:
    minh = abs(data[-1][1] - data[h_idx+1][1])
elif h_idx == len(data)-1:
    minh = abs(data[0][1] - data[h_idx - 1][1])
else:
    minh = abs(data[h_idx - 1][1] - data[h_idx + 1][1])
print((h*w - minh*minw) * K)





# minw = 500
# minh = 500
#
# for i in range(len(data)):
#     if data[i][0] == 1 or data[i][0] == 2:
#         if data[i][1] > maxw:
#             maxw = data[i][1]
#         if data[i][1] < minw:
#             minw = data[i][1]
# for i in range(len(data)):
#     if data[i][0] == 3 or data[i][0] == 4:
#         if data[i][1] > maxh:
#             maxh = data[i][1]
#         if data[i][1] < minh:
#             minh = data[i][1]
#
# # print(maxw,maxh,minw,minh)
# X = (maxw * maxh) - (minw * minh)
# print(X*K)