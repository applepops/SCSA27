from collections import deque

didj = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move_turtle(si, sj, ei, ej):
    q = deque()
    is_found = False

    parents = [[[] for _ in range (N)] for _ in range (N)]
    visited = [[0] * N for _ in range (N)]

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            is_found = True
            break

        for di, dj in didj:
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:

                if ocean[ni][nj] == 1:
                    continue

                if turtle_arr[ni][nj] != 0:
                    continue

                q.append([ni, nj])
                visited[ni][nj] = 1

                parents[ni][nj] = [ci, cj]

    if not is_found:
        return si, sj

    else:

        route = []

        i, j = ei, ej
        route.append((i, j))
        while (i, j) != (si, sj):
            i, j = parents[i][j]
            route.append((i, j))
        route.reverse()
        route.pop(0)
        return route[0][0], route[0][1]


def eruption():
    q = deque()
    erupted = set()

    # 처음 분출하는 화산
    for r, c in volcano_info:
        amount = volcano_info[(r, c)]

        if heat_arr[r][c] + s_mout[r][c] >= amount:
            erupted.add((r, c))

            heat_arr[r][c] += amount

            # 4방향으로 분출
            for d in range(4):
                q.append([r, c, d, amount])

    while q:
        ci, cj, cd, heat = q.popleft()

        # 현재 열이 0이면 더 이상 전달할 수 없음
        if heat <= 0:
            continue

        ni = ci + didj[cd][0]
        nj = cj + didj[cd][1]

        if not (0 <= ni < N and 0 <= nj < N):
            continue

        if ocean[ni][nj] == 1:
            continue

        next_heat = heat // 2

        heat_arr[ni][nj] += next_heat

        if (
            (ni, nj) in volcano_info
            and (ni, nj) not in erupted
            and heat_arr[ni][nj] + s_mout[ni][nj]
                >= volcano_info[(ni, nj)]
        ):
            erupted.add((ni, nj))

            amount = volcano_info[(ni, nj)]

            heat_arr[ni][nj] += amount


            for d in range(4):
                q.append([ni, nj, d, amount])

        if next_heat > 0:
            q.append([ni, nj, cd, next_heat])

    return erupted

N, M, K = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range (N)]

ans = [0] * (M+1)

turtle_info = dict()
turtle_arr = [[0] * N for _ in range (N)]
for m in range (1, M+1):
    r, c = map(int, input().split())
    turtle_info[m] = [r, c]
    turtle_arr[r][c] = m


volcano_info = dict()
s_mout = [[0] * N for _ in range (N)]
for k in range (K):
    r, c, p = map(int, input().split())
    volcano_info[(r, c)] = p


heat_arr = [[0] * N for _ in range (N)]

turn = 0

for _ in range (100):

    if len(turtle_info) == 0:
        break

    turn += 1

    #[1] 거북이의 순차적인 이동
    for turtle in range (1, M+1):
        #움직일 수 있는 거북이면..
        if turtle_info.get(turtle):
            tr, tc = turtle_info[turtle][0], turtle_info[turtle][1]
            turtle_arr[tr][tc] = 0 #흔적 지워
            ntr, ntc = move_turtle(tr, tc, N-1, N-1)

            if (ntr, ntc) == (N-1, N-1):
                ans[turtle] = turn
                turtle_info.pop(turtle)
            else:
                turtle_arr[ntr][ntc] = turtle
                turtle_info[turtle] = [ntr, ntc]


    #[2] 화산의 압력 10씩 증가
    #실험
    for r, c in list(volcano_info.keys()):
        s_mout[r][c] += 10


    #[3] 화산 분출 및 연쇄 반응
    exploded_vols = eruption()

    #[4] 바다거북의 화석화
    for turtle in list(turtle_info.keys()):
        tr, tc = turtle_info[turtle][0], turtle_info[turtle][1]
        if heat_arr[tr][tc] >= 20:
            turtle_info.pop(turtle)
            turtle_arr[tr][tc] = -1 #화석화
            ans[turtle] = -1 #정답에도 기롷ㄱ

    #[5] 열기 정보 초기화
    #바다 위의 모든 열기 정보 사라짐.
    #분출한! 모든 화산 마그마 압력은 0이 되고 아닌 화산은 그대로 유지.
    new_heat_arr = [[0] * N for _ in range (N)]
    for vr, vc in list(volcano_info.keys()):
        if not (vr, vc) in exploded_vols:
            pass
        else:
            s_mout[vr][vc] = 0


    heat_arr = new_heat_arr


for a in range(1, M+1):
    if ans[a] == 0:
        ans[a] = -1
    print(ans[a])
