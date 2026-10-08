from collections import deque

didj = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(si, sj):

    total_cnt = 0
    red_cnt = 0
    not_red_ijs = []
    total_ijs = []
    cur_bomb_color = arr[si][sj]

    q = deque()
    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        total_cnt += 1
        if arr[ci][cj] == 0:
            red_cnt += 1
        else:
            not_red_ijs.append([ci, cj])
        total_ijs.append([ci, cj])

        for di, dj in didj:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] in [cur_bomb_color, 0]:
                q.append([ni, nj])
                visited[ni][nj] = 1

    not_red_ijs = sorted(not_red_ijs, key=lambda x: (-x[0], x[1]))
    best_i, best_j = not_red_ijs[0][0], not_red_ijs[0][1]

    return total_cnt, red_cnt, best_i, best_j, total_ijs

def apply_gravity():
    for c in range (N):
        pnt = N-1
        for r in range (N-1, -1, -1):
            if arr[r][c] == -1:
                pnt = r-1

            else:
                if arr[r][c] != 10:
                    if pnt != r:
                        arr[r][c], arr[pnt][c] = arr[pnt][c], arr[r][c]
                    pnt -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
score = 0

while True:

    red_ijs = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                red_ijs.append([i, j])

    visited = [[0] * N for _ in range (N)]
    hubo = []
    #[1] 폭탄 묶음들 찾기
    for i in range (N):
        for j in range (N):
            if 0 < arr[i][j] <= M and visited[i][j] == 0:
                tcnt, rcnt, bi, bj, ij_lst = bfs(i, j)

                if tcnt > 1: #전체 개수가 2 이상이어야 후보가 될 수 있어
                    hubo.append([tcnt, rcnt, bi, bj, ij_lst])
                #빨간색 원복하기
                for ri, rj in red_ijs:
                    visited[ri][rj] = 0

    if not hubo:
        break
    else:
        hubo = sorted(hubo, key=lambda x: (-x[0], x[1], -x[2], x[3]))
        need_to_delete = hubo[0][4]
        score += len(need_to_delete) ** 2

        # [2] 터뜨린다. 빈칸은 10으로 하자...
        for ndi, ndj in need_to_delete:
            arr[ndi][ndj] = 10

    # [3] 중력 작용
    apply_gravity()

    # [4] 90도 반시계 회전
    arr = [list(row) for row in zip(*arr)][::-1]

    # [5] 중력 작용
    apply_gravity()

print(score)