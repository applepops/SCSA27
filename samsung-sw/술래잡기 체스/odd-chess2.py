#순서대로 위부터 반시계방향으로 회전하는 8방향
#0-based
didj = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

#1~16번 도둑말 이동시키는 함수
def move_dorobo(sul_i, sul_j, arr_, dorobos_):

    for i in range (1, 17):

        #이미 잡힌 말이면...
        if visited[i] == 1:
            continue

        ci = dorobos_[i][0]
        cj = dorobos_[i][1]

        c_dir = dorobos_[i][2]

        ni = ci + didj[c_dir][0]
        nj = cj + didj[c_dir][1]

        for k in range (8): #8번이 맞음. 왜냐면 아예 못 가는 경우에 다시 원래 방향으로 돌아와야 됨.
            #격자 밖이다.
            if ni < 0 or nj < 0 or ni >= 4 or nj >= 4:
                #방향 45도 회전
                c_dir = (c_dir + 1) % 8
                ni = ci + didj[c_dir][0]
                nj = cj + didj[c_dir][1]
                dorobos_[i][2] = c_dir #방향도 업데이트!
            #술래가 있는 곳이다.
            elif ni == sul_i and nj == sul_j:
                #방향 45도 회전
                c_dir = (c_dir + 1) % 8
                ni = ci + didj[c_dir][0]
                nj = cj + didj[c_dir][1]
                dorobos_[i][2] = c_dir #방향도 업데이트!

            #술래가 없고 격자 안임.
            else:
                #빈칸이면
                if arr_[ni][nj] == 0:
                    arr_[ci][cj] = 0
                    arr_[ni][nj] = i
                #다른 도둑말이 있으면 -> swap
                else:
                    dorobos_[arr_[ci][cj]][0], dorobos_[arr_[ni][nj]][0] = dorobos_[arr_[ni][nj]][0], dorobos_[arr_[ci][cj]][0]
                    dorobos_[arr_[ci][cj]][1], dorobos_[arr_[ni][nj]][1] = dorobos_[arr_[ni][nj]][1], dorobos_[arr_[ci][cj]][1]
                    arr_[ci][cj], arr_[ni][nj] = arr_[ni][nj], arr_[ci][cj]
                break

def move_sulle(c_sulle_i, c_sulle_j, c_sulle_dir, c_score, arr_, dorobos_):

    global max_score

    max_score = max(c_score, max_score)

    # 먼저 도둑말들 이동...
    move_dorobo(c_sulle_i, c_sulle_j, arr_, dorobos_)

    #그 다음 술래 이동...
    #뭐 최대로 가봤자 그 방향으로 3번 가겠지.
    for k in range (1, 4):
        ni = c_sulle_i + didj[c_sulle_dir][0] * k
        nj = c_sulle_j + didj[c_sulle_dir][1] * k

        if 0 <= ni < 4 and 0 <= nj < 4:
            #말 잡자
            visited[arr_[ni][nj]] = 1
            #깊은 복사해서 넘기자..
            new_arr = [row[:] for row in arr_[:]]
            new_arr[ni][nj] = 0
            new_dorobos = [row[:] for row in dorobos_[:]]
            #재귀 호출
            move_sulle(ni, nj, dorobos[arr_[ni][nj]][2], c_score + arr_[ni][nj], new_arr, new_dorobos)
            #말 놓아주자
            visited[arr_[ni][nj]] = 0

        else:
            break


#맨앞은 더미
dorobos = [[] for _ in range (17)]
#arr도 만들어..
arr = [[0] * 4 for _ in range (4)]

#도둑들 정보 입력받기
for i in range (4):
    tmp = list(map(int, input().split()))
    dorobos[tmp[0]] = [i, 0, tmp[1]-1]
    arr[i][0] = tmp[0]
    dorobos[tmp[2]] = [i, 1, tmp[3]-1]
    arr[i][1] = tmp[2]
    dorobos[tmp[4]] = [i, 2, tmp[5]-1]
    arr[i][2] = tmp[4]
    dorobos[tmp[6]] = [i, 3, tmp[7]-1]
    arr[i][3] = tmp[6]

visited = [0] * 17

max_score = 0

#도둑말을 잡으면서 시작한다.
#처음 0, 0에 있는 애가 잡힌다.
sulle_i = 0
sulle_j = 0
sulle_dir = dorobos[arr[0][0]][2]
cur_score = arr[0][0]
visited[arr[0][0]] = 1
arr[0][0] = 0

move_sulle(sulle_i, sulle_j, sulle_dir, cur_score, arr, dorobos)

print(max_score)