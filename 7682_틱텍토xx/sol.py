import sys
sys.stdin = open('input.txt')

dx = [1, 1, 1, 0]
dy = [0, 1, -1, 1]

while True:
    arr = [['']*3 for _ in range(3)]
    data = input()
    cnt = 0
    if data == 'end':
        break
    for i in range(3):
        for j in range(3):
            arr[i][j] = data[cnt]
            cnt += 1
    # for i in arr:
    #     print(i)
    # 9이면 통과 될 조건 만족하는지 보기
    if '.' not in data:
        if data.count('X') == 5 and data.count('O') == 4:
            print('valid')
        else:
            print('invalid')
    # 아니면 3개 연속 되는지 보기
    elif '.' in data:
        if data.count('X') - data.count('O') == 1:
            result = 0
            for x in range(3):
                for y in range(3):
                    for i in range(4):
                        count = 1
                        for j in range(1,3):
                            nx = x + dx[i] * j
                            ny = y + dy[i] * j
                            if 0 <= nx < 3 and 0 <= ny < 3 and arr[x][y] == 'X' and arr[x][y] == arr[nx][ny]:
                                count += 1
                                if count == 3:
                                    result += 1
            if result:
                print('valid')
            else:
                print('invalid')

        elif data.count('X') - data.count('O') == 0:
            X_result = 0
            O_result = 0
            for x in range(3):
                for y in range(3):
                    for i in range(4):
                        X_count = 1
                        O_count = 1
                        for j in range(1, 3):
                            nx = x + dx[i] * j
                            ny = y + dy[i] * j
                            if 0 <= nx < 3 and 0 <= ny < 3 and arr[x][y] in 'OX' and arr[x][y] == arr[nx][ny]:
                                if arr[x][y] == 'X':
                                    X_count += 1
                                    if X_count == 3:
                                        X_result += 1
                                elif arr[x][y] == 'O':
                                    O_count += 1
                                    if O_count == 3:
                                        O_result += 1
            if O_result:
                print('valid')
            elif X_result:
                print('invalid')
            else:
                print('invalid')
        else:
            print('invalid')