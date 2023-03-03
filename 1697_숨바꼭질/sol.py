import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int,input().split())
second = [0] * 100001

def BFS(start):
    queue = deque([])
    queue.append(start)

    while queue:
        start = queue.popleft()
        if start == K:
            return second[start]

        for i in (start-1, start+1, start*2):
            if 0 <= i <= 100000 and second[i] == 0:
                second[i] = second[start] + 1
                queue.append(i)
print(BFS(N))