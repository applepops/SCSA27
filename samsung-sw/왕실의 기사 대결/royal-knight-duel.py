#제출 후 실패시 30분 뒤에 제출 가능함.
#신중한 단위테스트와 검증
#ideation 작은 과정도 꼼꼼하게 하기.
from collections import deque

def find_moving_knights(snum, d):
    m_knights = set()

    q = deque()
    visited = [[0] * L for _ in range(L)]

    for i in range(knights_info[snum][0], knights_info[snum][0] + knights_info[snum][2]):
        for j in range(knights_info[snum][1], knights_info[snum][1] + knights_info[snum][3]):
            q.append([i, j])
            visited[i][j] = 1

    m_knights.add(snum)

    while q:
        ci, cj = q.popleft()

        if d == 0:
            di, dj = -1, 0

            ni = di + ci
            nj = dj + cj

            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0 and knights[ni][nj] >= 0:
                m_knights.add(knights[ni][nj])

                for i in range(knights_info[knights[ni][nj]][0], knights_info[knights[ni][nj]][0] + knights_info[knights[ni][nj]][2]):
                    for j in range(knights_info[knights[ni][nj]][1], knights_info[knights[ni][nj]][1] + knights_info[knights[ni][nj]][3]):
                        q.append([i, j])
                        visited[i][j] = 1

        elif d == 1:
            di, dj = 0, 1

            ni = di + ci
            nj = dj + cj

            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0 and knights[ni][nj] >= 0:
                m_knights.add(knights[ni][nj])

                for i in range(knights_info[knights[ni][nj]][0], knights_info[knights[ni][nj]][0] + knights_info[knights[ni][nj]][2]):
                    for j in range(knights_info[knights[ni][nj]][1], knights_info[knights[ni][nj]][1] + knights_info[knights[ni][nj]][3]):
                        q.append([i, j])
                        visited[i][j] = 1

        elif d== 2:
            di, dj = 1, 0

            ni = di + ci
            nj = dj + cj

            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0 and knights[ni][nj] >= 0:
                m_knights.add(knights[ni][nj])

                for i in range(knights_info[knights[ni][nj]][0],
                               knights_info[knights[ni][nj]][0] + knights_info[knights[ni][nj]][2]):
                    for j in range(knights_info[knights[ni][nj]][1],
                                   knights_info[knights[ni][nj]][1] + knights_info[knights[ni][nj]][3]):
                        q.append([i, j])
                        visited[i][j] = 1

        elif d==3:

            di, dj = 0, -1

            ni = di + ci
            nj = dj + cj

            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0 and knights[ni][nj] >= 0:
                m_knights.add(knights[ni][nj])

                for i in range(knights_info[knights[ni][nj]][0],
                               knights_info[knights[ni][nj]][0] + knights_info[knights[ni][nj]][2]):
                    for j in range(knights_info[knights[ni][nj]][1],
                                   knights_info[knights[ni][nj]][1] + knights_info[knights[ni][nj]][3]):
                        q.append([i, j])
                        visited[i][j] = 1

    return m_knights


def can_we_move(m_knights, d):
    for k in m_knights:
        r, c, h, w, hp = knights_info[k]

        if d == 0:
            nr, nc = r - 1, c
        elif d == 1:
            nr, nc = r, c + 1
        elif d == 2:
            nr, nc = r + 1, c
        else:
            nr, nc = r, c - 1

        for i in range(nr, nr + h):
            for j in range(nc, nc + w):
                if not (0 <= i < L and 0 <= j < L):
                    return False
                if arr[i][j] == 2:
                    return False

    return True

def put_knights_in_arr():
    global knights

    knights = [[-1] * L for _ in range(L)] #싹 초기화
    for k in range (N):
        if not dead_knights[k]: #죽은 애가 아니면
            for i in range(knights_info[k][0], knights_info[k][0] + knights_info[k][2]):
                for j in range(knights_info[k][1], knights_info[k][1] + knights_info[k][3]):
                    knights[i][j] = k

def print_knights():
    for row in knights:
        print(*row)

#[입력받기]
#체크판 크기, 기사들 숫자, 명령 개수
L, N, Q = map(int, input().split()) #[주의] 체스판 L임

arr = [list(map(int, input().split())) for _ in range (L)] #불변

knights = [[-1] * L for _ in range (L)]

knights_info = []
for _ in range (N):
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    knights_info.append([r, c, h, w, k])

dead_knights = [False] * N
hurts_knights = [0] * N

put_knights_in_arr()
# print_knights()

#왕이 내린 명령만큼 돈다..
for q in range (Q):
    # print()
    # print(f"{q+1}번째 명령")
    knight_num, way = map(int, input().split())
    knight_num -= 1
    # print(f"{knight_num}번 기사는 {way}로 가라")

    # print("이동 전")
    put_knights_in_arr()
    # print_knights()

    #[1] 이미 사라진 기사를 움직이려고 하는가?
    if dead_knights[knight_num]:
        # print("이미 사라진 기사: False")
        continue
    else:
        #아직 남아있는 기사다.

        #[3] 움직임의 대상이 되는 기사들을 알아오자.
        moving_knights = find_moving_knights(knight_num, way)

        # print("움직이는 애들")
        # print(moving_knights)

        #[4] 이번 이동이 가능한지 check한다.
        if can_we_move(moving_knights, way):
            # print("이동 가능: True")
            #[5] 기사들 위치를 업데이트 해준다.
            for m in moving_knights:

                if way == 0:
                    knights_info[m][0] -= 1
                elif way == 1:
                    knights_info[m][1] += 1
                elif way == 2:
                    knights_info[m][0] += 1
                elif way == 3:
                    knights_info[m][1] -= 1

            #[6] 데미지를 계산해서 업데이트 해준다.
            for m in moving_knights:
                if m == knight_num: #[주의] 명령을 받은 기사는 피해를 입지 않는다.
                    continue
                for i in range(knights_info[m][0], knights_info[m][0] + knights_info[m][2]):
                    for j in range(knights_info[m][1], knights_info[m][1] + knights_info[m][3]):
                        if arr[i][j] == 1: #함정이다
                            # print("닳는다")
                            knights_info[m][4] -= 1
                            hurts_knights[m] += 1 #정보 업데이트

                            # [6.1] 사라진 기사인지도 확인해서 업데이트해준다.
                            if knights_info[m][4] <= 0:
                                dead_knights[m] = True #정보 업데이트, 죽었다.
            # print(hurts_knights)
            # print(dead_knights)

            # print("이동 후")
            put_knights_in_arr()
            # print_knights()

        else: #이동이 불가능하다. 그냥 넘어간다.
            # print("이동불가: False")
            continue

# print("결국")
# print_knights()

#[7] 생존한 기사들의 데미지를 더하자.
ans = 0
for n in range (N):
    if not dead_knights[n]: #살아있는 애들일 때만 더해라.
        ans += hurts_knights[n]

print(ans)