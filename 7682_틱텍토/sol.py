import sys
sys.stdin = open('input.txt')

while True:
    arr = [['']*3 for _ in range(3)]
    data = input()
    cnt = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = data[cnt]
            cnt += 1
    if data == 'end':
        break
    # 9이면 통과 될 조건 만족하는지 보기
    if len(data) == 9:
        O_count = 0
        X_count = 0
        for i in data:
            if i == 'X':
                X_count += 1
            elif i == 'O':
                O_count += 1
        if X_count == 5 and O_count == 4:
            print('valid')
        else:
            print('invalid')
    # 아니면 3개 연속 되는지 보기
    else:
        pass