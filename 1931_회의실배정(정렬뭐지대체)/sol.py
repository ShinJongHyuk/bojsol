import sys
sys.stdin = open('input.txt')

N = int(input())
data = []

for _ in range(N):
    A = list(map(int,input().split()))
    data.append(A)
data.sort(key=lambda x : (x[1], x[0]))
result = 1
x = data[0][0]
y = data[0][1]

for i in range(1,N):
    if y <= data[i][0]:
        x = data[i][0]
        y = data[i][1]
        result += 1
print(result)



