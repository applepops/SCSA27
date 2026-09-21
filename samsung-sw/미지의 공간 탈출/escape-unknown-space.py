from pprint import pprint
didj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def return_arr(num):

    if num == 11:
        return arr11
    elif num == 12:
        return arr12
    elif num == 13:
        return arr13
    elif num == 14:
        return arr14
    elif num == 15:
        return arr15
    elif num == 16:
        return arr16

def return_visited(num):

    if num == 11:
        return visited11
    elif num == 12:
        return visited12
    elif num == 13:
        return visited13
    elif num == 14:
        return visited14
    elif num == 15:
        return visited15
    elif num == 16:
        return visited16

def move(ci, cj, now_arr, now_arr_num, now_d):

    global si, sj, ei, ej

    ni, nj = ci + didj[now_d][0], cj + didj[now_d][1]

    if len(now_arr) == M: #시간의 벽
        if 0 <= ni < M and 0 <= nj < M: #같은 arr내 움직임
            return ni, nj, now_arr, now_arr_num, now_d
        else: #다른 arr로 이동하는 거다.
            if now_arr_num == 11:
                if ni == M:
                    now_arr_num = 12
                    ni = 0
                    nj = cj
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif ni == -1:
                    now_arr_num = 13
                    ni = 0
                    nj = M-cj-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == -1:
                    now_arr_num = 14
                    ni = 0
                    nj = ci
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == M:
                    now_arr_num = 15
                    ni = 0
                    nj = M-ci-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
            elif now_arr_num == 12:
                if ni == -1:
                    now_arr_num = 11
                    ni = M-1
                    nj = cj
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == -1:
                    now_arr_num = 14
                    ni = ci
                    nj = M-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == M:
                    now_arr_num = 15
                    ni = ci
                    nj = 0
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif ni == M:
                    now_arr_num = 16
                    ni = ei
                    nj = cj + sj
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
            elif now_arr_num == 13:
                if ni == -1:
                    now_arr_num = 11
                    ni = 0
                    nj = M-cj-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == -1:
                    now_arr_num = 15
                    ni = ci
                    nj = M-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == M:
                    now_arr_num = 14
                    ni = ci
                    nj = 0
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif ni == M:
                    now_arr_num = 16
                    ni = si -1
                    nj = sj + M -cj -1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
            elif now_arr_num == 14:
                if ni == -1:
                    now_arr_num = 11
                    ni = cj
                    nj = 0
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == -1:
                    now_arr_num = 13
                    ni = ci
                    nj = M-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == M:
                    now_arr_num = 12
                    ni = ci
                    nj = 0
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif ni == M:
                    now_arr_num = 16
                    ni = si + cj
                    nj = sj-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
            elif now_arr_num == 15:
                if ni == -1:
                    now_arr_num = 11
                    ni = cj
                    nj = M-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == M:
                    now_arr_num = 13
                    ni = ci
                    nj = 0
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif nj == -1:
                    now_arr_num = 12
                    ni = ci
                    nj = M-1
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif ni == M:
                    now_arr_num = 16
                    ni = ei - 1 - cj
                    nj = ej
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d


    else: #평면
        if 0 <= ni < N and 0 <= nj < N: #같은 arr내 움직임
            if now_arr[ni][nj] != 3: #시간의 벽으로 가는 게 아님
                return ni, nj, now_arr, now_arr_num, now_d
            else: #시간의 벽으로 간다.... (3)인 것이다.
                if now_d == 3 and ni == ei-1:
                    now_arr_num = 12
                    ni = M-1
                    nj = cj - sj
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif now_d == 2 and ni == si:
                    now_arr_num = 13
                    ni = M-1
                    nj = M - 1 - (cj - sj)
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif now_d == 0 and nj == sj:
                    now_arr_num = 14
                    ni = M-1
                    nj = ci - si
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d
                elif now_d == 1 and nj == ej -1:
                    now_arr_num = 15
                    ni = M-1
                    nj = ei - 1 - ci
                    return ni, nj, return_arr(now_arr_num), now_arr_num, now_d

        else: #아예 격자를 벗어남. 못 간다.
            return -1, -1, now_arr, now_arr_num, now_d

    pass

