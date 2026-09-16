#산타때문에 상우하좌만 지키고 나머지는 걍 아무렇게나 씀.
didj = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

#가장 가까운 산타를 알아와
def choose_santa():
    hubo = [] #산타 번호, 거리, R, C
    for santa in range (1, P+1):
        if dead_santa[santa]:
            continue
        si = santa_ijs[santa][0]
        sj = santa_ijs[santa][1]
        distance = abs(deer_ij[0] - si) * abs(deer_ij[0] - si) + abs(deer_ij[1] - sj) * abs(deer_ij[1] - sj)
        hubo.append([santa, distance, si, sj])

    hubo = sorted(hubo, key=lambda x: (x[1], -x[2], -x[3]))
    return hubo[0][0] #목표로 하는 산타 번호를 return

#갈 수 있는 8방향 조사해서 가까워지는 방향으로 간 다음 좌표 반환
def go_to_santa(si, sj):
    distance_by_way = []
    for d in range (8):
        ni = deer_ij[0] + didj[d][0]
        nj = deer_ij[1] + didj[d][1]
        if 0 <= ni < N and 0 <= nj < N:
            distance = abs(ni - si) * abs(ni - si) + abs(nj - sj) * abs(nj - sj)
            distance_by_way.append(distance)

        else:
            distance_by_way.append(float("inf"))

    min_distance = min(distance_by_way)
    next_way = distance_by_way.index(min_distance)

    #루돌프 좌표 갱신했다.
    deer_ij[0], deer_ij[1] = deer_ij[0] + didj[next_way][0], deer_ij[1] + didj[next_way][1]

    return next_way

#연쇄 상호작용
def effect_others(si, sj, d):

    while True:
        #착지하게 되는 칸에 다른 산타가 있다면..
        if santa_arr[si][sj] != 0:
            pushed_santa = santa_arr[si][sj]
            #한 칸 밀려나게 되는 것이다
            ni, nj = santa_ijs[pushed_santa][0] + didj[d][0], santa_ijs[pushed_santa][1] + didj[d][1]

            if 0 <= ni < N and 0 <= nj < N: #그 밀려난 칸이 격자 이내면 계속 간다.
                santa_ijs[pushed_santa][0], santa_ijs[pushed_santa][1] = ni, nj
            else: #격자 밖이면 그 밀려난 산타는 죽는다. 그리고 더 밀려날 애들도 없다는 뜻이지.
                dead_santa[pushed_santa] = True
                return

            si, sj = santa_ijs[pushed_santa][0], santa_ijs[pushed_santa][1]

        else:
            return

#갈 수 있는 4방향 조사해서 루돌프에 가까워지는 방향으로 간 다음 좌표 반환
#다 inf면 가지말고 그냥 유지
def go_to_deer(s_num):
    si_ = santa_ijs[s_num][0]
    sj_ = santa_ijs[s_num][1]
    cur_distance = abs(deer_ij[0] - si_) * abs(deer_ij[0] - si_) + abs(deer_ij[1] - sj_) * abs(deer_ij[1] - sj_)

    distance_by_way = [] #거리랑 방향 순이다.
    #다른 산타가 없는 곳이어야 함. 범위 내여야 함.
    # 현재 거리를 알아야 함. 가까워질 수 없으면 굳이 안 움직임.
    for d in range(4):
        ni, nj = si_ + didj[d][0], sj_ + didj[d][1]
        if 0 <= ni < N and 0 <= nj < N and santa_arr[ni][nj] == 0:
            now_distance = abs(deer_ij[0] - ni) * abs(deer_ij[0] - ni) + abs(deer_ij[1] - nj) * abs(deer_ij[1] - nj)
            if now_distance >= cur_distance:
                distance_by_way.append([float("inf"), d])
            else:
                distance_by_way.append([now_distance, d])
        else:
            distance_by_way.append([float("inf"), d])

    distance_by_way = sorted(distance_by_way, key=lambda x: (x[0], x[1]))
    # print(distance_by_way)
    santa_way = distance_by_way[0][1]

    if distance_by_way[0][0] == float("inf"): #이동을 할 수 없는 경우
        return -1
    else:
        #[3.1] 산타 새로운 위치 갱신.
        santa_ijs[s_num][0], santa_ijs[s_num][1] = santa_ijs[s_num][0] + didj[santa_way][0], santa_ijs[s_num][1] + didj[santa_way][1]
        return santa_way

#산타 좌표 갱신
def save_santa_ij():
    for i in range (N):
        for j in range (N):
            santa_arr[i][j] = 0

    for santa in range (1, P+1):
        if dead_santa[santa]:
            continue
        santa_arr[santa_ijs[santa][0]][santa_ijs[santa][1]] = santa

def custom_print():
    print("======산타 현재 위치======")
    for row in santa_arr:
        print(*row)
    print("========================")
    print(f"루돌프 위치: {deer_ij[0]} {deer_ij[1]}")

