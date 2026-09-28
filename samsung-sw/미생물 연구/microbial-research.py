from collections import deque

def bfs(si, sj):
    q = deque()
    q.append([si, sj])

    visited[si][sj] = 1
    total_cnt = 0
    cur_ijs = []

    while q:
        ci, cj = q.popleft()
        total_cnt += 1
        cur_ijs.append([ci, cj])

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == arr[si][sj]:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return total_cnt, cur_ijs

def find_best_sisj(m_num):

    tmp = sorted(ijs[m_num], key=lambda x: (x[0], x[1]))
    ddi, ddj = tmp[0][0], tmp[0][1]

    #0, 0으로 시작을 맞춰줄 거임.
    for i in range (len(tmp)):
        tmp[i][0], tmp[i][1] = tmp[i][0] - ddi, tmp[i][1] - ddj

    #x좌표 작, y좌표 작 순
    for c in range(0, N):
        for r in range(N - 1, -1, -1):
            for ci, cj in tmp:
                if not (0 <= r + ci < N and 0 <= c + cj < N) or new_arr[r + ci][c + cj] != 0:
                    break
            else:
                return r, c

    return -1, -1



N, Q = map(int, input().split())
arr = [[0] * N for _ in range (N)]

for q in range (1, Q+1):
    #[1] 이번 q회차 미생물 넣기
    c1, r1, c2, r2 = map(int, input().split())
    r1, r2 = N-r2, N-r1

    for r in range (r1, r2):
        for c in range (c1, c2):
            arr[r][c] = q

    # print(f"{q}회차 시작. 미생물 넣기")
    # for row in arr:
    #     print(*row)

    #[2] check
    #[2.0] 세팅, 얘들은 매번 갱신 필요.
    delete_lst = []
    group_cnt = [0] * (Q+1) #맨앞 더미 주의
    size_lst = [0] * (Q+1) #맨앞 더미 주의
    size_lst_for_future = [0] * (Q+1)
    ijs = [[] for _ in range (Q+1)] #맨앞 더미 주의

    visited = [[0] * N for _ in range (N)]

    #[2.1] 무리가 2개 이상으로 나누어지는지
    for i in range (N):
        for j in range (N):
            if visited[i][j] == 0 and arr[i][j] != 0:
                group_cnt[arr[i][j]] += 1

                # [2.2] 나누어진다면 그대로 없어진다.
                if group_cnt[arr[i][j]] > 1:
                    size_lst[arr[i][j]] = 0
                    ijs[arr[i][j]] = []
                    continue
                # [2.3] 안 나누어진다면 그 사이즈랑 좌표들을 기억한다.
                else:
                    now_cnt, now_ijs = bfs(i, j)
                    size_lst[arr[i][j]] += now_cnt
                    ijs[arr[i][j]] += now_ijs

    size_lst_for_future = size_lst.copy()

    #[3] 배양용기 이동
    new_arr = [[0] * N for _ in range (N)]

    #[3.1] 가장 차지한 영역이 넓은 무리 선택하기
    #둘 이상이라면 가장 먼저 투입된 미생물 선택. 근데 나는 순서대로 보니까. 괜찮지 않을까?
    for _ in range (Q):
        cur_max = max(size_lst)
        if cur_max == 0: #루프 끝.
            break

        m_num = size_lst.index(cur_max)
        size_lst[m_num] = 0

        #[3.2] new_arr에다가 이동시키자.
        si, sj = find_best_sisj(m_num)
        #[3.3] 들어갈 곳이 없는 녀석
        if (si, sj) == (-1, -1):
            continue
        else:
            for ci, cj in ijs[m_num]:
                new_arr[ci+si][cj+sj] = m_num
    # print()
    # print(f"{q}회차. 미생물 이동시키기")
    # for row in new_arr:
    #     print(*row)

    arr = new_arr

    #[4]점수계산하자.
    ssang = set()
    for i in range (N):
        for j in range (N):
            if arr[i][j] == 0:
                continue
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = di + i
                nj = dj + j
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] != arr[ni][nj] and arr[ni][nj] != 0:
                    ssang.add((min(arr[i][j], arr[ni][nj]), max(arr[i][j], arr[ni][nj])))

    ans = 0
    if ssang:
        for m1, m2 in ssang:
            ans += size_lst_for_future[m1] * size_lst_for_future[m2]

    print(ans)