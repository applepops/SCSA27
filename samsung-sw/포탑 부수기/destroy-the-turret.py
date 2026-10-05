from collections import deque

def count_remained_potap():
    cnt = 0
    for i in range (N):
        for j in range (M):
            if arr[i][j] != 0:
                cnt += 1
    return cnt

def choose_attaker():
    min_power  = float("inf")
    hubo = []
    for i in range (N):
        for j in range (M):
            if arr[i][j] == 0:
                continue
            min_power = min(min_power, arr[i][j])

    for i in range (N):
        for j in range (M):
            if arr[i][j] == min_power:
                hubo.append([min_power, last_attack_arr[i][j], i+j, j, i])

    hubo = sorted(hubo, key=lambda x: (x[0], -x[1], -x[2], -x[3]))
    return hubo[0][-1], hubo[0][-2]

def choose_pi_attaker(ai, aj):
    max_power  = -float("inf")
    hubo = []

    for i in range (N):
        for j in range (M):
            if arr[i][j] == 0:
                continue
            max_power = max(max_power, arr[i][j])

    for i in range (N):
        for j in range (M):
            #공격자 제외
            if (i, j) == (ai, aj):
                continue
            if arr[i][j] == max_power:
                hubo.append([max_power, last_attack_arr[i][j], i+j, j, i])

    hubo = sorted(hubo, key=lambda x: (-x[0], x[1], x[2], x[3]))
    return hubo[0][-1], hubo[0][-2]

def laser(si, sj, ei, ej):
    q = deque()
    q.append([si, sj])

    visited = [[0] * M for _ in range (N)]
    visited[si][sj] = 1

    parents = [[[] for _ in range (M)] for _ in range (N)]

    is_reachable = False

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            is_reachable = True
            break

        for d in range (4):
            ni = didj[d][0] + ci
            nj = didj[d][1] + cj
            #어린왕자 처리
            ni %= N
            nj %= M

            if visited[ni][nj] == 0 and arr[ni][nj] != 0:
                parents[ni][nj] = [ci, cj]
                visited[ni][nj] = 1
                q.append([ni, nj])

    if not is_reachable:
        return -1
    else:
        #피해 주기
        # 공격자 제외
        ways = []
        ci, cj = ei, ej
        while (si, sj) != (ci, cj):
            ways.append([ci, cj])
            ci, cj = parents[ci][cj]

        ways.reverse()
        for w in range (len(ways)-1):
            i, j = ways[w]
            arr[i][j] -= arr[si][sj] // 2
            related_arr[i][j] = True
            if arr[i][j] < 0:
                arr[i][j] = 0
        i, j = ways[-1]
        arr[i][j] -= arr[si][sj]
        if arr[i][j] < 0:
            arr[i][j] = 0

def bomb(si, sj, ei, ej):
    ci, cj = ei, ej
    for di, dj in didj:
        ni = di + ci
        nj = dj + cj
        ni %= N
        nj %= M

        #공격자 제외
        if (ni, nj) == (si, sj):
            continue

        if arr[ni][nj] > 0:
            arr[ni][nj] -= arr[si][sj] // 2
            related_arr[ni][nj] = True
            if arr[ni][nj] < 0:
                arr[ni][nj] = 0

    arr[ei][ej] -= arr[si][sj]
    if arr[ei][ej] < 0:
        arr[ei][ej] = 0

#우하좌상 - 다음은 뭐 맘대로
didj = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
last_attack_arr = [[0] * M for _ in range (N)]

for k in range (1, K+1):
    # print(f"{k}회차")

    #종료조건
    if count_remained_potap() == 1:
        break

    related_arr = [[False] * M for _ in range (N)]

    #[1] 공격자 선정
    ai, aj = choose_attaker()
    # print("공격자")
    # print(ai, aj)
    last_attack_arr[ai][aj] = k
    related_arr[ai][aj] = True

    #[2] 피공격자 선정
    pi, pj = choose_pi_attaker(ai, aj)
    # print("피공격자")
    # print(pi, pj)
    related_arr[pi][pj] = True

    #[3] 공격자의 공격
    #공격자 버프
    arr[ai][aj] += N + M

    #[3.1] 레이저 공격
    if laser(ai, aj, pi, pj) == -1:
        #[3.2] 포탑 공격
        #공격자 제외
        bomb(ai, aj, pi, pj)

    # print("공격 후 관련된 애들")
    # for row in related_arr:
    #     print(*row)
    #
    # print()
    # print("공격 후 상태")
    # for row in arr:
    #     print(*row)

    #[4] 포탑 정비, 부서지지 않은 포탑 중 공격과 무관한 애들 1씩 증가
    for i in range (N):
        for j in range (M):
            if not related_arr[i][j] and arr[i][j] != 0:
                arr[i][j] += 1

    # print()
    # print("정비 후 상태")
    # for row in arr:
    #     print(*row)

print(max(map(max, arr)))

