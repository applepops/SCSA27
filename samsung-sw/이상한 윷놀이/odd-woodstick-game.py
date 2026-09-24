N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]
horses_info = []
horses_in_arr = [[[] for _ in range (N)] for _ in range (N)]
turn = 0

didj = [(-1, 0), (0, -1), (1, 0), (0, 1)] #상좌하우

for k in range (K):
    x, y, d = map(int, input().split())
    x, y = x-1, y-1
    if d == 1:
        d = 3
    elif d == 2:
        d = 1
    elif d == 3:
        d = 0
    elif d == 4:
        d = 2
    horses_info.append([x, y, d])
    horses_in_arr[x][y].append(k)


while True:
    turn += 1
    is_end = False

    if turn > 1000:
        turn = -1
        break

    for k in range (K):

        ci, cj, cd = horses_info[k]
        ni, nj = ci + didj[cd][0], cj + didj[cd][1]

        if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == 2:
            cd = (cd + 2) % 4
            horses_info[k][2] = cd #방향 업데이트

        ni, nj = ci + didj[cd][0], cj + didj[cd][1]

        if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == 2:
            continue
        else:
            my_idx = horses_in_arr[ci][cj].index(k)
            my_hommies = horses_in_arr[ci][cj][my_idx:]
            horses_in_arr[ci][cj] = horses_in_arr[ci][cj][:my_idx]

            if arr[ni][nj] == 1:  # 빨강색인 경우
                my_hommies.reverse()

            horses_in_arr[ni][nj] += my_hommies
            for horse in my_hommies:
                horses_info[horse][0] = ni
                horses_info[horse][1] = nj

        if len(horses_in_arr[ni][nj]) >= 4:
            is_end = True

    if is_end:
        break

print(turn)