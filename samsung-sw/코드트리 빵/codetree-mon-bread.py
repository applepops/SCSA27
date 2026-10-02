from collections import deque

didj = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def go_basecamp(si, sj):

    min_distance = float("inf")
    hubo = []

    q = deque()
    q.append([si, sj, 0])

    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    while q:
        ci, cj, cd = q.popleft()

        if cd > min_distance:
            break

        if arr[ci][cj] == 1 and min_distance >= cd:
            min_distance = min(min_distance, cd)
            hubo.append([ci, cj])

        for di, dj in didj:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                q.append([ni, nj, cd+1])
                visited[ni][nj] = 1

    hubo = sorted(hubo, key=lambda x: (x[0], x[1]))

    return hubo[0][0], hubo[0][1]

def go_gs25(num, si, sj):

    q = deque()
    q.append([si, sj])

    ei, ej = gs25_ijs[num]

    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    parents = [[[] for _ in range (N)] for _ in range (N)]

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            break

        for di, dj in didj:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                q.append([ni, nj])
                visited[ni][nj] = 1
                parents[ni][nj] = [ci, cj]

    ci, cj = ei, ej
    ways = []
    while (ci, cj) != (si, sj):
        ways.append([ci, cj])
        ci, cj = parents[ci][cj]

    ways.reverse()

    return ways[0][0], ways[0][1]

#격자 크기, 사람 수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

gs25_ijs = [[] for _ in range (M+1)] #맨앞 더미
for m in range (1, M+1):
    r, c = map(lambda x: int(x)-1, input().split())
    gs25_ijs[m] = [r, c]

arrived = [0] * (M+1) #맨앞 더미
people_info = dict()

turn = 1
while True:

    #[종료조건]: 모든 사람이 편의점에 도착함.
    if sum(arrived) == M:
        break

    # print(people_info)

    delete_p = []

    #[1] 현재 격자 내 사람들 움직임
    for p in people_info.keys():
        pi, pj = people_info[p]
        npi, npj = go_gs25(p, pi, pj)
        people_info[p] = [npi, npj]

        if (npi, npj) == (gs25_ijs[p][0], gs25_ijs[p][1]):
            delete_p.append(p)

    #[2] 편의점 도착하면? 못 지나가게 하기
    for p in delete_p:
        people_info.pop(p)
        arrived[p] = 1
        arr[gs25_ijs[p][0]][gs25_ijs[p][1]] = -1

    #[3] t번째 사람이 편의점과 가장 가까운 베캠 들어감
    if turn <= M:
        cur_person_to_bc = turn
        cpi, cpj = gs25_ijs[cur_person_to_bc]
        res_i, res_j = go_basecamp(cpi, cpj)

        people_info[cur_person_to_bc] = [res_i, res_j]

        #[4] 베캠 못 지나가게 하기
        arr[res_i][res_j] = -1

    turn += 1

print(turn-1)