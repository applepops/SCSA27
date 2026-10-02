'''
엣지: N이 1이라서 즉시 종료
1 1 1 4
0
'''

#리팩 버전 -> bfs 하나로

from collections import deque

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


def change_dir(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 1
    elif direction == 2:
        return 0
    elif direction == 3:
        return 2

def bfs(si, sj, wd):

    min_distance = float("inf")
    hubo = []

    q = deque()
    q.append([si, sj, 0, wd])

    now_visited = [[0] * N for _ in range (N)]
    now_visited[si][sj] = 1

    while q:

        ci, cj, cd, cdir = q.popleft()

        if cd > min_distance:
            break

        #아직 가본 적 없는 가장 가까운 바다 후보지에 추가
        if visited[ci][cj] == 0 and min_distance >= cd:
            min_distance = min(min_distance, cd)
            hubo.append([ci, cj, cdir])

        for nd in range (4):

            ni = didj[nd][0] + ci
            nj = didj[nd][1] + cj

            #격자 내이고, 이번 bfs에서 미방문이고, 바다인 곳으로 이동
            if in_range(ni, nj) and now_visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append([ni, nj, cd + 1, nd])
                now_visited[ni][nj] = 1

    if hubo:
        hubo = sorted(hubo, key=lambda x: (x[0], x[1]))
        ans.append([hubo[0][0], hubo[0][1]])
        return hubo[0][0], hubo[0][1], hubo[0][2]
    else:
        return -1, -1, -1


didj = [(0, -1), (1, 0), (0, 1), (-1, 0)] #좌하우상

#격자 크기, 고래 위치, 고래 방향
N, r, c, d = map(int, input().split())
whale_i, whale_j, whale_d = r-1, c-1, d-1
whale_d = change_dir(whale_d)
visited = [[0] * N for _ in range (N)]

#격자 상태 0: 바다 1: 암초
arr = [list(map(int, input().split())) for _ in range (N)]
ocean_cnt = 0
for i in range (N):
    for j in range (N):
        if arr[i][j] == 0:
            ocean_cnt += 1

#시작지점 처리
visited[whale_i][whale_j] = 1
ans = []
ans.append([whale_i, whale_j])


while True:
    #[종료조건]: 헤엄칠 수 있는 모든 바다 방문 시 종료
    #모든 바다 칸은 바다 칸만을 거쳐 서로 도달 가능함으로 사실상 암초를 뺀 곳들.
    if len(ans) == ocean_cnt:
        break

    #[1] 인접 탐험

    while True:

        cnt = 1
        #정방향
        ni, nj = whale_i + didj[whale_d][0], whale_j + didj[whale_d][1]

        if in_range(ni, nj) and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            whale_i, whale_j = ni, nj
            visited[ni][nj] = 1
            ans.append([whale_i, whale_j])
            continue

        cnt += 1
        #좌회전
        ni, nj = whale_i + didj[(whale_d + 1 ) % 4][0], whale_j + didj[(whale_d + 1 ) % 4][1]

        if in_range(ni, nj) and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            whale_i, whale_j = ni, nj
            visited[ni][nj] = 1
            whale_d = (whale_d + 1) % 4
            ans.append([whale_i, whale_j])
            continue
        #우회전
        cnt += 1

        ni, nj = whale_i + didj[(whale_d - 1) % 4][0], whale_j + didj[(whale_d-1)%4][1]

        if in_range(ni, nj) and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            whale_i, whale_j = ni, nj
            visited[ni][nj] = 1
            whale_d = (whale_d - 1) % 4
            ans.append([whale_i, whale_j])
            continue
        #반대로
        cnt += 1
        ni, nj = whale_i + didj[(whale_d +2)%4][0], whale_j + didj[(whale_d+2)%4][1]

        if in_range(ni, nj) and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            whale_i, whale_j = ni, nj
            visited[ni][nj] = 1
            whale_d = (whale_d + 2) % 4
            ans.append([whale_i, whale_j])
            continue

        #갈 곳 없음. 가까운 바다로 이동하자.
        if cnt == 4:
            break


    #[2] 가까운 바다로 이동
    ei, ej, new_d = bfs(whale_i, whale_j, whale_d)
    #더 갈 곳이 없는 경우. 끝내자.
    if (ei, ej, new_d) == (-1, -1, -1):
        break

    whale_d = new_d
    whale_i, whale_j = ei, ej
    visited[ei][ej] = 1

for i, j in ans:
    print(i+1, j+1)
