from collections import deque

def spread_meonji(start_i, start_j):

    # 먼지가 있기는 하다면..
    if arr[start_i][start_j] > 0:
        temp = arr[start_i][start_j] // 5

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = start_i + di
            nj = start_j + dj

            #방의 범위를 벗어나지 않고, 이동하려는 방향에 시공의 돌풍이 없으면
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1:

                    adding_meonji[ni][nj] += temp
                    arr[start_i][start_j] -= temp


#행, 열, 시간
N, M, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]

wind_location = []
for i in range (N):
    if arr[i][0] == -1:
        wind_location.append((i, 0))

#t초 동안 반복한다.
for _ in range (t):

    #나중에 돌면서 더해주어야 하는 먼지들을 담는 배열
    adding_meonji = [[0] * M for _ in range (N)]

    #1. 먼지의 확산
    for i in range (N):
        for j in range (M):
            #시공의 돌풍이 아니라면
            if arr[i][j] != -1:
                spread_meonji(i, j)

    #먼지 한꺼번에 확산 시켜주기
    for i in range (N):
        for j in range (M):
            if arr[i][j] != -1:
                arr[i][j] += adding_meonji[i][j]

    #2. 시공의 돌풍의 청소
    up_wind_meonjis = deque()


    #반시계방향으로 도는 놈 우측으로
    for i in range (1, M-1):
        up_wind_meonjis.append(arr[wind_location[0][0]][i])
    # 윗쪽으로
    for i in range (wind_location[0][0], 0, -1):
        up_wind_meonjis.append(arr[i][M-1])
    # 좌측으로
    for i in range (M-1, 0, -1):
        up_wind_meonjis.append(arr[0][i])
    #아랫쪽으로
    for i in range (0, wind_location[0][0]):
        up_wind_meonjis.append(arr[i][0])

    up_wind_meonjis.appendleft(0)
    up_wind_meonjis.pop()

    for i in range (1, M-1):
        temp = up_wind_meonjis.popleft()
        arr[wind_location[0][0]][i] = temp

    # 윗쪽으로
    for i in range (wind_location[0][0], 0, -1):
        temp = up_wind_meonjis.popleft()
        arr[i][M-1] = temp
    # 좌측으로
    for i in range (M-1, 0, -1):
        temp = up_wind_meonjis.popleft()
        arr[0][i] = temp
    #아랫쪽으로
    for i in range (0, wind_location[0][0]):
        temp = up_wind_meonjis.popleft()
        arr[i][0] = temp

    down_wind_meonjis = deque()

    #시계방향으로 도는 놈 우측으로
    for i in range (1, M-1):
        down_wind_meonjis.append(arr[wind_location[1][0]][i])
    # 아랫쪽으로
    for i in range (wind_location[1][0], N-1):
        down_wind_meonjis.append(arr[i][M-1])
    # 왼측으로
    for i in range (M-1, 0, -1):
        down_wind_meonjis.append(arr[N-1][i])
    # 윗쪽으로
    for i in range (N-1, wind_location[1][0], -1):
        down_wind_meonjis.append(arr[i][0])

    down_wind_meonjis.appendleft(0)
    down_wind_meonjis.pop()

    #시계방향으로 도는 놈 우측으로
    for i in range (1, M-1):
        temp = down_wind_meonjis.popleft()
        arr[wind_location[1][0]][i] = temp
    # 아랫쪽으로
    for i in range (wind_location[1][0], N-1):
        temp = down_wind_meonjis.popleft()
        arr[i][M-1] = temp
    # 왼측으로
    for i in range (M-1, 0, -1):
        temp = down_wind_meonjis.popleft()
        arr[N-1][i] = temp
    # 윗쪽으로
    for i in range (N-1, wind_location[1][0], -1):
        temp = down_wind_meonjis.popleft()
        arr[i][0] = temp

cnt = 0
for i in range (N):
    for j in range (M):
        if arr[i][j] != -1:
            cnt += arr[i][j]

print(cnt)