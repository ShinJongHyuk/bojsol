import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start):
    queue = deque([])
    queue.append(start)
    visited = [0] * (N + 1)
    while queue:
        start = queue.popleft()
        if start == N:
            return visited
        if visited[start] == 0:
            visited[start] = 1

        for next in range(1,N+1):
            if data[start][next]:
                queue.append(next)
                visited[next] = visited[start] + 1

    return

N, M = map(int,input().split())

data = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    data[A][B] = 1
    # data[B][A] = 1


print(BFS(1))