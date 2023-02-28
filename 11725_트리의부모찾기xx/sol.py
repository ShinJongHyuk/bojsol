import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    data = []
    for i in range(N-1):
        d = list(map(int,input().split()))
        data.append(d)

    for i in range(len(data)):
        if data[i][0] == 1:
            if tree[1][0] == 0:
                tree[1][0] = data[i][1]
            else:
                tree[1][1] = data[i][1]
            tree[data[i][1]][2] = data[i][0]
        elif data[i][1] == 1:
            if tree[1][0] == 0:
                tree[1][0] = data[i][0]
            else:
                tree[1][1] = data[i][0]
            tree[data[i][0]][2] = data[i][1]

    for i in range(len(data)):
        if data[i][0] != 1 and data[i][1] != 1:
            if tree[data[i][1]][2] == 0:
                if tree[data[i][0]][0] == 0:
                    tree[data[i][0]][0] = data[i][1]
                else:
                    tree[data[i][0]][1] = data[i][1]
                tree[data[i][1]][2] = data[i][0]
            elif tree[data[i][1]][2]:
                if tree[data[i][1]][0] == 0:
                    tree[data[i][1]][0] = data[i][0]
                else:
                    tree[data[i][1]][1] = data[i][0]
                tree[data[i][0]][2] = data[i][1]
    # cnt = -1
    # for i in tree:
    #     cnt += 1
    #     print(cnt,i)
    # print()
    for i in range(2,N+1):
        print(tree[i][2])
    print()