import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    word = input()
    p = input()
    stack = []
    for char in word:
        stack.append(char)
        if stack[]