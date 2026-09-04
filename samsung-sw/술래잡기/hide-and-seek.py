#나는 이미 풀었다.
#문제를 싫어하지 말자!!!!!! 하지만 또 싫어지려해. 아니야!

#입력받기...
#N*N, M은 도망자 수, H는 나무의 수, K는 턴의 수
N, M, H, K = map(int, input().split())

hiding_people = [] #사람들은 배열로 관리할게.
for _ in range (M):
    x, y, d = map(int, input().split())
    x -= 1 #0-based로 만들어요
    y -= 1

    hiding_people.append([x, y, d])

trees = [[0] * N for _ in range (N)] #나무가 있는 위치를 바로 알기 위해..
for _ in range (H):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    trees[x][y] = 1


#술래의 좌표들이랑 방향들.. 다 저장해뒀다... 달팽이를 구현하는 게 너무 힘들어...
#술래의 시작 좌표는 N//2, N//2
si, sj = N//2, N//2
s_dir = 0

#얘가 뭐냐면 중앙에서 0, 0으로 가기까지의 좌표들임.
sulle_goes_to = []
sulle_goes_to.append([si, sj])
didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ci, cj = si, sj
c_dir = s_dir

lst = [i for i in range (1, N) for _ in range (2)]

for go in lst:
    for i in range (go):
        ni = ci + didj[c_dir][0]
        nj = cj + didj[c_dir][1]

        sulle_goes_to.append([ni, nj])
        ci = ni
        cj = nj
    c_dir = (c_dir + 1) % 4

for i in range (N-1):
    ni = ci + didj[0][0]
    nj = cj + didj[0][1]

    sulle_goes_to.append((ni, nj))

    ci = ni
    cj = nj

reversed_sulle_goes_to = sulle_goes_to[::-1]
sulle_goes_to = sulle_goes_to + reversed_sulle_goes_to[1::]
sulle_goes_to.pop(-1)

sulle_way = []

c_dir = s_dir
for go in lst:
    for i in range (go):
        sulle_way.append(c_dir)
    c_dir = (c_dir + 1) % 4

for i in range (N-1):
    sulle_way.append(c_dir)

reversed_sulle_way = []
for w in sulle_way:
    reversed_sulle_way.append((w + 2) % 4)
reversed_sulle_way.reverse()
sulle_way = sulle_way + reversed_sulle_way

# print(sulle_way)
# print(sulle_goes_to)

total_score = 0

sulle_idx = 0
#자 이게 K턴을 돌자
for k in range (1, K+1):

    #술래의 현재 위치를 가져온다.
    sulle_i, sulle_j = sulle_goes_to[sulle_idx][0], sulle_goes_to[sulle_idx][1]

    #1. 술래 위치로부터 맨허튼 거리 3 이내인 도망자들이 움직인다.
    for i in range (len(hiding_people)):
        if abs(hiding_people[i][0] - sulle_i) + abs(hiding_people[i][1] - sulle_j) <= 3:
            ni = hiding_people[i][0] + didj[hiding_people[i][2]][0]
            nj = hiding_people[i][1] + didj[hiding_people[i][2]][1]

            #격자 안이다.
            if 0 <= ni < N and 0 <= nj < N:
                if ni == sulle_i and nj == sulle_j:
                    continue
                else:
                    hiding_people[i][0] = ni
                    hiding_people[i][1] = nj
            #격자 밖이다.
            else:
                #방향 틀어서 한 칸 가본다.
                ni = hiding_people[i][0] + didj[(hiding_people[i][2] +2)%4][0]
                nj = hiding_people[i][1] + didj[(hiding_people[i][2] +2)%4][1]
                hiding_people[i][2] = (hiding_people[i][2] + 2) % 4 #안가더라도 방향은 돌려줘야되는듯?

                if ni == sulle_i and nj == sulle_j:
                    continue
                else:
                    hiding_people[i][0] = ni
                    hiding_people[i][1] = nj
    # print("도망갔다.")
    # print(hiding_people)

    #2. 술래가 움직인다. 만들어둔 달팽이 방향으로..+1만 해주면 돼.
    sulle_idx = (sulle_idx + 1)  % len(sulle_way)
    sulle_i, sulle_j = sulle_goes_to[sulle_idx][0], sulle_goes_to[sulle_idx][1]
    sulle_cur_way = sulle_way[sulle_idx]

    #3. 술래가 바라보는 방향으로 3칸에 있는 도망자들이 잡힌다. 단, 나무가 있는 곳에 도망자는 안 잡힌다.
    got_people_idx = []
    for i in range(len(hiding_people)):
        if hiding_people[i][0] == sulle_i and hiding_people[i][1] == sulle_j and trees[hiding_people[i][0]][hiding_people[i][1]] == 0:
            got_people_idx.append(i)

        if hiding_people[i][0] == sulle_i + didj[sulle_cur_way][0] and hiding_people[i][1] == sulle_j + didj[sulle_cur_way][1] and trees[hiding_people[i][0]][hiding_people[i][1]] == 0:
            got_people_idx.append(i)

        if hiding_people[i][0] == sulle_i + (didj[sulle_cur_way][0] * 2) and hiding_people[i][1] == sulle_j + (didj[sulle_cur_way][1] * 2) and trees[hiding_people[i][0]][hiding_people[i][1]] == 0:
            got_people_idx.append(i)

    # print(got_people_idx)

    #4. 점수를 계산한다.
    total_score += len(got_people_idx) * k

    new_hiding_people = []
    #5. 도망자들을 list에서 제거한다.
    for i in range (len(hiding_people)):
        if i in got_people_idx:
            continue
        else:
            new_hiding_people.append(hiding_people[i])

    hiding_people = new_hiding_people
    # print(hiding_people)

print(total_score)