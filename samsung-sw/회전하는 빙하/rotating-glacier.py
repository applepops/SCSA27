from collections import deque

def print_cur_arr(my_arr):
    for row in my_arr:
        print(*row)

def bfs(si, sj):
    global max_iceberg

    tmp_iceberg = 0

    q = deque()
    q.append((si, sj))

    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        tmp_iceberg += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N:
                if visited[ni][nj] == 0 and arr[ni][nj] != 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

    max_iceberg = max(max_iceberg, tmp_iceberg)


#level에 맞게 작은 배열로 쪼개는 함수
def rotate_by_level(ci, cj, cur_level):

    #원본 배열 copy
    tmp_arr = [row[:] for row in arr]

    temp_lst = []

    for i in range (ci, ci+2**cur_level, cur_level):
        for j in range (cj, cj+2**cur_level, cur_level):
            #단위 안에 있는 작은 회전해야 하는 애들이 시작하는 꼭짓점
            temp_lst.append([i, j])

    for i in range (len(temp_lst)):
        mini_arr = [row[temp_lst[i][1]:temp_lst[i][1]+cur_level] for row in tmp_arr[temp_lst[i][0]:temp_lst[i][0]+cur_level]]
        if i == 0:
            new_i = 1
        elif i == 1:
            new_i = 3
        elif i == 2:
            new_i = 0
        elif i == 3:
            new_i = 2

        #돌려주기
        for p in range (temp_lst[new_i][0],temp_lst[new_i][0]+cur_level):
            for q in range (temp_lst[new_i][1], temp_lst[new_i][1]+cur_level):
                arr[p][q] = mini_arr[p-temp_lst[new_i][0]][q-temp_lst[new_i][1]]



#인자로 받는 것은 level
def find_start_point(cur_level):
    if cur_level == 0:
        return 0

    #i와 j는 rotate를 할 시작지점이 되는 거다.
    for i in range (0, 2**N, 2**cur_level):
        for j in range (0, 2**N, 2**cur_level):
            rotate_by_level(i, j, cur_level)


def melt():

    need_to_melt = [[0] * (2**N) for _ in range (2**N)]

    for i in range (2**N):
        for j in range (2**N):

            if arr[i][j] == 0:
                continue

            cur_cnt = 0

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = di + i
                nj = dj + j

                if 0 <= ni < 2**N and 0 <= nj < 2**N and arr[ni][nj] != 0:
                    cur_cnt += 1

            if cur_cnt >= 3:
                continue
            else:
                need_to_melt[i][j] = 1


    #녹이기
    for i in range(2 ** N):
        for j in range(2 ** N):
            if need_to_melt[i][j] == 1:
                arr[i][j] -= 1


#회전 가능 레벨 N, Q는 회전횟수
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (2**N)]

rotate_levels = list(map(int, input().split()))

for rl in rotate_levels:
    find_start_point(rl)
    melt()

visited = [[0] * (2**N) for _ in range (2**N)]
max_iceberg = 0
for i in range (2**N):
    for j in range (2**N):
        if visited[i][j] == 0 and arr[i][j] != 0:
            bfs(i, j)


print(sum(map(sum, arr)))
print(max_iceberg)

