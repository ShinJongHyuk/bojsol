import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    A = a[1:]
    B = b[1:]
    A.sort()
    B.sort()
    while A and B and A[-1] == B[-1]:
        A.pop()
        B.pop()


    if A and B:
        if max(A) > max(B):
            print('A')
        else:
            print('B')
    elif A and not B:
        print('A')
    elif not A and B:
        print('B')
    elif not A and not B:
        print('D')
