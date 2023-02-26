import sys
sys.stdin = open('input,.txt')

N = int(input())
data = [0] + list(map(int,input().split()))
T = int(input())

for _ in range(T):
    a, b = map(int,input().split())
    if a == 1:
        for i in range(b,len(data),b):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0

    elif a == 2:
        cnt = 1
        while b + cnt < len(data) and 0 < b - cnt < len(data):
            if data[b + cnt] == data[b - cnt]:
                if data[b - cnt] == 0:
                    data[b - cnt] = 1
                    data[b + cnt] = 1
                else:
                    data[b - cnt] = 0
                    data[b + cnt] = 0
                cnt += 1
            else:
                break
        if data[b] == 0:
            data[b] = 1
            data[b] = 1
        else:
            data[b] = 0
            data[b] = 0
result = [0] * 101
for i in range(1,len(data)):
    result[i-1] = data[i]
for i in range(N):
    if i != 0 and (i % 20) == 0:
        print()
    print(result[i], end=' ')