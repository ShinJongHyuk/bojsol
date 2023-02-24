import sys
sys.stdin = open('input.txt')

def DFS(S):
    global result
    stack = [S]
    visited = [0] * 24
    while stack:
        start = stack.pop()

        if visited[start] == 0:
            visited[start] = 1
        for next in range(24):
            if data[start][next] and not visited[next]:
                visited[next] = visited[start] + 1
                stack.append(next)
    return max(visited)



N = int(input())

data = [[0] * 24 for _ in range(24)]

stack = []
visit = []
result = []
for _ in range(N):
    x, y = map(int,input().split())
    data[x][y] += 1
    visit.append(x)
print(visit)
for i in visit:
    x = DFS(i)
    result.append(x)
print(result)
print(max(result))
