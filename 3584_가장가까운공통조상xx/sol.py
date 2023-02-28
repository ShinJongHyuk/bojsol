import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    result = []
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N-1):
        p, c = map(int,input().split())

        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    x,y = map(int,input().split())
    x_list = [x]
    y_list = [y]

    while x != 0:
        p1 = tree[x][2]
        x_list.append(p1)
        x = p1


    while y != 0:
        p2 = tree[y][2]
        y_list.append(p2)
        y = p2
    # print(x_list,y_list)
    result = []
    for i in x_list:
        for j in y_list:
            if i == j:
                result.append(i)
    print(result[0])