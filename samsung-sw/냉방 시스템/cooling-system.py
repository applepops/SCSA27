#구상 충분히 했니?
#나는 이미 풀었다.

#애매한 부분: 에어컨은 무조건 5부터 시원함이 시작되는 걸까? 일단 이걸로 해볼게.

from collections import deque

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

#사무실들 모두 K 이상인지 확인하는 함수 -> return은 True 아님 False
def check_office():
    for i, j in offices:
        if cold_airs[i][j] >= K:
            continue
        else:
            return False #하나라도 K 미만이면 False 반환
    else:
        return True #다 통과하면 True 반환

def go_cold_air(si, sj, dir):
    q = deque()
    q.append([si, sj, 5]) #일단 5부터 시작함. 나중에 수정필요하다면..

    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1 #여기 다시 갈 일은 없지만..

    while q: #미친.. 틀릴 수 있는 부분이 너무 많아.. 10분만 더 투자해서 점검하자.
        ci, cj, c_air_amount = q.popleft()
        cold_airs[ci][cj] += c_air_amount #꺼내면서 값 더해준다.

        if c_air_amount == 1: #더 갈 필요도 없다.
            continue

        if dir == 2: #왼쪽으로 퍼지기
            #왼위
            if in_range(ci-1, cj) and walls[ci][cj][0] == 0 and in_range(ci-1, cj-1) and walls[ci-1][cj][1] == 0 and visited[ci-1][cj-1] == 0:
                q.append([ci-1, cj-1, c_air_amount-1])
                visited[ci-1][cj-1] = 1

            #왼
            if in_range(ci, cj-1) and walls[ci][cj][1] == 0 and visited[ci][cj-1] == 0:
                q.append([ci, cj - 1, c_air_amount - 1])
                visited[ci][cj - 1] = 1

            #왼아래
            if in_range(ci + 1, cj) and walls[ci + 1][cj][0] == 0 and in_range(ci + 1, cj - 1) and walls[ci + 1][cj][1] == 0 and visited[ci + 1][cj - 1] == 0:
                q.append([ci + 1, cj - 1, c_air_amount - 1])
                visited[ci + 1][cj - 1] = 1

        elif dir == 3: #위쪽으로 퍼지기
            #왼위
            if in_range(ci, cj-1) and walls[ci][cj][1] == 0 and in_range(ci - 1, cj - 1) and walls[ci][cj - 1][0] == 0 and visited[ci - 1][cj - 1] == 0:
                q.append([ci - 1, cj - 1, c_air_amount - 1])
                visited[ci - 1][cj - 1] = 1
            #위
            if in_range(ci-1, cj) and walls[ci][cj][0] == 0 and visited[ci-1][cj] == 0:
                q.append([ci-1, cj, c_air_amount - 1])
                visited[ci-1][cj] = 1

            #오른위
            if in_range(ci, cj+1) and walls[ci][cj+1][1] == 0 and in_range(ci - 1, cj + 1) and \
                    walls[ci][cj + 1][0] == 0 and visited[ci - 1][cj + 1] == 0:
                q.append([ci - 1, cj + 1, c_air_amount - 1])
                visited[ci - 1][cj + 1] = 1

        elif dir == 4: #오른쪽으로 퍼지기
            #오른위
            if in_range(ci-1, cj) and walls[ci][cj][0] == 0 and in_range(ci-1, cj+1) and walls[ci-1][cj+1][1] == 0 and visited[ci-1][cj+1] == 0:
                q.append([ci-1, cj+1, c_air_amount-1])
                visited[ci-1][cj+1] = 1

            #오른
            if in_range(ci, cj+1) and walls[ci][cj+1][1] == 0 and visited[ci][cj+1] == 0:
                q.append([ci, cj + 1, c_air_amount - 1])
                visited[ci][cj + 1] = 1

            #오른아래
            if in_range(ci+1, cj) and walls[ci+1][cj][0] == 0 and in_range(ci+1, cj+1) and walls[ci+1][cj+1][1] == 0 and visited[ci+1][cj+1] == 0:
                q.append([ci+1, cj+1, c_air_amount-1])
                visited[ci+1][cj+1] = 1

        elif dir == 5: #아랫쪽으로 퍼지기
            #왼아래
            if in_range(ci, cj-1) and walls[ci][cj][1] == 0 and in_range(ci+1, cj-1) and walls[ci+1][cj-1][0] == 0 and visited[ci+1][cj-1] == 0:
                q.append([ci+1, cj-1, c_air_amount-1])
                visited[ci+1][cj-1] = 1

            #아래
            if in_range(ci+1, cj) and walls[ci+1][cj][0] == 0 and visited[ci+1][cj] == 0:
                q.append([ci+1, cj, c_air_amount - 1])
                visited[ci+1][cj] = 1

            #오른아래
            if in_range(ci, cj+1) and walls[ci][cj+1][1] == 0 and in_range(ci + 1, cj + 1) and \
                    walls[ci + 1][cj + 1][0] == 0 and visited[ci + 1][cj + 1] == 0:
                q.append([ci + 1, cj + 1, c_air_amount - 1])
                visited[ci + 1][cj + 1] = 1


