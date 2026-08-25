# 1번 말이 선택할 수 있는 이동경로 -> 4가지
dxdy1 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# 2번 말이 선택할 수 있는 이동경로 -> 2가지
dxdy2 = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]]
# 3번 말이 선택할 수 있는 이동경로 -> 4가지
dxdy3 = [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]]
# 4번 말이 선택할 수 있는 경로 -> 4가지
dxdy4 = [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (0, -1), (1, 0)]]
# 5번 말이 선택할 수 있는 경로 -> 1가지
dxdy5 = [[(1, 0), (-1, 0), (0, -1), (0, 1)]]

#들어가는 인자는 말의 종류, 말의 행 위치, 말의 열 위치, 말이 지금 선택한 방향
def go_horse(which_horse, si, sj, way):

    ci, cj = si, sj

    #말 본인 visited 처리하기
    my_visited[si][sj] = 1

    if which_horse == 1:
        while True:
            ni = ci + dxdy1[way][0]
            nj = cj + dxdy1[way][1]

            if 0 <= ni < N and 0 <= nj < M:
                # 상대편 말이 아닌 이상
                if arr[ni][nj] != 6:
                    my_visited[ni][nj] = 1
                    ci = ni
                    cj = nj
                else:
                    break
            else:
                break

    elif which_horse == 2:

        for k in range (2):
            ci, cj = si, sj
            while True:
                ni = ci + dxdy2[way][k][0]
                nj = cj + dxdy2[way][k][1]

                if 0 <= ni < N and 0 <= nj < M:
                    # 상대편 말이 아닌 이상
                    if arr[ni][nj] != 6:
                        my_visited[ni][nj] = 1
                        ci = ni
                        cj = nj
                    else:
                        break
                else:
                    break

    elif which_horse == 3:
        for k in range (2):
            ci, cj = si, sj
            while True:
                ni = ci + dxdy3[way][k][0]
                nj = cj + dxdy3[way][k][1]

                if 0 <= ni < N and 0 <= nj < M:
                    # 상대편 말이 아닌 이상
                    if arr[ni][nj] != 6:
                        my_visited[ni][nj] = 1
                        ci = ni
                        cj = nj
                    else:
                        break
                else:
                    break

    elif which_horse == 4:
        for k in range (3):
            ci, cj = si, sj
            while True:
                ni = ci + dxdy4[way][k][0]
                nj = cj + dxdy4[way][k][1]

                if 0 <= ni < N and 0 <= nj < M:
                    # 상대편 말이 아닌 이상
                    if arr[ni][nj] != 6:
                        my_visited[ni][nj] = 1
                        ci = ni
                        cj = nj
                    else:
                        break
                else:
                    break

    elif which_horse == 5:
        for k in range (4):
            ci, cj = si, sj
            while True:
                ni = ci + dxdy5[way][k][0]
                nj = cj + dxdy5[way][k][1]

                if 0 <= ni < N and 0 <= nj < M:
                    # 상대편 말이 아닌 이상
                    if arr[ni][nj] != 6:
                        my_visited[ni][nj] = 1
                        ci = ni
                        cj = nj
                    else:
                        break
                else:
                    break
    else:
        return

#디버깅용 프린트 함수
# def print_my_visited():
#     for row in my_visited:
#         print(*row)


def backtracking(n):
    global min_sum
    global my_visited

    # 종료조건
    if n == len(horses_lst):
        my_visited = [[0] * M for _ in range(N)]

        for h in range(len(horses_lst)):
            go_horse(horses_lst[h][0], horses_lst[h][1], horses_lst[h][2], where_to_go[h])

        temp = N*M - sum(map(sum, my_visited))
        min_sum = min(min_sum, temp)
        return

    if horses_lst[n][0] == 1:
        for i in range(len(dxdy1)):
            where_to_go.append(i)
            backtracking(n + 1)
            where_to_go.pop()

    elif horses_lst[n][0] == 2:
        for i in range(len(dxdy2)):
            where_to_go.append(i)
            backtracking(n + 1)
            where_to_go.pop()

    elif horses_lst[n][0] == 3:
        for i in range(len(dxdy3)):
            where_to_go.append(i)
            backtracking(n + 1)
            where_to_go.pop()

    elif horses_lst[n][0] == 4:
        for i in range(len(dxdy4)):
            where_to_go.append(i)
            backtracking(n + 1)
            where_to_go.pop()

    elif horses_lst[n][0] == 5:
        where_to_go.append(0)
        backtracking(n + 1)
        where_to_go.pop()


N, M = map(int, input().split())

# 체스판 입력받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 튜플. (말 종류, 행, 열) 들어감.
horses_lst = []
other_team_horse_cnt = 0

for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            horses_lst.append((arr[i][j], i, j))
        elif arr[i][j] == 6:
            other_team_horse_cnt += 1

visited = [[0] * M for _ in range(N)]
min_sum = float("INF")
where_to_go = []

backtracking(0)

print(min_sum-other_team_horse_cnt)
