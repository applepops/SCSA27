from collections import deque

def check_treasure_cnt(check_arr):

    this_time_cnt = 0

    q = deque()
    visited = [[0] * 5 for _ in range (5)]

    for i in range (5):
        for j in range (5):
            if visited[i][j] == 0:
                tmp_cnt = 0
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    tmp_cnt += 1
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni = ci + di
                        nj = cj + dj

                        if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 0 and check_arr[ni][nj] == check_arr[i][j]:
                            q.append([ni, nj])
                            visited[ni][nj] = 1

                if tmp_cnt >= 3:
                    this_time_cnt += tmp_cnt

    return this_time_cnt

def get_treasure_ijs():

    this_time_ijs = []

    q = deque()
    visited = [[0] * 5 for _ in range (5)]

    for i in range (5):
        for j in range (5):
            if visited[i][j] == 0:
                tmp_ijs = []
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    tmp_ijs.append([ci, cj])
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni = ci + di
                        nj = cj + dj

                        if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 0 and arr[ni][nj] == arr[i][j]:
                            q.append([ni, nj])
                            visited[ni][nj] = 1

                if len(tmp_ijs) >= 3: #3개 이상이어야만 유물 인정
                    this_time_ijs = this_time_ijs + tmp_ijs

    this_time_ijs = sorted(this_time_ijs, key=lambda x: (x[1], -x[0])) #열작 행큰

    return this_time_ijs

def rotate(rotate_arr, start_i, start_j, how_much):

    #부분 가져오기
    tmp_mini_arr = [row[start_j:start_j+3] for row in rotate_arr[start_i:start_i+3]]

    #돌리기
    if how_much == 90:
        tmp_mini_arr = [list(row) for row in zip(*tmp_mini_arr[::-1])]

    elif how_much == 180:
        tmp_mini_arr = [row[::-1] for row in tmp_mini_arr[::-1]]

    elif how_much == 270:
        tmp_mini_arr = [list(row) for row in zip(*tmp_mini_arr)][::-1]

    #이식하기
    for i in range (start_i, start_i+3):
        for j in range (start_j, start_j+3):
            rotate_arr[i][j] = tmp_mini_arr[i-start_i][j-start_j]

    # print()
    # print(f"{how_much}")
    # for row in rotate_arr:
    #     print(*row)
    # print()

#[입력받기]
#탐사횟수, 벽면 유물 조각 개수
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (5)]
#벽면의 숫자들
wall_treasures = deque(map(int, input().split()))
#각 턴마다 유물 가치 저장하는 배열
turn_scores = [0] * K

#K턴 돈다...
for k in range (K):
    # print(f"{k}턴입니다.")
    #[1] 탐사진행
    hubo = []
    for i in range (0, 3):
        for j in range (0, 3):
            for gakdo in [90, 180, 270]:
                tmp_arr = [row[:] for row in arr] #[주의] deepcopy 여기서
                rotate(tmp_arr, i, j, gakdo)
                t_cnt = check_treasure_cnt(tmp_arr)
                hubo.append([t_cnt, gakdo, j+1, i+1]) #유물 개수, 각도, 중심좌표 열, 행

    hubo = sorted(hubo, key= lambda x: (-x[0], x[1], x[2], x[3]))
    # print(hubo)

    #[1.1] 조기종료 조건 수행. 탐사 진행에서 유물 획득 불가.
    if hubo[0][0] == 0:
        break

    #[2] 실제로 돌리기
    rotate(arr, hubo[0][3]-1, hubo[0][2]-1, hubo[0][1])

    #[3] 유물 획득 (연쇄 획득)
    while True:
        ijs = get_treasure_ijs()
        #[3.0] 종료 조건: 더 이상 유물을 찾을 수 없음.
        if len(ijs) == 0:
            break
        else:
            #[3.1] 점수 추가
            turn_scores[k] += len(ijs)

            #[3.2] 벽면 숫자로 새롭게 채워주기
            for n in range (len(ijs)):
                this_i, this_j = ijs[n][0], ijs[n][1]
                new_treasue = wall_treasures.popleft()

                arr[this_i][this_j] = new_treasue

    # print(f"점수 {turn_scores[k]}")

#[4] 출력하기
for i in range (len(turn_scores)):
    if turn_scores[i] == 0:
        break
    else:
        print(turn_scores[i], end=" ")
