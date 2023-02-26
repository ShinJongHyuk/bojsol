import sys
sys.stdin = open('input.txt')
N = int(input())
result = []
def cal(S):
    value = [N,S]
    while True:
        x = value[-2]
        y = value[-1]
        v = x - y
        value.append(v)
        if v < 0:
            value.pop()
            return value

for i in range(1,N+1):
    result.append(cal(i))


maxV = 0
maxV_idx = 0
for i in range(len(result)):
    if len(result[i]) > maxV:
        maxV = len(result[i])
        maxV_idx = i
print(maxV)
print(*result[maxV_idx])
