import sys
sys.stdin = open('input.txt')

arr = [[0]*1000 for _ in range(1000)]

data = []
stack = [0]
N = int(input())
for _ in range(N):
    a, b = list(map(int, input().split()))
    data.append([a, b])
data.sort()
# print(data)
maxT = 0
maxT_idx = 0
for i in range(len(data)):
    if maxT < data[i][1]:
        maxT = data[i][1]
        maxT_idx = i

# for i in range(len(data)):
#     x = data[i][0]
#     y = data[i][1]
#     if i == maxT_idx:
#         continue
#     elif i > maxT_idx:
#         for j in range(data[maxT_idx][0], x):
#             for k in range(0,y):
#                 if not arr[j][k]:
#                     stack[0] += 1
#                 arr[j][k] += 1
#     else:
#         for j in range(x,data[maxT_idx][0]):
#             for k in range(0,y):
#                 if not arr[j][k]:
#                     stack[0] += 1
#                 arr[j][k] += 1



result = data[maxT_idx][1] + stack[0]

# for i in range(len(arr)):
#     if i > data[-1][0]:
#         break
#     for j in range(len(arr)):
#         if j > maxT:
#             break
#         if arr[i][j]:
#             result += 1

print(result)


