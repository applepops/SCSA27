from collections import deque

def get_M_way(si, sj, ei, ej):

    q = deque()
    q.append([si, sj])

    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    is_reachable = False

    parents = [[[] for _ in range (N)] for _ in range (N)]

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            is_reachable = True
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj]==0:
                q.append([ni, nj])
                visited[ni][nj] = 1
                parents[ni][nj] = [ci, cj]

    if is_reachable:
        ways = []
        ci, cj = ei, ej
        while (ci, cj) != (si, sj):
            ways.append([ci, cj])
            ci, cj = parents[ci][cj]

        ways.reverse()
        return ways
    else:
        return -1

def freeze(d, si, sj):
    q = deque()
    q.append([si, sj, 'M'])

    rocked_cnt = 0

    v = [[0] * N for _ in range (N)]
    v[si][sj] = 0

    while q:
        ci, cj, who = q.popleft()

        if who == 'M':
            for dd in (d, (d+1)%8, (d-1)%8):
                ni = ci + didj[dd][0]
                nj = cj + didj[dd][1]

                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                    if len(cur_state[ni][nj]):
                        q.append([ni, nj, 'W'])
                        v[ni][nj] = 1
                    else:
                        q.append([ni, nj, 'M'])
                        v[ni][nj] = 1

        elif who == 'W':
            d_lst = []
            if d == 0:
                if sj == cj:
                    d_lst = [d]
                elif sj < cj:
                    d_lst = [d, (d + 1) % 8]
                elif sj > cj:
                    d_lst = [d, (d - 1) % 8]
            elif d == 2:
                if si == ci:
                    d_lst = [d]
                elif si < ci:
                    d_lst = [d, (d + 1) % 8]
                elif si > ci:
                    d_lst = [d, (d - 1) % 8]
            elif d == 4:
                if sj == cj:
                    d_lst = [d]
                elif sj < cj:
                    d_lst = [d, (d - 1) % 8]
                elif sj > cj:
                    d_lst = [d, (d + 1) % 8]
            elif d == 6:
                if si == ci:
                    d_lst = [d]
                elif si < ci:
                    d_lst = [d, (d - 1) % 8]
                elif si > ci:
                    d_lst = [d, (d + 1) % 8]

            for dd in d_lst:
                ni = ci + didj[dd][0]
                nj = cj + didj[dd][1]

                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] <= 1:
                    q.append([ni, nj, 'W'])
                    v[ni][nj] = 2

    # print()
    # for row in v:
    #     print(*row)

    # 돌 된 애들 세기
    for i, j in warriors_ijs.values():
        if v[i][j] == 1:
            rocked_cnt += 1

    return rocked_cnt, d, v

def change_dir(d):
    if d == 0:
        return 0
    elif d == 2:
        return 6
    elif d == 4:
        return 2
    elif d == 6:
        return 4

def cal_distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

didj = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M = map(int, input().split())
Msi, Msj, Mei, Mej = map(int, input().split())
warriors_ijs = dict()
cur_state = [[[] for _ in range (N)] for _ in range (N)]

tmp_lst = list(map(int, input().split()))
for m in range (1, M+1):
    warriors_ijs[m] = tmp_lst[:2]
    tmp_lst = tmp_lst[2:]

arr = [list(map(int, input().split())) for _ in range (N)]
ways = get_M_way(Msi, Msj, Mei, Mej)

#현재 상태 표시하기 (전사들)
for w in warriors_ijs.keys():
    i, j = warriors_ijs[w]
    cur_state[i][j].append(w)

# for row in cur_state:
#     print(*row)

#메두사가 갈 길이 없음.
if ways == -1:
    print(-1)
else:
    for i, j in ways:

        total_distance = 0
        rock_cnt = 0
        attacked_cnt = 0

        #메두사 이동함
        Mci, Mcj = i, j
        # print(Mci, Mcj)

        if (Mci, Mcj) == (Mei, Mej):
            print(0)
            break

        #이동한 곳에 전사가 있다면
        if len(cur_state[Mci][Mcj]):
            d_lst = cur_state[Mci][Mcj]
            cur_state[Mci][Mcj] = []
            for d in d_lst:
                warriors_ijs.pop(d)

        hubo = []
        for d in (0, 2, 4, 6):
            cnt, d, v = freeze(d, Mci, Mcj)
            d = change_dir(d)
            hubo.append([cnt, d, v])

        hubo = sorted(hubo, key=lambda x:(-x[0], x[1]))

        rock_cnt += hubo[0][0]
        v = hubo[0][2]

        movable_w_lst = []
        for w in warriors_ijs.keys():
            i, j = warriors_ijs[w]
            if v[i][j] != 1:
                movable_w_lst.append(w)

        # print()
        # print(movable_w_lst)
        #
        # print()
        # for row in v:
        #     print(*row)


        for w in movable_w_lst:
            ci, cj = warriors_ijs[w]
            cur_d = cal_distance(ci, cj, Mci, Mcj)

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): #상하좌으
                ni = ci + di
                nj = cj + dj
                next_d = cal_distance(ni, nj, Mci, Mcj)

                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != 1 and cur_d > next_d:
                    ci, cj = ni, nj #갱신
                    warriors_ijs[w] = [ci, cj]
                    total_distance += 1
                    break
            #다 돌았는데 못 감.
            else:
                continue

            cur_d = cal_distance(ci, cj, Mci, Mcj)
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):  # 좌우상하
                ni = ci + di
                nj = cj + dj
                next_d = cal_distance(ni, nj, Mci, Mcj)

                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != 1 and cur_d > next_d:
                    ci, cj = ni, nj  # 갱신
                    warriors_ijs[w] = [ci, cj]
                    total_distance += 1
                    break
            # 다 돌았는데 못 감.
            else:
                continue

        new_cur_state = [[[] for _ in range (N)] for _ in range (N)]
        # 현재 상태 표시하기 (전사들)
        for w in warriors_ijs.keys():
            i, j = warriors_ijs[w]
            new_cur_state[i][j].append(w)

        cur_state = new_cur_state

        if len(cur_state[Mci][Mcj]):
            attacked_cnt += len(cur_state[Mci][Mcj])
            d_lst = cur_state[Mci][Mcj]
            cur_state[Mci][Mcj] = []
            for d in d_lst:
                warriors_ijs.pop(d)

        # for row in cur_state:
        #     print(*row)


        print(total_distance, rock_cnt, attacked_cnt)






