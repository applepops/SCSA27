#엣지: 전사가 없는 경우?

from collections import deque

didj = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우 0 1 2 3

def get_medusa_way(si, sj, ei, ej):
    q = deque()
    parents = [[[] for _ in range (N)] for _ in range (N)]
    visited = [[0] * N for _ in range (N)]

    visited[si][sj] = 1
    q.append([si, sj])
    is_found = False

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            is_found = True
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): #상하좌우
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
                parents[ni][nj] = [ci, cj]

    if is_found:
        path = [[ei, ej]]
        gi, gj = ei, ej
        while (gi, gj) != (si, sj):
            path.append(parents[gi][gj])
            gi, gj = parents[gi][gj]
        path.reverse()
        return path
    else:
        return -1

def get_medusa_sisun(mi, mj, way):
    q = deque()
    sisun = [[0] * N for _ in range (N)]
    sisun[mi][mj] = 1
    q.append([mi, mj])

    sisun_ijs = set()

    way_didj = []
    if way == 0: #상
        way_didj = [(-1, 0), (-1, -1), (-1, 1)]
    elif way == 1: #하
        way_didj = [(1, 0), (1, -1), (1, 1)]
    elif way == 2: #좌
        way_didj = [(-1, -1), (0, -1), (1, -1)]
    elif way == 3: #우
        way_didj = [(-1, 1), (0, 1), (1, 1)]

    while q:
        ci, cj = q.popleft()

        if (mi, mj) != (ci, cj):
            sisun_ijs.add((ci, cj))

        for di, dj in way_didj:
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and sisun[ni][nj] == 0:
                q.append([ni, nj])
                sisun[ni][nj] = 1

    sisun[mi][mj] = 0

    # print(f"메두사 시선 {way}로 발사")
    # for row in sisun:
    #     print(*row)
    #
    # print("메두사 시선 쏜 곳 좌표들")
    # print(sisun_ijs)
    # print()

    return sisun_ijs

def warriors_bfs(wi, wj, medusa_way, warrior_way): #메두사가 보는 방향, warrior가 뒤로 나가는 방향
    q = deque()
    wvisited = [[0] * N for _ in range (N)]
    wvisited[wi][wj] = 1
    q.append([wi, wj])

    w_back_ijs = set()

    way_didj = []
    if medusa_way == 0 and warrior_way == 2: #상 & 왼쪽
        way_didj = [(-1, 0), (-1, -1)]
    elif medusa_way == 0 and warrior_way == 3: #상 & 오른쪽
        way_didj = [(-1, 0), (-1, 1)]
    elif medusa_way == 1 and warrior_way == 2: #하 & 왼쪽
        way_didj = [(1, 0), (1, -1)]
    elif medusa_way == 1 and warrior_way == 3: #하 & 오른쪽
        way_didj = [(1, 0), (1, 1)]

    elif medusa_way == 2 and warrior_way == 0: #좌 & 위
        way_didj = [(0, -1), (-1, -1)]
    elif medusa_way == 2 and warrior_way == 1: #좌 & 아래
        way_didj = [(0, -1), (1, -1)]
    elif medusa_way == 3 and warrior_way == 0: #우 & 위
        way_didj = [(0, 1), (-1, 1)]
    elif medusa_way == 3 and warrior_way == 1: #우 & 아래
        way_didj = [(0, 1), (1, 1)]

    while q:
        ci, cj = q.popleft()

        if (ci, cj) != (wi, wj): #시작점은 안 넣어.
            w_back_ijs.add((ci, cj))

        for di, dj in way_didj:
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and wvisited[ni][nj] == 0:
                q.append([ni, nj])
                wvisited[ni][nj] = 1

    # print(f"{wi}, {wj}가 막아주는 곳:")
    # print(w_back_ijs)

    return w_back_ijs

def exclude_medusa_sisun(mi, mj, ijs, way):

    excluded_ijs = []

    for w in range (len(warriors_ijs)):

        #죽은 애들은 그냥 넘어가고
        if dead_warriors[w]:
            continue

        #좀 걱정되는 부분.. 시간 터지려나.. 최대 300명인디..
        if (warriors_ijs[w][0], warriors_ijs[w][1]) in ijs: #메두사의 시선 안에 있는 녀석들만.
            #상
            if way == 0:
                if warriors_ijs[w][1] == mj: #같은 열에 있으면..
                    for i in range (warriors_ijs[w][0]-1, -1, -1):
                        excluded_ijs.append((i, mj))
                else: #다른 열인데 메두사의 시선 안에 있는 거임.
                    if warriors_ijs[w][1] < mj: #왼
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 0, 2)
                    else:
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 0, 3)
            #하
            elif way == 1:
                if warriors_ijs[w][1] == mj:  # 같은 열에 있으면..
                    for i in range(warriors_ijs[w][0] + 1, N):
                        excluded_ijs.append((i, mj))
                else: #다른 열인데 메두사의 시선 안에 있는 거임.
                    if warriors_ijs[w][1] < mj:  # 왼
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 1, 2)
                    else:
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 1, 3)
            #좌
            elif way == 2:
                if warriors_ijs[w][0] == mi:  # 같은 행에 있으면..
                    for j in range(warriors_ijs[w][1] - 1, -1, -1):
                        excluded_ijs.append((mi, j))
                else:  # 다른 행인데 메두사의 시선 안에 있는 거임.
                    if warriors_ijs[w][0] < mi:  #위
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 2, 0)
                    else: #아래
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 2, 1)
            #우
            elif way == 3:
                if warriors_ijs[w][0] == mi:  # 같은 행에 있으면..
                    for j in range(warriors_ijs[w][1] + 1, N):
                        excluded_ijs.append((mi, j))
                else:  # 다른 행인데 메두사의 시선 안에 있는 거임.
                    if warriors_ijs[w][0] < mi:  # 위
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 3, 0)
                    else:  # 아래
                        excluded_ijs += warriors_bfs(warriors_ijs[w][0], warriors_ijs[w][1], 3, 1)

    # print("전사들이 막아주는 좌표들")
    # print(excluded_ijs)
    excluded_ijs = set(excluded_ijs)
    ijs = ijs - excluded_ijs
    warriors_cnt = 0
    warriors_lst = []

    # print("메두사가 진짜로 멈출 수 있는 좌표들만")
    # print(ijs)
    # print()

    for w in range (len(warriors_ijs)):
        # 죽은 애들은 그냥 넘어가고
        if dead_warriors[w]:
            continue
        else:
            if (warriors_ijs[w][0], warriors_ijs[w][1]) in ijs:
                warriors_cnt += 1
                warriors_lst.append(w)

    # print("여기로 간다면 잡히는 애들")
    # print(warriors_lst)
    return warriors_cnt, warriors_lst, ijs