def mix_cold_air():

    tmp_cold_air = [[0] * N for _ in range (N)]

    for i in range (N):
        for j in range (N):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): #순서대로 위, 아래, 왼, 오른
                ni = i + di
                nj = j + dj
                flag = False
                #범위 내인가, 내가 더 큰 게 맞냐?
                if in_range(ni, nj) and cold_airs[i][j] > cold_airs[ni][nj]:
                    if (di, dj) == (-1, 0): #위
                        if walls[i][j][0] == 0:
                            flag = True
                    elif (di, dj) == (0, -1): #왼쪽
                        if walls[i][j][1] == 0:
                            flag = True
                    elif (di, dj) == (0, 1): #오른쪽
                        if walls[ni][nj][1] == 0:
                            flag = True
                    elif (di, dj) == (1, 0): #아래
                        if walls[ni][nj][0] == 0:
                            flag = True
                if flag:
                    gap = (cold_airs[i][j] - cold_airs[ni][nj]) // 4
                    tmp_cold_air[i][j] -= gap
                    tmp_cold_air[ni][nj] += gap

    for i in range (N):
        for j in range (N):
            cold_airs[i][j] += tmp_cold_air[i][j]


#입력받기
#격자 크기 N*N, 벽의 개수, 원하는 사무실의 시원함 정도
N, M, K = map(int, input().split())

tmp_arr = [list(map(int, input().split())) for _ in range (N)]

#사무실 위치 배열에 저장하기
offices = []
#에어컨 위치 배열에 저장하기 + 에어컨 방향까지
aircons = []

for i in range (N):
    for j in range (N):
        if tmp_arr[i][j] == 1:
            offices.append([i, j])

        elif 2 <= tmp_arr[i][j] <= 5:
            aircons.append([i, j, tmp_arr[i][j]])

#[0, 0] 이면 벽 없는 거고..앞에께 있으면 위에 벽 있는 거, 뒤에께 있으면 왼쪽 벽 있는 거.
walls = [[[0, 0] for _ in range (N)] for _ in range (N)]

for _ in range (M):
    x, y, d = map(int, input().split())
    x, y = x-1, y-1
    walls[x][y][d] = 1

#시~원한 공기들은 2차원 배열로 저장할 거야
cold_airs = [[0] * N for _ in range (N)]

turn = 0

#끝없이 돈다.
while True:
    #0. turn을 1 더해준다. -> 만약 더했는데 100을 초과하면 turn을 -1로 바꾸고 while문 탈출
    turn += 1

    if turn > 100: #[주의] 나중에 수정!!!!!
        turn = -1
        break

    #1. 모든 에어컨에서 시원한 바람이 나온다.
    for i, j, d in aircons: #바로 다음 칸을 일단 먼저 구하고 걔네부터 큐에 넣을 예정임.
        if d == 2: #왼
            ni, nj = i, j-1
            go_cold_air(ni, nj, d)
        elif d == 3: #위
            ni, nj = i-1, j
            go_cold_air(ni, nj, d)
        elif d == 4: #오른
            ni, nj = i, j+1
            go_cold_air(ni, nj, d)
        elif d == 5: #아래
            ni, nj = i+1, j
            go_cold_air(ni, nj, d)

    # print(f"{turn}회차입니다.... 에휴.")
    # for row in cold_airs:
    #     print(*row)

    #2. 시원한 공기들이 섞인다.
    mix_cold_air()

    #3. 외벽에 대해서만 시원함이 1칸씩 감소한다.
    for i in range (0, N): #맨 왼쪽줄..
        if cold_airs[i][0] > 0:
            cold_airs[i][0] -= 1
    for i in range (0, N): #맨 오른쪽줄..
        if cold_airs[i][N-1] > 0:
            cold_airs[i][N-1] -= 1

    for j in range (1, N-1):
        if cold_airs[0][j] > 0:
            cold_airs[0][j] -= 1
    for j in range (1, N-1):
        if cold_airs[N-1][j] > 0:
            cold_airs[N-1][j] -= 1


    #4. 사무실들 위치를 순회하면서 모두 K이상인지 확인한다.
    #True면 while문 탈출
    if check_office():
        break

print(turn)

