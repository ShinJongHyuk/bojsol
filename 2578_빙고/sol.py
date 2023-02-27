import sys
sys.stdin = open('input.txt')

bingo = []

for _ in range(5):
    bingo.append(list(map(int,input().split())))

data = [list(map(int,input().split())) for _ in range(5)]
for i in range(3):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if data[i][j] == bingo[k][l]:
                    bingo[k][l] = 0


result = []
cnt = 0
for a in range(5):
    for b in range(5):
        if bingo[a][b] == 0:
            cnt += 1
            if cnt == 5:
                result.append(cnt)
cnt = 0
for a in range(5):
    for b in range(5):
        if bingo[b][a] == 0:
            cnt += 1
            if cnt == 5:
                result.append(cnt)
cnt = 0
for a in range(5):
    if bingo[a][a] == 0:
        cnt += 1
        if cnt == 5:
            result.append(cnt)

cnt = 0
for a in range(5):
    if bingo[a][-a-1] == 0:
        cnt += 1
        if cnt == 5:
            result.append(cnt)
if

print(result)