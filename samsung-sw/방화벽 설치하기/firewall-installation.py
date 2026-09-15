from collections import deque

def bfs(wall_lst):

    fire_cnt = 0
    tmp_arr = [row[:] for row in arr]
    for i, j in wall_lst:
        tmp_arr[i][j] = 1

    # print()
    # for row in tmp_arr:
    #     print(*row)


    visited = [[0] * M for _ in range(N)]

    for i in range (N):
        for j in range (M):
            if tmp_arr[i][j] == 2 and visited[i][j] == 0:

                q = deque()
                q.append([i, j])
                visited[i][j] = 1

                while q:

                    ci, cj = q.popleft()
                    fire_cnt += 1

                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni = di + ci
                        nj = dj + cj

                        if 0 <= ni < N and 0 <= nj <  M and visited[ni][nj] == 0 and tmp_arr[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = 1

    # print(f"불 개수: {fire_cnt}")

    return fire_cnt


def backtracking(n, idx):
    global min_fire_cnt
    global wall_cnt

    if n == 3:
        res = bfs(lst[:])
        if min_fire_cnt > res:
            min_fire_cnt = res

        return

    for h in range (idx, len(hubo)):
        lst.append(hubo[h])
        backtracking(n+1, h+1)
        lst.pop()



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
min_fire_cnt = float("inf")
wall_cnt = 0

hubo = []
for i in range (N):
    for j in range (M):
        if arr[i][j] == 0:
            hubo.append([i, j])
        if arr[i][j] == 1:
            wall_cnt += 1


lst = []
backtracking(0, 0)

# print(min_fire_cnt)

print(N*M - min_fire_cnt - wall_cnt - 3)