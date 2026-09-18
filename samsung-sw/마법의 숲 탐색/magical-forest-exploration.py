'''
개인코드리뷰
260918 마법의 숲 탐색

코드길이: 주석 포함 약 164줄
메모리: 26MB
수행시간: 672ms (왜이래!)

문제이해 및 구상 (52분)
구현 (53분)
오픈테케 -> 틀림
디버깅 (30분)
검증 (5분)
제출 -> 성공

[문제이해 및 구상]
- 첫인상: 할 만한데?
- 주의해야 하는 것 1-based인 것, 시계방향/반시계방향, 숲 초기화 및 정령 사라지는 조건.
- 근데 실수한 부분이 다 문제를 꼼꼼히 읽지 않은 것으로부터 시작되었음.
- 문제 읽을 때 '나의' 출구에서만 이동가능하다는 거 문제이해에 강조하지 않았고
- 골렘의 이동도 단순히 남, 서, 동 이동만 생각했지 서하고 동이 서/동 이동 체크 후 남 체크한다는 것 빼먹음.
- 문제를 더 꼼꼼히 정독했어야 했는데 혼자만의 세계에 빠져버렸다.

[구현]
- 어려울 건 없었는데 단위테스팅하면서 로직 오류를 발견함.
- 먼저 남, 서, 동 이동을 각각 따로따로 가게 처리했는데 이러면 무한루프 돌길래 문제 다시 읽고 수정.
- 왜냐면 마지막 행에서 끝없이 좌우로 왔다갔다거리면서 끝나지 않기 때문.

[디버깅]
- 오픈테케가 틀렸음.
- 다행인 건 이 문제는 그림을 친절히 주기 때문에 찍어보며 확인하면 된다는 것.
- 틀린 부분은 위에도 간단히 설명했듯 2가지
- 1. bfs 로직: 내 출구에서만 나갈 수 있는데 남의 출구 발견하면 나가버림. 바보. -> 오픈테케 1번에서 발견
- 2. 서/동 이동 가능한지 확인한 뒤에 남 이동 확인하고 가능하면 True 해야 하는데
     바로 대각 이동을 해버리게 짰음 -> 오픈테케 2번에서 발견

[검증]
- 이렇게 구멍을 많이 발견했는데 진짜 더 틀렸으면 사람이 아니겠거니 생각.
- 그냥 다른 테케 하나 만들어보고 문제 로직대로 잘 흘러가길래 제출.
- 엣지까지 생각하지는 못함. 엣지가 뭐가 있을 수 있을까...

성공.

[잘한 점]
- 루틴을 지키긴 함(?)
- 행 index 신경 많이 써서 실수 안 함.
- 로직 수정해야 할 때 당황하지 않은 것. 사실 당황함. 근데 어쨌거나 멘탈 잡은 것.

[못한 점]
- 못한 게 더 많은 날이라고 생각함.
- 문제 꼼꼼히 읽었어야 하는데 골렘이동과 정령이동이라는 두 가지 커다란 주요 로직에서 모두 실수를 범했음.
- 용서할 수 없다. 이런 일은 있어서는 안된다.
- 문제를 잘 읽자.

'''

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

#[1] K번의 반복
for k in range (1, K+1):


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

    if is_continue:
        continue

    #[3] 정령
    #[3.1] 정령의 이동
    point = bfs(mi, mj)

    # [4] 점수 더해주기
    total_point += point - 2


#[출력하기]
print(total_point)