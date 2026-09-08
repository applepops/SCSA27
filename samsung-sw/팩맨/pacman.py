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


didj = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1)
}

#입력받기
#r, c는 0-based로.
M, T = map(int, input().split())
packman_i, packman_j = map(lambda x: int(x)-1, input().split())

# alive_monsters
# [r][c][d]에 해당 방향의 몬스터 개수를 저장
alive_monsters = [[[0] * 8 for _ in range(4)] for _ in range(4)]

dead_monsters = [[0] * 4 for _ in range(4)]

for _ in range(M):
    r, c, d = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    alive_monsters[r][c][d] += 1


#4*4 배열
#t턴 동안 반복한다.
for t in range(T):
    # print("======================")
    # print(f"{t+1}턴입니다.")
    # print(f"팩맨은 현재: {packman_i} {packman_j}")
    #
    # print(alive_monsters)

    #1. 몬스터 복제 시도
    #현재 위치에서 자신과 같은 방향을 가진 몬스터를 복제.
    # 기존 코드의 eggs에 몬스터 하나하나를 넣는 대신
    # 현재 배열 자체를 복사해둔다.
    eggs = [[alive_monsters[r][c][:] for c in range(4)] for r in range(4)]


    #2. 몬스터 이동
    #한 칸 이동하되, 몬스터 시체가 없고 팩맨이 없고 격자를 벗어나면 안됨.
    #안되는 경우 방향 바꾸고 그걸 8번해도 안되면 움직이지 않고 유지

    # 이동한 몬스터를 새 배열에 저장
    # 몬스터를 하나하나 이동시키는 게 아니라
    # 같은 칸/같은 방향의 몬스터를 한꺼번에 이동시킨다.
    new_alive_monsters = [[[0] * 8 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            for d in range(8):

                monster_cnt = alive_monsters[r][c][d]

                if monster_cnt == 0: #없어. 넘어가.
                    continue

                ci, cj, cd = r, c, d

                for _ in range(8):

                    ni = ci + didj[cd + 1][0]
                    nj = cj + didj[cd + 1][1]

                    #다음으로 갈 곳에 격자 안이고, 몬스터 시체 없고, 팩맨이 있는 위치가 아니면.
                    if 0 <= ni < 4 and 0 <= nj < 4 and dead_monsters[ni][nj] == 0:
                        if ni == packman_i and nj == packman_j:
                            cd += 1
                            if cd == 8:
                                cd = 0
                        else:
                            new_alive_monsters[ni][nj][cd] += monster_cnt
                            break
                    else:
                        cd += 1
                        if cd == 8:
                            cd = 0
                else:
                    #8방향 모두 이동할 수 없으면 움직이지 않고 유지
                    new_alive_monsters[r][c][d] += monster_cnt

    alive_monsters = new_alive_monsters #갱신.


    #초기화하고 채워주기..
    # 각 칸에 몬스터가 몇 마리 있는지만 따로 저장
    tmp_alive_monsters_arr = [[0] * 4 for _ in range (4)]

    for r in range(4):
        for c in range(4):
            tmp_alive_monsters_arr[r][c] = sum(alive_monsters[r][c])

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
    #
    # 기존에는 매번 alive_monsters 전체를 순회해서
    # 해당 위치의 몬스터를 찾아야 했는데,
    # 이제는 alive_monsters[ni][nj] 자체를 비워주면 된다.

    freshly_dead_monster = [[0] * 4 for _ in range (4)]

    for way in packman_next_way:

        ni = packman_i + didj[way][0]
        nj = packman_j + didj[way][1]

        if tmp_alive_monsters_arr[ni][nj] > 0:
            freshly_dead_monster[ni][nj] = 2

            # 해당 칸의 몬스터를 전부 죽임
            alive_monsters[ni][nj] = [0] * 8

            # 팩맨이 한 칸 이동해서 몬스터를 죽였으므로
            # 이후 같은 칸에 다시 방문하더라도
            # 이미 몬스터는 죽어있다.

        packman_i = ni #팩맨 위치 업데이트
        packman_j = nj


    #4. 몬스터 시체 소멸
    for i in range (4):
        for j in range (4):
            if dead_monsters[i][j] > 0:
                dead_monsters[i][j] -= 1

    for i in range (4):
        for j in range (4):
            if freshly_dead_monster[i][j] == 2:
                dead_monsters[i][j] = 2


    # print("시체들.")
    # for row in dead_monsters:
    #     print(*row)


    #5. 몬스터 복제 완성
    #알들이 깨어난다. alive_monsters에 넣어주자.

    for r in range(4):
        for c in range(4):
            for d in range(8):
                alive_monsters[r][c][d] += eggs[r][c][d]

    # print("알들이 깨어났다.")
    # print(alive_monsters)


#다 끝나고 나면..
#살아남은 몬스터의 마리 수를 출력한다.

answer = 0

for r in range(4):
    for c in range(4):
        answer += sum(alive_monsters[r][c])

print(answer)
