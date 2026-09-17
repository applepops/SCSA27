from collections import deque

def bfs(si, sj):

    q = deque()
    q.append([si, sj])

    ijs = [[si, sj]]
    eggs_cnt = 0

    while q:
        ci, cj = q.popleft()
        eggs_cnt += arr[ci][cj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R and visited[ni][nj] == 0:
                q.append([ni, nj])
                ijs.append([ni, nj])
                visited[ni][nj] = 1

    new_eggs_cnt = eggs_cnt // len(ijs)
    for i, j in ijs:
        arr[i][j] = new_eggs_cnt

    return len(ijs)

#[입력받기]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
turn = 0

while True:

    is_move = False

    visited = [[0] * N for _ in range (N)]
    for i in range (N):
        for j in range (N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                res = bfs(i, j)
                if res > 1:
                    is_move = True

    if not is_move:
        break
    else:
        turn += 1

#[출력]
print(turn)