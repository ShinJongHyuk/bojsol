import sys
sys.stdin = open('input.txt')

for _ in range(4):
    stack = []
    x, y, p, q, x2, y2, p2, q2 = map(int, input().split())
    maxV = max(x, y, p, q, x2, y2, p2, q2)
    arr = [[0]*(maxV+1) for _ in range(maxV+1)]
    for i in range(x,p+1):
        for j in range(y,q+1):
            arr[i][j] += 1
    for i in range(x2, p2 + 1):
        for j in range(y2, q2 + 1):
            arr[i][j] += 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                stack.append([i,j])
    if stack:
        print(stack[0],stack[-1])
    if stack:
        if abs(stack[-1][0] - stack[0][0]) != 0 and abs(stack[-1][1] - stack[0][1]) != 0:
            print('a')
        elif abs(stack[-1][0] - stack[0][0]) == 0 and abs(stack[-1][1] - stack[0][1]) == 0:
            print('c')
        elif abs(stack[-1][0] - stack[0][0]) == 0 or abs(stack[-1][1] - stack[0][1]) == 0:
            print('b')


    else:
        print('d')
#
# for _ in range(4):
#     x, y, p, q, x2, y2, p2, q2 = map(int, input().split())
#     if x < x2:
#         x = x2
#     if p > p2:
#         p = p2
#     if y < y2:
#         y = y2
#     if q > q2:
#         q = q2
#     # print(x,y,p,q)
#
#     # if p - x < 0 and q - y < 0:
#     #     print('d')
#     # elif p - x == 0 and q - y == 0:
#     #     print('c')
#     # elif p - x == 0 and q - y < 0:
#     #     print('a')
#     # elif p - x < 0 and q - y == 0:
#     #     print('a')
#     # elif p - x == 0 and q - y < 0:
#     #     print('a')
#     #
#     #
#     # else:
#     #     print('d')
#     if p - x >= 0 or q - y >= 0 :
#         if abs(p - x) != 0 and abs(q - y) != 0:
#             print('a')
#         elif abs(p - x) == 0 and abs(q - y) == 0:
#             print('c')
#         elif abs(p - x) == 0 or abs(q - y) == 0:
#             print('b')
#
#
#     else:
#         print('d')