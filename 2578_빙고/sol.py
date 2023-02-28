import sys
sys.stdin = open('input.txt')

bingo = []

for _ in range(5):
    bingo.append(list(map(int,input().split())))
result = []
data = [list(map(int,input().split())) for _ in range(5)]
for i in range(3):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if data[i][j] == bingo[k][l]:
                    bingo[k][l] = 0


