import sys
sys.stdin = open('input.txt')
from itertools import  permutations

N = int(input())
K = int(input())
card = []
result = []
for _ in range(N):
    card.append(input())
for i in permutations(card,K):
    result.append(''.join(i))

result2 = set(result)
print(len(result2))

