#왜 이렇게 쉽지? 의심스럽다.

#한 칸에 둘 이상의 곰팡이가 주어지는 경우는 없음.
#곰팡이의 크기는 전부 다름.

#위, 아래, 오른, 왼
didj = [(-1, 0), (1, 0), (0, 1), (0, -1)]

#1. 곰팡이 채취
def get_gompangi(cc):

    global gompani_sum

    for i in range (N):
        if len(arr[i][cc]) == 1:
            gompani_sum += arr[i][cc][0][0]
            arr[i][cc] = []
            break
    #다 돌았는데 없다면..
    else:
        return

    return

#2. 곰팡이 이동
def move_gompangi():
    tmp_lst = []

    for i in range (N):
        for j in range (M):
            if len(arr[i][j]) == 1: #곰팡이가 있으면

                tmp = arr[i][j].pop(0)
                ci, cj = i, j
                c_s = tmp[1] #거리
                c_d = tmp[2] #방향
                c_b = tmp[0]

                di, dj = didj[c_d][0], didj[c_d][1]

                for _ in range(c_s):
                    ni = ci + di
                    nj = cj + dj

                    # 격자를 벗어나지 않으면.
                    if 0 <= ni < N and 0 <= nj < M:
                        ci, cj = ni, nj
                    # 격자를 벗어나면
                    else:
                        if c_d == 0:
                            c_d = 1
                        elif c_d == 1:
                            c_d = 0
                        elif c_d == 2:
                            c_d = 3
                        elif c_d == 3:
                            c_d = 2  # 정반대로 방향 전환, 전환된 방향 유지.
                        di, dj = didj[c_d][0], didj[c_d][1]
                        ci = di + ci
                        cj = dj + cj

                        continue

                tmp_lst.append([ci, cj, c_b, c_s, c_d])

            else:
                continue

    for i, j, b, s, d in tmp_lst:
        arr[i][j].append([b, s, d])


#3. 한 칸에 두 마리 이상인 경우 크기가 큰 곰팡이가 다른 곰팡이 잡아먹기 (한 놈만 남아)
def eat_gompangi():
    for i in range (N):
        for j in range (M):
            if len(arr[i][j]) >= 2:
                max_b, max_s, max_d = max(arr[i][j])
                arr[i][j] = [] #비우고 큰 놈 하나만 다시 넣기
                arr[i][j].append([max_b, max_s, max_d])


def print_arr():
    for row in arr:
        print(*row)

#격자판의 모든 열을 검사했을 때, 인턴이 채취한 곰팡이 크기의 총합.
#모든 열은 한 번씩만 검사하는 거겠지?

#입력 받기
#격자판 크기 정보, 곰팡이의 수
N, M, K = map(int, input().split())

arr = [[[] for _ in range (M)] for _ in range (N)]

gompani_sum = 0

for _ in range (K):
    #좌표, 1초동안 움직이는 거리, 이동방향, 크기
    x, y, s, d, b = map(int, input().split())
    #0-based로 만들기
    x -= 1
    y -= 1

    d -= 1

    arr[x][y].append([b, s, d]) #크기를 맨 앞에 집어넣자.

for j in range (0, M):
    get_gompangi(j)

    move_gompangi()

    eat_gompangi()

print(gompani_sum)

