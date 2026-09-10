def custom_print(arr_):
    print("==========")
    for row in arr_:
        print(*row)
    print("==========")

didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#입력받기
#격자의 크기, 플레이어의 수, 라운드의 수
N, M, K = map(int, input().split())

tmp_arr = [list(map(int, input().split())) for _ in range (N)]

guns_arr = [[[0] for _ in range (N)] for _ in range (N)]

for i in range (N):
    for j in range (N):
        if tmp_arr[i][j] > 0:
            guns_arr[i][j].append(tmp_arr[i][j])

players_point = [0] * M #플레이어들 포인트 저장할 거임.
players_info = [[] for _ in range (M)] #플레이어 좌표, 방향, 기초 공격력, 총 공격력 저장용
players_arr = [[-1] * N for _ in range (N)] #플레이어 넘버를 넣어서 위치 표현. 플레이어 없는 곳은 -1

for m in range (M):
    #좌표, 방향, 기초공격력
    x, y, d, s = map(int, input().split())
    x, y = x-1, y-1 #0-based로 만들기
    players_info[m] = [x, y, d, s, 0] #처음에는 다 총 없으니까 총 추가.
    #2차원에도 저장하자.
    players_arr[x][y] = m

# custom_print(players_arr)
# custom_print(guns_arr)
# print(players_info)

#K번의 라운드 동안 반복한다.
for k in range (K):
    #플레이어 M명이 순차적으로 다 돈다.
    for m in range (M):

        #플레이어의 이동처리
        ci, cj, cdir, cs, cgun = players_info[m]
        players_arr[ci][cj] = -1 #출발했응께 초기화.

        ni = didj[cdir][0] + ci
        nj = didj[cdir][1] + cj

        if not (0 <= ni < N and 0 <= nj < N): #격자 밖이면..
            cdir = (cdir + 2) % 4 #방향 바꾸기
            ni = didj[cdir][0] + ci
            nj = didj[cdir][1] + cj

        ci, cj = ni, nj
        players_info[m] = [ci, cj, cdir, cs, cgun] #방향 바뀌었을 가능성 때문에 갱신.

        #이동 칸에 플레이어가 없는지 확인
        #   칸에 총이 있는지 확인 -> 이건 할 필요가 없긴 함. 왜냐면 난 default가 0이라.
        #   swap한다. max인 녀석이랑.

        if players_arr[ci][cj] == -1:
            for g in range (len(guns_arr[ci][cj])):
                if guns_arr[ci][cj][g] > cgun:
                    cgun, guns_arr[ci][cj][g] = guns_arr[ci][cj][g], cgun

            players_arr[ci][cj] = m #위치 갱신한다.
            players_info[m] = [ci, cj, cdir, cs, cgun]

        # 이동 칸에 플레이어가 있다면.
        else:
            #싸운다.
            #이동 칸의 플레이어 정보를 가져온다.
            other_player_num = players_arr[ci][cj]
            oi, oj, odir, os, ogun = players_info[other_player_num]

            winner_num = -1
            loser_num = -1

            #비교한다. 비교 기준 2개다.
            # 이긴 사람과 진 사람의 player number를 알아온다.
            if os + ogun > cs + cgun:
                winner_num = other_player_num
                loser_num = m
            elif cs + cgun > os + ogun:
                winner_num = m
                loser_num = other_player_num
            elif os + ogun == cs + cgun: #둘이 똑같다면..
                if os > cs:
                    winner_num = other_player_num
                    loser_num = m
                else:
                    winner_num = m
                    loser_num = other_player_num

            #이긴 사람은 우선 그 값의 차를 point로 획득한다.
            players_point[winner_num] += abs((os + ogun) - (cs + cgun))

            wi, wj, wdir, ws, wgun = players_info[winner_num]
            li, lj, ldir, ls, lgun = players_info[loser_num]

            #진 사람은 gun을 0으로 하고 그 위치에 gun append해준다.
            guns_arr[ci][cj].append(lgun)
            lgun = 0

            #그리고 진 사람은 본인 이동방향으로 이동한다.
            l_ni = didj[ldir][0] + ci
            l_nj = didj[ldir][1] + cj

            while True:
                #만약 이동방향에 다른 플레이어가 있거나 격자 범위 밖이면 회전한다.
                if not (0 <= l_ni < N and 0 <= l_nj < N) or players_arr[l_ni][l_nj] != -1:
                    ldir = (ldir + 1) % 4
                    l_ni = didj[ldir][0] + ci
                    l_nj = didj[ldir][1] + cj
                else:
                    break #빈칸을 발견할 때 이동한다.

            li, lj = l_ni, l_nj

            #그리고 그 칸에 갔는데 총이 있으면 제일 공격력 큰 총을 획득한다. swap 한다는 거다.
            for g in range (len(guns_arr[li][lj])):
                if guns_arr[li][lj][g] > lgun:
                    lgun, guns_arr[li][lj][g] = guns_arr[li][lj][g], lgun

            #이긴 사람의 총을 갈아끼운다.
            for g in range (len(guns_arr[ci][cj])):
                if guns_arr[ci][cj][g] > wgun:
                    wgun, guns_arr[ci][cj][g] = guns_arr[ci][cj][g], wgun

            #진 사람이든 이긴 사람이든 x랑 y랑 d랑 gun이랑 plauersarr 다 갱신한다.
            players_info[winner_num] = [wi, wj, wdir, ws, wgun]
            players_info[loser_num] = [li, lj, ldir, ls, lgun]

            players_arr[ci][cj] = winner_num
            players_arr[li][lj] = loser_num

        # print(f"{k}회차에서..")
        # print(f"{m}번 선수 이동 끝났음.")
        # custom_print(players_arr)
        # custom_print(guns_arr)
        # print("플레이어 정보")
        # print(players_info)
        #[주의] 자료구조들 갱신해!!!

print(*players_point)
