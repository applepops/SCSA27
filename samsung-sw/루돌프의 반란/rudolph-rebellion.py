didj = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def update_santa_arr():
    global santa_arr

    new_santa_arr = [[0] * N for _ in range (N)]

    for santa in list(santa_info.keys()):
        r, c, state = santa_info[santa]
        if state >= 0:
            new_santa_arr[r][c] = santa

    santa_arr = new_santa_arr

def cal_distance(r1, c1, r2, c2):
    return abs(r1-r2)**2 + abs(c1-c2)**2

def pick_santa_and_move(si, sj):

    hubo = []

    for santa in santa_info.keys():
        r, c, state = santa_info[santa]
        if state == -1: #탈락한 산타 제외
            continue
        now_distance = cal_distance(si, sj, r, c)
        hubo.append([now_distance, r, c, santa])

    hubo = sorted(hubo, key=lambda x: (x[0], -x[1], -x[2]))
    mokpyo_i, mokpyo_j = hubo[0][1], hubo[0][2]
    cur_distance = hubo[0][0]

    way_hubo = []

    for d in range(8):
        ni = si + didj[d][0]
        nj = sj + didj[d][1]
        next_distance = cal_distance(ni, nj, mokpyo_i, mokpyo_j)

        if 0 <= ni < N and 0 <= nj < N and cur_distance > next_distance:
            way_hubo.append([next_distance, ni, nj, d])

    way_hubo = sorted(way_hubo, key=lambda x: (x[0]))
    #루돌프의 다음 좌표를 반환
    return way_hubo[0][1], way_hubo[0][2], way_hubo[0][-1]

def move_santa(si, sj, ri, rj):
    cur_distance = cal_distance(si, sj, ri, rj)

    way_hubo = []

    for d in range(4):
        ni = si + didj[d][0]
        nj = sj + didj[d][1]
        next_distance = cal_distance(ni, nj, ri, rj)

        if 0 <= ni < N and 0 <= nj < N and santa_arr[ni][nj] == 0 and cur_distance > next_distance:
            way_hubo.append([next_distance, d, ni, nj])

    way_hubo = sorted(way_hubo, key=lambda x: (x[0], x[1]))
    if way_hubo:
        return way_hubo[0][-2], way_hubo[0][-1], way_hubo[0][-3]
    else: #갈 곳이 없으면 안 움직여버려.
        return si, sj, -1

def go_till_end(santa_num, si, sj, d):

    while True:
        if not (0 <= si < N and 0 <= sj < N): #범위 나갔음.
            santa_info[santa_num] = [si, sj, -1]
            break

        #범위 안 나감
        if santa_arr[si][sj] == 0: #연쇄이동 없음
            break
        else: #연쇄이동 있음
            santa_num = santa_arr[si][sj]
            si, sj = si + didj[d][0], sj + didj[d][1]
            santa_info[santa_num][0] = si
            santa_info[santa_num][1] = sj

#######################
# [입력받기]
#######################
N, K, P, C, D = map(int, input().split())
Ri, Rj = map(lambda x: int(x)-1, input().split())
santa_info = dict()
santa_arr = [[0] * N for _ in range (N)]
santa_score = [0] * (P+1) #맨앞은 더미

for p in range (1, P+1):
    num, r, c = map(int, input().split())
    santa_info[num] = [r-1, c-1, 0] #위치, state(defalut: 0)

update_santa_arr()

#######################
# [실행부]
#######################
for k in range (1, K+1):

    #[종료조건]:
    dead_santa_cnt = 0
    for santa in range (1, P+1):
        r, c, state = santa_info[santa]
        if state == -1:
            dead_santa_cnt += 1
    if dead_santa_cnt == P:
        break

    #[1] 루돌프의 움직임
    Ri, Rj, R_d = pick_santa_and_move(Ri, Rj)

    #[2] 루돌프의 움직임으로 인한 충돌?
    #산타 기절 처리
    if santa_arr[Ri][Rj] != 0: #지금 누군가가 있음
        now_santa = santa_arr[Ri][Rj]
        santa_score[now_santa] += C #점수 획득

        s_ni = Ri + didj[R_d][0] * C #밀려나기
        s_nj = Rj + didj[R_d][1] * C

        santa_info[now_santa] = [s_ni, s_nj, k+2] #기절과 갱신

        #[3] 루돌프의 움직임으로 인한 연쇄반응
        go_till_end(now_santa, s_ni, s_nj, R_d)
        update_santa_arr()

    #[4] 산타의 순차 움직임
    for santa in range (1, P+1):
        r, c, state = santa_info[santa]
        if 0 <= state <= k: #미탈락, 미기절
            nr, nc, nd = move_santa(r, c, Ri, Rj)
            if nd == -1:
                continue
            else:
                #움직였음..
                santa_info[santa][0] = nr
                santa_info[santa][1] = nc
                update_santa_arr()

            #[5] 산타의 움직임으로 인한 충돌?
            #산타 기절 처리
            if (nr, nc) == (Ri, Rj): #루돌프와 충돌!
                santa_score[santa] += D  # 점수 획득

                s_ni = Ri + didj[(nd+2)%4][0] * D  # 밀려나기
                s_nj = Rj + didj[(nd+2)%4][1] * D
                update_santa_arr()

                santa_info[santa] = [s_ni, s_nj, k + 2] #기절과 갱신
                # [5] 산타의 움직임으로 인한 연쇄반응
                go_till_end(santa, s_ni, s_nj, (nd+2)%4)
            update_santa_arr()

    #[6] 기절 안 한 산타는 1씩 점수 얻음
    for santa in list(santa_info.keys()):
        r, c, state = santa_info[santa]
        if state >= 0:
            santa_score[santa] += 1

for i in range (1, P+1):
    print(santa_score[i], end=" ")