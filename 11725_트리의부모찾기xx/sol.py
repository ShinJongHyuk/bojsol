import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    data = []
    for i in range(N-1):
        a,b = list(map(int,input().split()))
        data.append(a)
        data.append(b)
    for i in range(len(data)//2):
        p, c = data[i*2], data[i*2+1]
        if p == 1:
            if tree[p][0] == 0:
                tree[p][0] = c
            else:
                tree[p][1] = c
            tree[c][2] = p
        if c == 1:
            p, c = c, p
            if tree[p][0] == 0:
                tree[p][0] = c
            else:
                tree[p][1] = c
            tree[c][2] = p
    for i in range(len(data)//2):
        p, c = data[i*2], data[i*2+1]
        if tree[p][2] and (p or c != 1):
            if tree[p][0] == 0:
                tree[p][0] = c
            else:
                tree[p][1] = c
            tree[c][2] = p



    for i in tree:
        print(i)
    print()




    #
    # for i in range(len(data)):
    #     if data[i][0] == 1:
    #         if tree[1][0] == 0:
    #             tree[1][0] = data[i][1]
    #         else:
    #             tree[1][1] = data[i][1]
    #         tree[data[i][1]][2] = data[i][0]
    #     elif data[i][1] == 1:
    #         if tree[1][0] == 0:
    #             tree[1][0] = data[i][0]
    #         else:
    #             tree[1][1] = data[i][0]
    #         tree[data[i][0]][2] = data[i][1]
    #
    # for i in range(len(data)):
    #     if data[i][0] != 1 and data[i][1] != 1:
    #         if tree[data[i][1]][2] == 0:
    #             if tree[data[i][0]][0] == 0:
    #                 tree[data[i][0]][0] = data[i][1]
    #             else:
    #                 tree[data[i][0]][1] = data[i][1]
    #             tree[data[i][1]][2] = data[i][0]
    #         elif tree[data[i][1]][2]:
    #             if tree[data[i][1]][0] == 0:
    #                 tree[data[i][1]][0] = data[i][0]
    #             else:
    #                 tree[data[i][1]][1] = data[i][0]
    #             tree[data[i][0]][2] = data[i][1]
    # # cnt = -1
    # # for i in tree:
    # #     cnt += 1
    # #     print(cnt,i)
    # # print()
    # for i in range(2,N+1):
    #     print(tree[i][2])
    # print()