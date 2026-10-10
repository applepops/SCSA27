from collections import deque

didj = [(0, 1), (1, 0), (0, -1), (-1, 0)] #우하좌상

def bfs(si, sj):
    is_found = False
    q = deque()
    q.append([si, sj])

    visited =[[0] * N for _ in range(N)]
    visited[si][sj] = 1

    parents = [[[] for _ in range (N)] for _ in range (N)]

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (N-1, N-1):
            is_found = True
            break

        for di, dj in didj:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 0 and turtle_arr[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
                parents[ni][nj] = [ci, cj]

    if is_found:
        ways = []
        while (ci, cj) != (si, sj):
            ways.append([ci, cj])
            ci, cj = parents[ci][cj]
        ways.reverse()
        return ways[0][0], ways[0][1]

    else:
        return si, sj

def explode():
    q = deque()
    lst = set()

    visited = [[0]* N for _ in range (N)]
    for v in valcano_info.keys():
        r, c, p = valcano_info[v]
        if valcano_power_arr[r][c] >= p:
            for d in range (4):
                q.append([r, c, p, d])
            visited[r][c] = 1
            valcano_steam_arr[r][c] += p
            lst.add(v)

    while q:
        ci, cj, cp, cd = q.popleft()

        if cp <= 0:
            continue

        for v in valcano_info.keys():
            r, c, p = valcano_info[v]
            if valcano_steam_arr[r][c] + valcano_power_arr[r][c] >= p and visited[r][c] == 0:
                for d in range (4):
                    q.append([r, c, p, d])
                visited[r][c] = 1
                valcano_steam_arr[r][c] += p
                lst.add(v)

        ni = ci + didj[cd][0]
        nj = cj + didj[cd][1]

        if 0<= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            q.append([ni, nj, cp//2, cd])
            valcano_steam_arr[ni][nj] += cp//2

    return lst


N, M, V = map(int, input().split())
#바다의 정보
arr = [list(map(int, input().split())) for _ in range (N)]
turtle_arr = [[0]* N for _ in range (N)]
valcano_power_arr = [[0]* N for _ in range (N)]

turtle_info = dict()
for m in range (1, M+1):
    r, c = map(int, input().split())
    turtle_info[m] = [r, c, 0]
    turtle_arr[r][c] = m

valcano_info = dict()
for v in range (1, V+1):
    r, c, p = map(int, input().split())
    valcano_info[v] = [r, c, p]

turn = 0

while True:

    turn += 1
    #print(f"{turn}턴=================")
    if turn > 100:
        break

    for turtle in turtle_info.keys():
        if turtle_info[turtle][2] == 0:
            break
    else:
        break

    valcano_steam_arr = [[0] * N for _ in range(N)]

    #[1] 이동 가능한 거북이 이동
    for turtle in turtle_info.keys():
        if turtle_info[turtle][2] != 0:
            continue
        else:
            r, c, *_ = turtle_info[turtle]
            #print(f"{turtle}번 거북이")
            turtle_arr[r][c] = 0 #있던 위치 지워주기
            nr, nc = bfs(r, c)
            if (nr, nc) == (-1, -1): #이동할 수 없음
                turtle_arr[r][c] = turtle
            elif (nr, nc) == (N-1, N-1): #안식처 도착
                turtle_info[turtle] = [nr, nc, turn]
            else: #일반 이동
                turtle_arr[nr][nc] = turtle
                turtle_info[turtle] = [nr, nc, 0]

    # print("거북이 이동")
    # for row in turtle_arr:
    #     print(*row)
    #
    # print(turtle_info)
    #[2] 화산의 압력이 증가
    for r, c, *_ in valcano_info.values():
        valcano_power_arr[r][c] += 10
    # print("압력 10 증가 후")
    # for row in valcano_power_arr:
    #     print(*row)

    #[3] 화산 분출 및 연쇄 반응
    exploded = explode()
    # print()
    # print(exploded)
    # for row in valcano_steam_arr:
    #     print(*row)

    #[4] 화석화
    for t in turtle_info.keys():
        r, c, state = turtle_info[t]
        if state == 0:
            if valcano_steam_arr[r][c] >= 20:
                turtle_info[t][2] = -1
                turtle_arr[r][c] = -1

    # print(turtle_info)
    # print("거북이 화석화 후")
    # for row in turtle_arr:
    #     print(*row)

    #[5] 분출한 화산의 압력은 0으로 만들고 나머지는 그대로로 하기
    for v in valcano_info.keys():
        if v in exploded:
            r, c, p = valcano_info[v]
            valcano_power_arr[r][c] = 0


for turtle in turtle_info.keys():
    if turtle_info[turtle][2] == 0:
        turtle_info[turtle][2] = -1
    print(turtle_info[turtle][2])