def get_distance(i1, j1, i2, j2):

    return abs(i1 - i2) + abs(j1 - j2)

#마을 크기, 전사의 수
N, M = map(int, input().split())

#메두사 집, 공원
si, sj, ei, ej = map(int, input().split())

#M명의 전사들의 좌표
warriors_ijs = []
tmp = list(map(int, input().split()))
for _ in range (M):
    nt = tmp[:2]
    tmp = tmp[2:]
    warriors_ijs.append(nt)

dead_warriors = [False] * M

arr = [list(map(int, input().split())) for _ in range (N)]

#[1] 메두사의 경로 찾기..
res_path = get_medusa_way(si, sj, ei, ej)
#-1이면 경로가 없는 거다. -> 근데 이걸 처음에 출력하라는 거야 뭐야
# 처음에 -1 출력하고 끝내는 거 맞는 것 같음.

mi, mj = si, sj #메두사 현재 경로

if res_path != -1:
    #전사들이 초기부터 메두사의 집에 위치하지는 않기 때문에 안심하고 첫 경로 보낼게.
    for p in range (1, len(res_path)):

        stopped_warriors = [False] * M #돌 걸린 거 풀어주기

        #[출력해야하는 변수들 준비할게]
        total_distance = 0
        stopped_warriors_cnt = 0
        attacked_warriors_cnt = 0

        mi, mj = res_path[p]

        #메두사가 가는 길에 전사가 있으면 걔는 죽는다....
        for w in range(len(warriors_ijs)):
            if (mi, mj) == (warriors_ijs[w][0], warriors_ijs[w][1]):
                dead_warriors[w] = True

        #도착한 경우 0을 출력하고 끝낸다.
        if (mi, mj) == (ei, ej):
            print(0)
            continue

        # print("메두사 현재 위치")
        # print(mi, mj)

        #[2] 메두사의 시선
        hubo = []
        for d in [0, 1, 2, 3]:
            total_sisun = get_medusa_sisun(mi, mj, d)
            cnt, w_lst, medusa_watching = exclude_medusa_sisun(mi, mj, total_sisun, d)
            hubo.append([d, cnt, w_lst, medusa_watching])
        hubo = sorted(hubo, key=lambda x: (-x[1], x[0]))

        # print("나는 어디로 갈까?")
        # print(hubo)

        for i in hubo[0][2]:
            stopped_warriors[i] = True

        # print("누가 멈췄니")
        # print(hubo[0][2])

        stopped_warriors_cnt = hubo[0][1] #출력해야됨!

        medusa_real_watching = hubo[0][3]

        tmp_set = set()
        tmp_set.add((mi, mj))

        medusa_real_watching = medusa_real_watching - tmp_set
        #[3] 전사들의 이동

        for w in range (len(warriors_ijs)):
            if dead_warriors[w] or stopped_warriors[w]:
                continue
            #첫번째 이동
            ci, cj = warriors_ijs[w][0], warriors_ijs[w][1]
            cur_distance = abs(ci - mi) + abs(cj - mj)
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = di + ci
                nj = dj + cj

                if 0 <= ni < N and 0 <= nj < N:
                    if not (ni, nj) in medusa_real_watching and get_distance(mi, mj, ni, nj) < cur_distance:
                        ci, cj = ni, nj
                        total_distance += 1
                        break
            #두번째 이동
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni = di + ci
                nj = dj + cj

                if 0 <= ni < N and 0 <= nj < N:
                    if not (ni, nj) in medusa_real_watching and get_distance(mi, mj, ni, nj) < cur_distance:
                        ci, cj = ni, nj
                        total_distance += 1
                        break

            warriors_ijs[w][0], warriors_ijs[w][1] = ci, cj #값 갱신

        # print("전사들의 위치")
        # print(warriors_ijs)
        # print("전사들이 멈췄는지")
        # print(stopped_warriors)

        # print(warriors_ijs)
        #[4] 전사의 공격
        for w in range (len(warriors_ijs)):
            if dead_warriors[w] or stopped_warriors[w]:
                continue

            if (mi, mj) == (warriors_ijs[w][0], warriors_ijs[w][1]):
                dead_warriors[w] = True
                attacked_warriors_cnt += 1

        # print("전사들이 죽었는지")
        # print(dead_warriors)

        # print("답!!!")
        print(total_distance, stopped_warriors_cnt, attacked_warriors_cnt)



        #[5] 출력. 모든 전사의 이동거리 합, 돌이 된 전사의 수, 메두사를 공격한 전사의 수
else:
    print(-1)