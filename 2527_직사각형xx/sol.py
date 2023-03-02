import sys
sys.stdin = open('input.txt')

for _ in range(4):
    x, y, p, q, x2, y2, p2, q2 = map(int, input().split())

    if x2 < p and y2 < q :
        print('a')
    elif (x2 - p == 0 and y2 < q) or (x2 < p and y2 - q == 0):
        print('b')
    elif (x2 - p and y2 - q == 0):
        print('c')
    elif x2 > p and y2 > q:
        print('d')






    # maxV = max(x, y, p, q, x2, y2, p2, q2)
    # arr = [[0]*(maxV+1) for _ in range(maxV+1)]
    # for i in range(x,p+1):
    #     for j in range(y,q+1):
    #         arr[i][j] += 1
    # for i in range(x2, p2 + 1):
    #     for j in range(y2, q2 + 1):
    #         arr[i][j] += 1
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i][j] == 2:
    #             stack.append([i,j])
    # if stack:
    #     if abs(stack[-1][0] - stack[0][0]) != 0 and abs(stack[-1][1] - stack[0][1]) != 0:
    #         print('a')
    #     elif abs(stack[-1][0] - stack[0][0]) == 0 and abs(stack[-1][1] - stack[0][1]) == 0:
    #         print('c')
    #     elif abs(stack[-1][0] - stack[0][0]) == 0 or abs(stack[-1][1] - stack[0][1]) == 0:
    #         print('b')
    #
    #
    # else:
    #     print('d')