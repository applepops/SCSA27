from collections import deque

def bfs(si, sj, tnum):

    q = deque()
    q.append([si, sj])
    v[si][sj] = 1

    ijs = []
    lst = []

    while q:

        ci, cj = q.pop()
        ijs.append((ci, cj))
        lst.append(arr[ci][cj])
        team_num_arr[ci][cj] = tnum

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = 1

    team_ijs[tnum] = ijs[:]
    team_cur_state[tnum] = lst[:]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
team_num_arr = [[0] * N for _ in range (N)]

#[0] 기초 공사
team_ijs = [[] for _ in range (M+1)] #더미 주의
team_cur_state = [[] for _ in range (M+1)] #더미 주의


v = [[0] * N for _ in range (N)]
team_num = 1
for i in range (N):
    for j in range (N):
        if arr[i][j] != 0 and v[i][j] == 0:
            bfs(i, j, team_num)
            team_num += 1

for m in range (1, M+1):
    team_cur_state[m] = deque(team_cur_state[m])

for m in range (1, M+1):
    idx_1 = team_cur_state[m].index(1)
    num = 1
    cur_idx = idx_1
    if team_cur_state[m][(idx_1 - 1) % len(team_cur_state[m])] == 2:
        dir = -1
    else:
        dir = 1

    for _ in range(len(team_cur_state[m])-1):
        cur_idx = (cur_idx + dir) % len(team_cur_state[m])
        if team_cur_state[m][cur_idx] == 4:
            team_cur_state[m][cur_idx] = -1
        else:
            num += 1
            team_cur_state[m][cur_idx] = num


ans = [0] * M

for k in range (1, K+1):

    #[1] 이동하기
    for m in range (1, M+1):
        idx_1 = team_cur_state[m].index(1)
        if team_cur_state[m][(idx_1 + 1) % len(team_cur_state[m])] == 2:
            #반시계 방향
            team_cur_state[m].rotate(-1)
            pass
        else:
            #시계 방향
            team_cur_state[m].rotate(1)

    #도로 집어넣어주자.
    for m in range(1, M + 1):
        for member in range(len(team_cur_state[m])):
            ci, cj = team_ijs[m][member]
            arr[ci][cj] = team_cur_state[m][member]

    #[2] 공 던지기
    if k > 4*N:
        nk = k % (4*N)
    else:
        nk = k

    mi, mj = -1, -1
    if 1 <= nk <= N:
        for j in range (0, N):
            if 1 <= arr[nk-1][j]:
                mi, mj = nk-1, j
                break

    elif N+1 <= nk <= 2*N:
        nk = nk - N
        for i in range(N-1,-1,-1):
            if 1 <= arr[i][nk-1]:
                mi, mj = i, nk-1
                break

    elif 2*N+1 <= nk <= 3*N:
        nk = (5*N + 1) - nk
        nk = nk - (N * 2)
        for j in range (N-1, -1, -1):
            if 1 <= arr[nk-1][j]:
                mi, mj = nk-1, j
                break

    elif 3*N+1 <= nk <= 4*N:
        nk = (7 * N + 1) - nk
        nk = nk - (N * 3)
        for i in range(0, N):
            if 1 <= arr[i][nk - 1]:
                mi, mj = i, nk - 1
                break
        #nk가 0이다.
    else:
        for i in range(0, N):
            if 1 <= arr[i][0]:
                mi, mj = i, 0
                break

    #공을 맞은 팀이 없음.
    if (mi, mj) == (-1, -1):
        continue

    #공 맞은 팀 있음.
    # [3] 답 더해주기
    cur_team_num = team_num_arr[mi][mj]
    idx_my = team_ijs[cur_team_num].index((mi, mj))

    ans[cur_team_num-1] += team_cur_state[cur_team_num][idx_my] ** 2

    #[4] 머리사람과 꼬리사람 바꾸기
    max_num = max(team_cur_state[cur_team_num])
    for member in range(len(team_cur_state[cur_team_num])):
        if team_cur_state[cur_team_num][member] != -1:
            team_cur_state[cur_team_num][member ]= max_num - team_cur_state[cur_team_num][member] + 1


    #도로 집어넣어주자.
    for member in range(len(team_cur_state[cur_team_num])):
        ci, cj = team_ijs[cur_team_num][member]
        arr[ci][cj] = team_cur_state[cur_team_num][member]

print(sum(ans))