from collections import deque


didj = [(0, 1), (1, 0), (0, -1), (-1, 0)] #오아래왼위

def go_near_dust(si, sj):

    min_distance = float("inf")

    q = deque()
    q.append([si, sj, 0])

    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    hubo = []

    while q:

        ci, cj, cd = q.popleft()

        if cd > min_distance:
            break

        if 1 <= arr[ci][cj] <= 100 and min_distance >= cd:
            min_distance = min(min_distance, cd)
            hubo.append([ci, cj, cd])

        for di, dj in didj:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and 0 <= arr[ni][nj] and visited[ni][nj] == 0 and cleaner_arr[ni][nj] == 0:
                q.append([ni, nj, cd+1])
                visited[ni][nj] = 1

    hubo = sorted(hubo, key=lambda x: (x[0], x[1])) #행작 열작
    #[의문]: 후보가 없을 수가 있나? 이동 불가능한 경우.
    if hubo:
        return hubo[0][0], hubo[0][1]
    else: #이동이 불가능하다면 그냥 처음 위치 리턴.
        return si, sj

def find_best_way_and_clean(si, sj):

    way_hubo = []
    for d in range (0, 4):
        dust_cnt = 0

        for nd in (d, (d+1)%4, (d-1)%4):
            ni = si + didj[nd][0]
            nj = sj + didj[nd][1]

            if 0 <= ni < N and 0 <= nj < N and 1 <= arr[ni][nj]:
                if arr[ni][nj] > 20:
                    dust_cnt += 20
                else:
                    dust_cnt += arr[ni][nj]

        way_hubo.append([dust_cnt, d])

    way_hubo = sorted(way_hubo, key=lambda x: (-x[0], x[1]))

    #진짜 청소하기
    real_way = way_hubo[0][1]

    for nd in (real_way, (real_way + 1) % 4, (real_way - 1) % 4):
        ni = si + didj[nd][0]
        nj = sj + didj[nd][1]

        if 0 <= ni < N and 0 <= nj < N and 1 <= arr[ni][nj]:
            if arr[ni][nj] > 20:
                arr[ni][nj] -= 20
            else:
                arr[ni][nj] = 0

    #본인 격자 위치 청소
    if arr[si][sj] > 20:
        arr[si][sj] -= 20
    else:
        arr[si][sj] = 0


def add_dust():
    for i in range (N):
        for j in range (N):
            if 1 <= arr[i][j]:
                arr[i][j] += 5

def spread_dust():
    add_arr = [[0] * N for _ in range (N)]

    for i in range (N):
        for j in range (N):
            if arr[i][j] == 0:
                tmp_cnt = 0

                for di, dj in didj:
                    ni = di + i
                    nj = dj + j

                    if 0 <= ni < N and 0 <= nj < N and 1 <= arr[ni][nj]:
                        tmp_cnt += arr[ni][nj]

                add_arr[i][j] += tmp_cnt // 10

    for i in range (N):
        for j in range (N):
            arr[i][j] += add_arr[i][j]


def cal_total_dust():
    total_dust = 0
    for i in range (N):
        for j in range (N):
            if 1 <= arr[i][j]:
                total_dust += arr[i][j]

    return total_dust



####################
#[입력받기]
####################
N, K, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
cleaner_ijs = [[] for _ in range (K)]
cleaner_arr = [[0] * N for _ in range (N)]
for k in range (K):
    r, c = map(lambda x: int(x)-1, input().split())
    cleaner_ijs[k] = [r, c]

#초기세팅 - 로봇청소기를 격자 내에 넣어주기 (번호는 1번부터)
for k in range (K):
    r, c = cleaner_ijs[k]
    cleaner_arr[r][c] = k + 1


####################
#[실행부]
####################
for l in range (L):

    # print()
    # print(f"{l}턴째")

    #[1] 청소기의 이동
    for k in range (K):
        r, c = cleaner_ijs[k]
        cleaner_arr[r][c] = 0 #청소기 기존 위치 지워주기
        new_r, new_c = go_near_dust(r, c)

        #자료구조 갱신
        cleaner_arr[new_r][new_c] = k + 1
        cleaner_ijs[k] = [new_r, new_c]

    # print("청소기들 위치")
    # for row in cleaner_arr:
    #     print(*row)

    #[2] 청소
    for k in range (K):
        r, c = cleaner_ijs[k]
        find_best_way_and_clean(r, c)

    # print("청소 완료")
    # for row in arr:
    #     print(*row)

    #[3] 먼지 축적
    add_dust()

    # print("먼지 축적 완료")
    # for row in arr:
    #     print(*row)


    #[4] 먼지 확산
    spread_dust()

    # print("먼지 확산 완료")
    # for row in arr:
    #     print(*row)

    #[5] 출력
    res = cal_total_dust()
    print(res)

    if not res:
        break