def find_se():
    for i in range(N):
        for j in range(N):
            if arr16[i][j] == 3:
                si, sj = i, j
                ei, ej = i + M, j + M
                return si, sj, ei, ej


N, M, F = map(int, input().split())
arr16 = [list(map(int, input().split())) for _ in range (N)]
arr15 = [list(map(int, input().split())) for _ in range (M)] #오
arr14 = [list(map(int, input().split())) for _ in range (M)] #왼
arr12 = [list(map(int, input().split())) for _ in range (M)] #앞
arr13 = [list(map(int, input().split())) for _ in range (M)] #뒷
arr11 = [list(map(int, input().split())) for _ in range (M)] #위

visited16 = [[0] * N for _ in range (N)]
visited15 = [[0] * M for _ in range (M)]
visited14 = [[0] * M for _ in range (M)]
visited12 = [[0] * M for _ in range (M)]
visited13 = [[0] * M for _ in range (M)]
visited11 = [[0] * M for _ in range (M)]


#타임머신 위치 찾기
tm_i, tm_j = -1, -1
for i in range (M):
    for j in range (M):
        if arr11[i][j] == 2:
            tm_i, tm_j = i, j

time_machine_ijs = []
time_machine_ijs.append([tm_i, tm_j, 11])
visited11[tm_i][tm_j] = 1

goal_i, goal_j = -1, -1
for i in range (N):
    for j in range (N):
        if arr16[i][j] == 4:
            goal_i, goal_j = i, j

time_wrong_points = []
for _ in range (F):
    r, c, d, v = map(int, input().split())
    time_wrong_points.append([r, c, d, v, 16]) #마지막에 있는 arr 번호 추가해서 적어줬음.
    arr16[r][c] = 9

si, sj, ei, ej = find_se()
# print(si, sj, ei, ej)
#단위테스팅 드가자...
# print(move(4, 1, arr16, 16, 0))

#지금 코드는 다른 arr로 이동할 때 그곳에서의 장애물 / 시간 이상 현상을 피하지는 않고 있음
#나중에 수정 필요함.

ans = 0
is_found = False
while True:
    ans += 1
    # print(f"{ans}번째")

    #시간 이상 현상이 움직인다.
    new_time_wrong_points = []
    for r, c, d, v, arr_n in time_wrong_points:
        if ans % v == 0: #이동되면 새로 갱신을 하는 거고
            nr, nc, now_arr, n_arr_n, n_d = move(r, c, return_arr(arr_n), arr_n, d)
            if now_arr[nr][nc] == 0: #이제야 장애물 확인함.
                now_arr[nr][nc] = 9
                new_time_wrong_points.append([nr, nc, n_d, v, n_arr_n])
        else: #차례가 아니면 기다리는 거고..
            new_time_wrong_points.append([r, c, d, v, arr_n])

    time_wrong_points = new_time_wrong_points


    #타임머신이 움직인다.
    new_time_machine_ijs = []
    for i in range (len(time_machine_ijs)):
        for d in [0, 1, 2, 3]:
            nr, nc, now_arr, n_arr_n, n_d = move(time_machine_ijs[i][0], time_machine_ijs[i][1], return_arr(time_machine_ijs[i][2]), time_machine_ijs[i][2], d)

            # print(f"{time_machine_ijs[i][0], time_machine_ijs[i][1], time_machine_ijs[i][2]}에서 넘어감.")
            # print(nr, nc, n_arr_n)

            if (nr, nc, n_arr_n) == (goal_i, goal_j, 16):
                is_found = True

            if (nr, nc) == (-1, -1):
                continue

            if 0 <= nr < len(now_arr) and 0 <= nc < len(now_arr) and now_arr[nr][nc] == 0 and return_visited(n_arr_n)[nr][nc] == 0: #장애물 확인 및 안 가본 곳인지 확인.
                return_visited(n_arr_n)[nr][nc] = 1
                new_time_machine_ijs.append([nr, nc, n_arr_n])
    time_machine_ijs = new_time_machine_ijs

    if not time_machine_ijs:
        break

    # pprint(visited16)

    if is_found:
        break

if is_found:
    print(ans)
else:
    print(-1)

