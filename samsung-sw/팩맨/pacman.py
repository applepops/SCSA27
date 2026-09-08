#나는 현자다.
#나는 이미 풀었다.
#문제를 다 읽고 코드 구상하자.
#기억 못할 것은 적어둔다.

def backtracking(n, cur_cnt, pi, pj, way_lst):
    global max_monster_cnt
    global packman_next_way

    if n == 3:
        if max_monster_cnt < cur_cnt:
            max_monster_cnt = cur_cnt
            packman_next_way = way_lst[:]
        return

    for i in [1, 3, 5, 7]:  # 상 좌 하 우
        ni = pi + didj[i][0]
        nj = pj + didj[i][1]

        if 0 <= ni < 4 and 0 <= nj < 4:

            way_lst.append(i)

            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                backtracking(n + 1, cur_cnt + tmp_alive_monsters_arr[ni][nj], ni, nj, way_lst)
                visited[ni][nj] = 0
            else: #이미 방문한 적 있던 곳이면 몬스터 새로 안 잡아먹음.
                backtracking(n + 1, cur_cnt, ni, nj, way_lst)

            way_lst.pop()



didj = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}

#입력받기
#r, c는 0-based로.
M, T = map(int, input().split())
packman_i, packman_j = map(lambda x: int(x)-1, input().split())

alive_monsters = []
dead_monsters = [[0] * 4 for _ in range (4)]

for _ in range (M):
    r, c, d = map(int, input().split())
    r, c = r-1, c-1
    alive_monsters.append([r, c, d]) #행, 열, 방향 순


#4*4 배열
#t턴 동안 반복한다.
for t in range (T):
    # print("======================")
    # print(f"{t+1}턴입니다.")
    # print(f"팩맨은 현재: {packman_i} {packman_j}")
    #
    # print(alive_monsters)

    #1. 몬스터 복제 시도
    #현재 위치에서 자신과 같은 방향을 가진 몬스터를 복제.
    eggs = []
    for r, c, d in alive_monsters:
        eggs.append([r, c, d])

    #2. 몬스터 이동
    #한 칸 이동하되, 몬스터 시체가 없고 팩맨이 없고 격자를 벗어나면 안됨.
    #안되는 경우 방향 바꾸고 그걸 8번해도 안되면 움직이지 않고 유지
    for i in range (len(alive_monsters)):
        ci, cj, cd = alive_monsters[i][0], alive_monsters[i][1], alive_monsters[i][2]

        for _ in range (8):

            ni = ci + didj.get(cd, 0)[0]
            nj = cj + didj.get(cd, 0)[1]

            #다음으로 갈 곳에 격자 안이고, 몬스터 시체 없고, 팩맨이 있는 위치가 아니면.
            if 0 <= ni < 4 and 0 <= nj < 4 and dead_monsters[ni][nj] == 0:
                if ni == packman_i and nj == packman_j:
                    cd += 1
                    if cd == 9:
                        cd = 1
                else:
                    alive_monsters[i][0], alive_monsters[i][1], alive_monsters[i][2] = ni, nj, cd
                    break
            else:
                cd += 1
                if cd == 9:
                    cd = 1
        else:
            continue

    #초기화하고 채워주기..
    tmp_alive_monsters_arr = [[0] * 4 for _ in range (4)]

    for r, c, d in alive_monsters:
        tmp_alive_monsters_arr[r][c] += 1

    # for row in tmp_alive_monsters_arr:
    #     print(*row)

    #3. 팩맨 이동
    #백트래킹. 상, 좌, 하, 우 순으로 순열로 3개 뽑기. -> 가장 많은 방향 3개 lst를 반환.
    max_monster_cnt = 0

    packman_next_way = []
    tmp_lst = []

    visited = [[0] * 4 for _ in range (4)]
    backtracking(0, 0, packman_i, packman_j, tmp_lst)
    # print("팩맨 이동경로")
    # print(packman_next_way)

    # 그 lst에 따라서 팩맨이 움직이면서 애들 죽인다.
    # 몬스터의 시체를 남긴다. dead_monsters 배열에 2를 추가.
    new_alive_monsters = []
    dead_idx = []
    for way in packman_next_way:
        ni = packman_i + didj.get(way, 0)[0]
        nj = packman_j + didj.get(way, 0)[1]

        if tmp_alive_monsters_arr[ni][nj] > 0:
            dead_monsters[ni][nj] = 2 #그냥 개수 상관없이 2처리만 하면 되는 거 아님? 1이랑 2짜리가 같이 있어도 2기준이겠지.

        for i in range (len(alive_monsters)):
            if ni == alive_monsters[i][0] and nj == alive_monsters[i][1]:
                dead_idx.append(i)

        packman_i = ni #팩맨 위치 업데이트
        packman_j = nj

    for i in range (len(alive_monsters)):
        if i in dead_idx:
            continue
        else:
            new_alive_monsters.append(alive_monsters[i]) #죽은 애들 빼고 산 애들만 다시 넣어주기

    alive_monsters = new_alive_monsters

    # print("팩맨이 지나가고.. 살아남은 애들")
    # print(alive_monsters)

    #4. 몬스터 시체 소멸
    for i in range (4):
        for j in range (4):
            if dead_monsters[i][j] == 2:
                continue
            elif dead_monsters[i][j] > 0:
                dead_monsters[i][j] -= 1

    # print("시체들.")
    # for row in dead_monsters:
    #     print(*row)

    #5. 몬스터 복제 완성
    #알들이 깨어난다. alive_monsters에 넣어주자.
    alive_monsters = alive_monsters + eggs
    # print("알들이 깨어났다.")
    # print(alive_monsters)


#다 끝나고 나면..
#살아남은 몬스터의 마리 수를 출력한다.

print(len(alive_monsters))