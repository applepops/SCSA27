#말을 순서대로 움직여야 하는 거겠지? 1번부터 K번..'규칙대로 순서대로 움직인다'
#한 턴이 다 끝나지 않은 경우라도 말이 4개 이상 겹쳐지면 즉시 게임 종료..

#답이 1000보다 크거나 불가능하면 -1 출력

didj = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def reverse_dir (d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def print_arr():
    for row in arr:
        print(*row)

def check_4():
    for r in range (N):
        for c in range (N):
            if len(arr[r][c]) >= 4:
                print(turn_cnt)
                exit()

turn_cnt = 0

#윷놀이 판 크기, 말의 개수
N, K = map(int, input().split())

#윷놀이판 색깔 상태
color_state = [list(map(int, input().split())) for _ in range (N)]
#말 상태를 보는 윷놀이판
arr = [[[] for _ in range (N)] for _ in range (N)]
#말의 위치와 방향정보를 저장하는 array
horses = [0] * (K+1)

for k in range (1, K+1):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1

    #말 위치랑 이동방향 바로 찾기 위한 용도로 저장해둔다.
    horses[k] = [x, y, d]
    #윷놀이판에 말 번호를 저장해둔다.
    arr[x][y].append(k)


while True:
    turn_cnt += 1

    #불가능한 경우
    if turn_cnt > 1000:
        print(-1)
        exit()

    #1번말부터 K번째 말까지 돈다.
    for i in range (1, K+1):

        c_num = i #말 번호
        ci = horses[i][0] #말 좌표
        cj = horses[i][1]
        c_dir = horses[i][2] #말 방향

        # 말이 이동할 다음 좌표를 구한다.
        ni = didj[c_dir][0] + ci
        nj = didj[c_dir][1] + cj

        c_idx = 0 #arr 해당 좌표에서의 말의 idx

        #움직이는 말이 현재 좌표에서 누군가를 위에 주렁주렁 달고 있을 수 있음.
        for idx in range (len(arr[ci][cj])):
            if arr[ci][cj][idx] == c_num:
                c_idx = idx
                break

        mal_tmp_lst = arr[ci][cj][c_idx:]  # 움직이려는 말놈들
        arr[ci][cj] = arr[ci][cj][:c_idx] # 움직이려는 말 원래 자리에서 빼주기

        #좌표가 이동가능한 곳인지 check
        if 0 <= ni < N and 0 <= nj < N:

            #그 좌표가 흰색이라면?
            if color_state[ni][nj] == 0:
                #위에 바로 얹어버리기
                arr[ni][nj] = arr[ni][nj] + mal_tmp_lst
                check_4()

                #아 말놈들을 모두 위치 변경해주어야 한다..
                for cn in mal_tmp_lst:
                    horses[cn][0] = ni
                    horses[cn][1] = nj

            #그 좌표가 빨간색이라면?
            elif color_state[ni][nj] == 1:
                mal_tmp_lst.reverse() #뒤집어주기
                arr[ni][nj] = arr[ni][nj] + mal_tmp_lst
                check_4()

                for cn in mal_tmp_lst:
                    horses[cn][0] = ni
                    horses[cn][1] = nj

            #그 좌표가 파란색이라면?
            elif color_state[ni][nj] == 2:
                #방향 바꾸기
                c_dir = reverse_dir(c_dir)
                horses[c_num][2] = c_dir #방향 바꾼 거 저장한다.
                #이동할 곳을 새롭게 정한다.
                ni = didj[c_dir][0] + ci
                nj = didj[c_dir][1] + cj

                #새롭게 이동하는 곳이 이동가능한 곳인가.
                if 0 <= ni < N and 0 <= nj < N:
                    #근데 또 파란색이면?
                    if color_state[ni][nj] == 2:
                        #그냥 원래 있던 곳에 있는다....
                        arr[ci][cj] = arr[ci][cj] + mal_tmp_lst
                        check_4()
                    #파란색 아니고 갈 수 있는 곳이면,
                    else:
                        if color_state[ni][nj] == 1:
                            mal_tmp_lst.reverse()
                        arr[ni][nj] = arr[ni][nj] + mal_tmp_lst
                        check_4()

                        for cn in mal_tmp_lst:
                            horses[cn][0] = ni
                            horses[cn][1] = nj

                else:
                    #이동 못하는 곳이면? 그냥 거기 있는다...
                    arr[ci][cj] = arr[ci][cj] + mal_tmp_lst
                    check_4()

        #다음 좌표가 이동가능한 곳이 아니면...
        else:
            c_dir = reverse_dir(c_dir)
            horses[c_num][2] = c_dir

            ni = didj[c_dir][0] + ci
            nj = didj[c_dir][1] + cj

            # 새롭게 이동하는 곳이 이동가능한 곳인가.
            if 0 <= ni < N and 0 <= nj < N:
                # 근데 또 파란색이면?
                if color_state[ni][nj] == 2:
                    # 그냥 원래 있던 곳에 있는다....
                    arr[ci][cj] = arr[ci][cj] + mal_tmp_lst
                    check_4()
                # 파란색 아니고 다른 갈 수 있는 곳이면,
                else:
                    if color_state[ni][nj] == 1:
                        mal_tmp_lst.reverse()
                    arr[ni][nj] = arr[ni][nj] + mal_tmp_lst
                    check_4()

                    for cn in mal_tmp_lst:
                        horses[cn][0] = ni
                        horses[cn][1] = nj
            else:
                # 이동 못하는 곳이면? 그냥 거기 있는다...
                arr[ci][cj] = arr[ci][cj] + mal_tmp_lst
                check_4()


    #4개 이상 겹치는 애 있는지 확인하기
    check_4()


