from collections import deque

def check_office():
    for i, j in office_ijs:
        if wind_info[i][j] < K:
            return False
    else:
        return True


def go_wind():

    for si, sj, d in aircon_ijs:

        q = deque()
        ssi, ssj = didj[d][0] + si, didj[d][1] + sj
        q.append([ssi, ssj, 5])

        visited = [[0] * N for _ in range (N)]
        visited[ssi][ssj] = 1
        wind_info[ssi][ssj] += 5

        while q:
            ci, cj, cd = q.popleft()

            if cd == 0:
                break

            #그냥 내 방향으로 가는 거
            ni = ci + didj[d][0]
            nj = cj + didj[d][1]

            if 0 <= ni < N and 0 <= nj < N and wall_info[ci][cj][d] == 0 and visited[ni][nj] == 0:
                q.append([ni, nj, cd-1])
                visited[ni][nj] = 1
                wind_info[ni][nj] += cd -1

            #옆 한쪽 확인하고 내 방향 가는 거
            ni = ci + didj[(d-1)%4][0]
            nj = cj + didj[(d-1)%4][1]
            if 0 <= ni < N and 0 <= nj < N and wall_info[ci][cj][(d-1)%4] == 0:
                nni = ni + didj[d][0]
                nnj = nj + didj[d][1]
                if 0 <= nni < N and 0 <= nnj < N and wall_info[ni][nj][d] == 0 and visited[nni][nnj] == 0:
                    q.append([nni, nnj, cd-1])
                    visited[nni][nnj] = 1
                    wind_info[nni][nnj] += cd - 1

            #다른 옆 한쪽 확인하고 내 방향 가는 거
            ni = ci + didj[(d+1)%4][0]
            nj = cj + didj[(d+1)%4][1]
            if 0 <= ni < N and 0 <= nj < N and wall_info[ci][cj][(d+1)%4] == 0:
                nni = ni + didj[d][0]
                nnj = nj + didj[d][1]
                if 0 <= nni < N and 0 <= nnj < N and wall_info[ni][nj][d] == 0 and visited[nni][nnj] == 0:
                    q.append([nni, nnj, cd-1])
                    visited[nni][nnj] = 1
                    wind_info[nni][nnj] += cd - 1


def mix_wind():

    tmp_wind = [[0] * N for _ in range (N)]

    for i in range (N):
        for j in range (N):
            for d in range (0, 4):
                ni = i + didj[d][0]
                nj = j + didj[d][1]

                if 0 <= ni < N and 0 <= nj < N and wall_info[i][j][d] == 0:
                    if wind_info[i][j] > wind_info[ni][nj]:
                        gap = (wind_info[i][j] - wind_info[ni][nj]) // 4
                        tmp_wind[i][j] -= gap
                        tmp_wind[ni][nj] += gap

    for i in range(N):
        for j in range(N):
            wind_info[i][j] += tmp_wind[i][j]

N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range (N)]
office_ijs = []
aircon_ijs = []
turn = 0

didj = [(-1, 0), (0, -1), (1, 0), (0, 1)] #위왼아래오

for i in range (N):
    for j in range (N):
        if input_arr[i][j] == 1:
            office_ijs.append([i, j])
        elif input_arr[i][j] == 2:
            aircon_ijs.append([i, j, 1])
        elif input_arr[i][j] == 3:
            aircon_ijs.append([i, j, 0])
        elif input_arr[i][j] == 4:
            aircon_ijs.append([i, j, 3])
        elif input_arr[i][j] == 5:
            aircon_ijs.append([i, j, 2])

wall_info = [[[0, 0, 0, 0] for _ in range (N)] for _ in range (N)]
wind_info = [[0] * N for _ in range (N)]

#벽 추가로 만들기
for _ in range (M):
    x, y, where = map(int, input().split())
    x, y = x-1, y-1

    wall_info[x][y][where] = 1

    if 0 <= x-1 < N and 0 <= y < N and where == 0:
        wall_info[x-1][y][2] = 1

    if 0 <= x < N and 0 <= y-1 < N and where == 1:
        wall_info[x][y-1][3] = 1


while True:

    if check_office():
        break

    turn += 1

    if turn > 100:
        turn = -1
        break

    go_wind()
    mix_wind()
    #외벽감소
    for i in range (0, N):
        if wind_info[i][0] > 0:
            wind_info[i][0] -= 1
        if wind_info[i][N-1] > 0:
            wind_info[i][N-1] -= 1
    for j in range (1, N-1):
        if wind_info[0][j] > 0:
            wind_info[0][j] -= 1
        if wind_info[N-1][j] > 0:
            wind_info[N-1][j] -= 1


print(turn)