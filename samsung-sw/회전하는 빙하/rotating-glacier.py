from collections import deque

def get_start_ijs(level):
    ijs = []

    for i in range (0, 2**N, 2**level):
        for j in range (0, 2**N, 2**level):
            ijs.append([i, j])

    return ijs

def rotate(level, si, sj):

    #얘네가 진짜 돌리는 좌측 상단 지점들.
    new_ij = []
    for i in range (si, si + 2**level, 2**(level-1)):
        for j in range(sj, sj + 2 ** level, 2 ** (level - 1)):
            new_ij.append([i, j])

    tmp_arr1 = [row[new_ij[0][1]:new_ij[0][1]+2 ** (level - 1)] for row in arr[new_ij[0][0]:new_ij[0][0]+2 ** (level - 1)]]
    tmp_arr2 = [row[new_ij[1][1]:new_ij[1][1] + 2 ** (level - 1)] for row in arr[new_ij[1][0]:new_ij[1][0] + 2 ** (level - 1)]]
    tmp_arr3 = [row[new_ij[2][1]:new_ij[2][1] + 2 ** (level - 1)] for row in
                arr[new_ij[2][0]:new_ij[2][0] + 2 ** (level - 1)]]
    tmp_arr4 = [row[new_ij[3][1]:new_ij[3][1] + 2 ** (level - 1)] for row in
                arr[new_ij[3][0]:new_ij[3][0] + 2 ** (level - 1)]]

    tmp_tmp = [row[:] for row in tmp_arr2[:]]
    tmp_arr2 = [row[:] for row in tmp_arr1[:]]
    tmp_arr1 = [row[:] for row in tmp_arr3[:]]
    tmp_arr3 = [row[:] for row in tmp_arr4[:]]
    tmp_arr4 = tmp_tmp

    for i in range (new_ij[0][0], new_ij[0][0]+2 ** (level - 1)):
        for j in range (new_ij[0][1], new_ij[0][1]+2 ** (level - 1)):
            arr[i][j] = tmp_arr1[i-new_ij[0][0]][j-new_ij[0][1]]

    for i in range (new_ij[1][0], new_ij[1][0]+2 ** (level - 1)):
        for j in range (new_ij[1][1], new_ij[1][1]+2 ** (level - 1)):
            arr[i][j] = tmp_arr2[i-new_ij[1][0]][j-new_ij[1][1]]

    for i in range (new_ij[2][0], new_ij[2][0]+2 ** (level - 1)):
        for j in range (new_ij[2][1], new_ij[2][1]+2 ** (level - 1)):
            arr[i][j] = tmp_arr3[i-new_ij[2][0]][j-new_ij[2][1]]

    for i in range (new_ij[3][0], new_ij[3][0]+2 ** (level - 1)):
        for j in range (new_ij[3][1], new_ij[3][1]+2 ** (level - 1)):
            arr[i][j] = tmp_arr4[i-new_ij[3][0]][j-new_ij[3][1]]



def bfs(i, j):
    q = deque()
    q.append([i, j])
    ice_cnt = 0

    while q:
        ci, cj = q.popleft()
        ice_cnt += 1
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < 2**N and 0 <= nj < 2**N and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return ice_cnt


N, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (2**N)]
level_lst = list(map(int, input().split()))

for cur_level in level_lst:
    if cur_level != 0:
        start_ijs = get_start_ijs(cur_level)
        for i, j in start_ijs:
            rotate(cur_level, i, j)

    #녹는다.
    melted_ice = [[0] * 2**N for _ in range (2**N)]
    for i in range (2**N):
        for j in range (2**N):
            cnt = 0
            for di, dj in ((-1, 0),(1, 0), (0, 1), (0, -1)):
                ni = di + i
                nj = dj + j
                if 0 <= ni < 2**N and 0 <= nj < 2**N and arr[ni][nj] != 0:
                    cnt += 1

            if cnt >= 3:
                continue
            else:
                melted_ice[i][j] += 1

    for i in range(2 ** N):
        for j in range(2 ** N):
            arr[i][j] -= melted_ice[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

ans_cnt = 0
visited = [[0] * 2**N for _ in range (2**N)]
for i in range(2 ** N):
    for j in range(2 ** N):
        if visited[i][j] == 0 and arr[i][j] != 0:
            visited[i][j] = 1
            res = bfs(i, j)
            ans_cnt = max(res, ans_cnt)

print(sum(map(sum, arr)))
print(ans_cnt)