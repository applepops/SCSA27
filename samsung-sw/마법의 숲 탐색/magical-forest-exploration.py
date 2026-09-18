from collections import deque

#북동남서
didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#중심 좌표를 보냈을 때 모든 다른 좌표들을 다 반환하는 함수 list 반환
def get_ijs(si, sj):

    ijs = [[si, sj]]

    for di, dj in didj:
        ni = di+si
        nj = dj+sj

        ijs.append([ni, nj])

    return ijs

#해당 방향으로 골렘이 움직일 수 있는지 없는지 확인하는 함수
def can_move(monster_i, direction):

    cur_si, cur_sj = monsters[monster_i][2], monsters[monster_i][3]
    new_si, new_sj = cur_si + didj[direction][0], cur_sj + didj[direction][1]

    new_ijs = get_ijs(new_si, new_sj)

    if direction in [1, 3]:
        for i, j in new_ijs:
            if not (0 <= i < R + 3 and 0 <= j < C and arr[i][j] == 0):
                return False
        new_si, new_sj = new_si + didj[2][0], new_sj + didj[2][1]

    new_ijs = get_ijs(new_si, new_sj)

    for i, j in new_ijs:
        if not (0 <= i < R+3 and 0 <= j < C and arr[i][j] == 0):
            return False
    else:
        return True

#골렘이 더 이상 이동하지 못하는 곳까지 왔을 때
#골렘을 arr에 출구와 함께 저장하는 함수
def put_monster_in_arr(m_num, monster_ijs):

    for i, j in monster_ijs:
        arr[i][j] = m_num
        debug_arr[i][j] = m_num

    exit_i, exit_j = monsters[m_num][2] + didj[monsters[m_num][1]][0], monsters[m_num][3] + didj[monsters[m_num][1]][1]
    debug_arr[exit_i][exit_j] = -1

#정령 이동 함수
def bfs(si, sj):

    max_i = -float("inf")

    q = deque()
    q.append([si, sj])

    visited = [[0] * C for _ in range(R + 3)]
    visited[si][sj] = 1

    while q:

        ci, cj = q.popleft()

        if ci > max_i:
            max_i = ci

        for di, dj in didj:
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < R+3 and 0 <= nj < C: #격자 내인가

                #ni, nj가 '나의' 출구라면 바로 넣어버려.
                if (ni, nj) == (monsters[arr[ci][cj]][4], monsters[arr[ci][cj]][5]) and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1

                #ni, nj가 내 출구가 아니야.
                else:
                    #ci, cj가 출구라면 어디든지 갈 수 있어. 골렘이기만 하면...
                    if (ci, cj) == (monsters[arr[ci][cj]][4], monsters[arr[ci][cj]][5]) and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                        q.append([ni, nj])
                        visited[ni][nj] = 1

                    #ci, cj가 출구가 아니면 ci cj와 같은 숫자의 골렘 내에서만 움직일 수 있어.
                    elif arr[ci][cj] == arr[ni][nj] and visited[ni][nj] == 0:
                        q.append([ni, nj])
                        visited[ni][nj] = 1

    return max_i

#숲을 초기화하는 함수
def restart_forest():
    global arr
    arr = [[0] * C for _ in range(R + 3)]

#[입력받기]
R, C, K = map(int, input().split())

monsters = [[] for _ in range (K+1)]
arr = [[0] * C for _ in range (R+3)]
total_point = 0

debug_arr = [[0] * C for _ in range (R+3)]

#[1] K번의 반복
for k in range (1, K+1):

    # print(f"{k}턴")

    #[2] 골렘
    #[2.1] 골렘의 정보 저장 (골렘 번호, 골렘 출구 방향, 골렘 중심 좌표 i, j)
    ci, d = map(int, input().split())
    monsters[k] = [k, d, 1, ci-1]
    is_continue = False

    #[2.2] 골렘의 끝없는 이동
    while True:
        if can_move(k, 2):
            # 골렘 중심좌표 갱신
            mi, mj = monsters[k][2], monsters[k][3]
            monsters[k][2], monsters[k][3] = mi + didj[2][0], mj + didj[2][1]

        elif can_move(k, 3):
            mi, mj = monsters[k][2], monsters[k][3]
            monsters[k][2], monsters[k][3] = mi + didj[3][0] + didj[2][0], mj + didj[3][1] + didj[2][1]
            #출구 방향 돌리기 - 반시계 방향
            monsters[k][1] = (monsters[k][1] - 1) % 4

        elif can_move(k, 1):
            mi, mj = monsters[k][2], monsters[k][3]
            monsters[k][2], monsters[k][3] = mi + didj[1][0] + didj[2][0], mj + didj[1][1] + didj[2][1]
            #출구 방향 돌리기 - 시계 방향
            monsters[k][1] = (monsters[k][1] + 1) % 4

        else:
            break

    #[2.3] 골렘 좌표들 임시 저장
    mi, mj = monsters[k][2], monsters[k][3]
    m_ijs = get_ijs(mi, mj)

    #[2.4] 숲 초기화 or 골렘을 arr에 저장
    for i, j in m_ijs:
        if 0 <= i < 3:
            #숲 초기화
            restart_forest()
            is_continue = True
            break
    else:
        #골렘을 arr에 저장
        put_monster_in_arr(k, m_ijs)
        #골렘의 출구 i, j도 저장을 좀 해볼게.
        monsters[k].append(mi + didj[monsters[k][1]][0])
        monsters[k].append(mj + didj[monsters[k][1]][1])

    # for row in arr:
    #     print(*row)
    # print()
    #
    # for row in debug_arr:
    #     print(*row)
    # print()

    if is_continue:
        continue

    #[3] 정령
    #[3.1] 정령의 이동
    point = bfs(mi, mj)

    # print(f"{k}의 점수는 {point-2}")
    # print()

    # [4] 점수 더해주기
    total_point += point - 2

# print(monsters)

#[출력하기]
print(total_point)