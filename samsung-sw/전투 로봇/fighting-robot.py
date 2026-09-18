from collections import deque

def bfs (si, sj):

    global total_distance
    min_distance = float("inf")

    q = deque()
    q.append([si, sj, 0])
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 0

    hubo = []

    while q:

        ci, cj, cd = q.popleft()

        if 0 < arr[ci][cj] < cur_level:
            if cd > min_distance:
                break
            else:
                min_distance = cd
                hubo.append([cd, ci, cj])


        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] <= cur_level:
                q.append([ni, nj, cd +1])
                visited[ni][nj] = 1

    # print(hubo)

    if hubo:
        hubo = sorted(hubo, key=lambda x: (x[0], x[1], x[2]))
        arr[hubo[0][1]][hubo[0][2]] = 0
        total_distance += hubo[0][0]
        return hubo[0][1], hubo[0][2]
    else:
        return -1, -1

#[입력받기]
N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]

for i in range (N):
    for j in range (N):
        if arr[i][j] == 9:
            robot_i, robot_j = i, j
            arr[i][j] = 0

killed_monster_cnt = 0
total_distance = 0

cur_level = 2

while True:

    robot_i, robot_j = bfs(robot_i, robot_j)
    # print(robot_i, robot_j)

    if (robot_i, robot_j) != (-1, -1):
        killed_monster_cnt += 1
    else:
        break

    if killed_monster_cnt == cur_level:
        cur_level += 1
        killed_monster_cnt = 0

print(total_distance)