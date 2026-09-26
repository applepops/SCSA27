
#[기본 세팅]
N, M, K = map(int, input().split())
tmp_arr = [list(map(int, input().split())) for _ in range (N)]
players_info = [[] for _ in range (M)]
players_dirs = [[] for _ in range (M)]
dead_players = [0] * M
arr_info = [[[] for _ in range (N)] for _ in range (N)]
turn = 0

didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range (N):
    for j in range (N):
        if tmp_arr[i][j] != 0:
            players_info[tmp_arr[i][j]-1].append(i)
            players_info[tmp_arr[i][j]-1].append(j)

tmp_lst = list(map(int, input().split()))
for t in range(len(tmp_lst)):
    players_info[t].append(tmp_lst[t]-1)

for m in range (M):
    ci, cj, cdir = players_info[m]
    arr_info[ci][cj] = [m, K]

for m in range (M):
    for _ in range (4):
        tmp_lst = list(map(lambda x: int(x) - 1, input().split()))
        players_dirs[m].append(tmp_lst)

###########################
#본격적인 시작이야..
while True:

    tmp_arr_info = [[[] for _ in range(N)] for _ in range(N)]

    turn += 1

    if turn >= 1000:
        turn = -1
        break

    #[이동]
    for m in range (M):
        if dead_players[m]:
            continue

        ci, cj, cdir = players_info[m]
        favor_dirs = players_dirs[m][cdir]

        for ndir in favor_dirs:
            ni, nj = didj[ndir][0] + ci, didj[ndir][1] + cj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            #빈칸이면
            if not arr_info[ni][nj]:
                tmp_arr_info[ni][nj].append([m, K+1])
                players_info[m][0], players_info[m][1], players_info[m][2] = ni, nj, ndir
                break
        #빈칸 못 찾았어.
        else:
            for nndir in favor_dirs:
                ni, nj = didj[nndir][0] + ci, didj[nndir][1] + cj
                if not (0 <= ni < N and 0 <= nj < N):
                    continue

                if arr_info[ni][nj][0] == m:
                    arr_info[ni][nj][1] = K+1
                    players_info[m][0], players_info[m][1], players_info[m][2] = ni, nj, nndir
                    break

    for i in range (N):
        for j in range (N):
            if tmp_arr_info[i][j]:
                arr_info[i][j] = tmp_arr_info[i][j][0]
                for player in range (1, len(tmp_arr_info[i][j])):
                    dead_players[tmp_arr_info[i][j][player][0]] = 1

    #[계약 턴수 줄어듦]
    for i in range (N):
        for j in range (N):
            if arr_info[i][j]:
                if arr_info[i][j][1] > 0:
                    arr_info[i][j][1] -= 1
                if arr_info[i][j][1] == 0:
                    arr_info[i][j] = []


    # [종료 조건 확인]
    if sum(dead_players) == M-1:
        break

print(turn)