#[입력받기]
#N*N, M개의 턴, P명의 산타, 루돌프의 힘, 산타의 힘.
N, M, P, C, D = map(int, input().split())
ri, rj = map(int, input().split())
deer_ij = [ri-1, rj-1]
santa_ijs = [[] for _ in range (P+1)] #1번부터 할게. 맨 앞은 더미

for _ in range(P):
    santa_num, si, sj = map(int, input().split())
    santa_ijs[santa_num] = [si-1, sj-1]

dead_santa = [False] * (P+1) #죽으면 True
dead_santa[0] = True
sleeping_santa = [0] * (P+1) #기절되면 +2 해주기
santa_score = [0] * (P+1) #점수

santa_arr = [[0] * N for _ in range (N)]
save_santa_ij() #기초공사

# custom_print() #지워라

#M턴 동안 반복한다.
for m in range (M):
    # print()
    # print(f"{m+1}턴입니다")

    #[1] 루돌프 움직임.
    #[1.1] 가장 가까운 산타를 알아온다.
    this_santa = choose_santa()
    # print(f"이번에 잡는 산타: {this_santa}")

    #[1.2] 루돌프가 이동한다. -> 루돌프 이동방향을 받는다.
    deer_way = go_to_santa(santa_ijs[this_santa][0], santa_ijs[this_santa][1])
    # print(f"루돌프 이동: {deer_ij[0]} {deer_ij[1]}")

    #[1.3] 루돌프 위치 갱신한다. #go_to_santa에서 함.

    #[2] 루돌프 이동으로 인한 충돌 확인
    if santa_arr[deer_ij[0]][deer_ij[1]] != 0:
        # [2.1] 도착 칸에 산타 있으면 산타 점수 올려주고 산타 이동시킴, 좌표 갱신.
        illed_santa = santa_arr[deer_ij[0]][deer_ij[1]]
        santa_score[illed_santa] += C

        n_si, n_sj = santa_ijs[illed_santa][0] + didj[deer_way][0] * C, santa_ijs[illed_santa][1] + didj[deer_way][1]*C
        #좌표 내
        if 0 <= n_si < N and 0 <= n_sj < N:
            santa_ijs[illed_santa][0], santa_ijs[illed_santa][1] = n_si, n_sj

            # [2.2] 산타 기절시키기
            sleeping_santa[illed_santa] = 2 #[주의]: 기절한 상태에서 또 부딪히면.. 어떻게 되는 거지... 기절이 쌓이나..

            # [2.3] 연쇄상호작용 확인.
            effect_others(santa_ijs[illed_santa][0], santa_ijs[illed_santa][1], deer_way)

        else:
            #산타 죽이기
            dead_santa[illed_santa] = True

    # [2.4] 좌표 갱신
    save_santa_ij()
    # custom_print()

    #[3] 산타가 순서대로 움직임. 죽거나 기절 안한 산타만 움직임.
    for s in range (1, P+1):
        if dead_santa[s] or sleeping_santa[s] > 0:
            continue
        # print(f"{s} 산타가 이동할 거임.")
        santa_next_way = go_to_deer(s)
        if santa_next_way == -1:
            continue
        else:
            save_santa_ij() #좌표 갱신

            #[4] 산타 이동으로 인한 충돌 확인
            if (santa_ijs[s][0], santa_ijs[s][1]) == (deer_ij[0], deer_ij[1]):
                #[4.1] 도착 칸에 루돌프 있으면 산타 점수 올려주고 산타 이동시킴. 좌표 계산.
                santa_next_way = (santa_next_way + 2) % 4 #반대로 가야지
                santa_score[s] += D
                n_si, n_sj = santa_ijs[s][0] + didj[santa_next_way][0] * D, santa_ijs[s][1] + \
                             didj[santa_next_way][1] * D
                # 좌표 내
                if 0 <= n_si < N and 0 <= n_sj < N:
                    santa_ijs[s][0], santa_ijs[s][1] = n_si, n_sj

                    #[4.2] 산타 기절시키기
                    sleeping_santa[s] = 2  # [주의]: 기절한 상태에서 또 부딪히면.. 어떻게 되는 거지... 기절이 쌓이나..

                    # [4.3] 연쇄상호작용 확인.
                    effect_others(santa_ijs[s][0], santa_ijs[s][1], santa_next_way)

                else:
                    # 산타 죽이기
                    dead_santa[s] = True

            # [4.4] 좌표 갱신
            save_santa_ij()
        # custom_print()

    #[5] 기절한 애들 턴 1씩 줄여주기
    for k in range(1, P+1):
        if sleeping_santa[k] > 0:
            sleeping_santa[k] -= 1

    # print("기절한 애들")
    # print(sleeping_santa)

    # print("죽은 애들")
    # print(dead_santa)

    #[6] 살아있는 애들 점수 주기
    for k in range (1, P+1):
        if not dead_santa[k]:
            santa_score[k] += 1

    # print(f"현재 {m+1}턴의 점수")
    # print(santa_score)

    #[7] 종료조건 확인하기, 해당되면 break
    cnt = 0
    for i in range (1, P+1):
        if dead_santa[i]:
            cnt += 1

    if cnt == P:
        break


for score in range (1, P+1):
    print(santa_score[score], end=" ")
