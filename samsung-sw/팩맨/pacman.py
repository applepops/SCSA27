def move_packman(n):

    global max_monster_cnt
    global real_lst

    if n == 3:
        cur_monster_cnt = 0
        visited = [[0] * 4 for _ in range(4)]

        ci, cj = pi, pj

        for i in range (3):
            d = lst[i]
            ni = ci + didj[d][0]
            nj = cj + didj[d][1]

            if not (0 <= ni < 4 and 0 <= nj < 4):
                return

            if visited[ni][nj] == 0:
                cur_monster_cnt += sum(monsters[ni][nj])
                visited[ni][nj] = 1

            ci, cj = ni, nj

        if max_monster_cnt < cur_monster_cnt:
            max_monster_cnt = cur_monster_cnt
            real_lst = lst[:]

        return

    for d in [0, 2, 4, 6]:
        lst.append(d)
        move_packman(n+1)
        lst.pop()



didj = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

#몬스터 수, 턴 수
M, K = map(int, input().split())
pi, pj = map(lambda x: int(x)-1, input().split())

monsters = [[[0] * 8 for _ in range (4)] for _ in range (4)]
dead = [[0] * 4 for _ in range (4)]

for _ in range (M):
    r, c, d = map(lambda x: int(x)-1, input().split())
    monsters[r][c][d] += 1

for k in range (K):
    #[1] 몬스터 복제 시도
    eggs = [[inside[:] for inside in row[:]] for row in monsters]

    #[2] 몬스터 이동
    moved_monsters = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for i in range (4):
        for j in range (4):
            for d in range (8):
                if monsters[i][j][d] == 0:
                    continue

                ci, cj, cd = i, j, d

                for _ in range (8):
                    ni = ci + didj[cd][0]
                    nj = cj + didj[cd][1]

                    if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (pi, pj) and dead[ni][nj] == 0:
                        ci, cj = ni, nj
                        moved_monsters[ci][cj][cd] += monsters[i][j][d]
                        break

                    cd = (cd + 1) % 8

                else:
                    moved_monsters[ci][cj][cd] += monsters[i][j][d]

    monsters = moved_monsters


    #[3] 팩맨 이동
    lst = []
    real_lst = []


    max_monster_cnt = -float("inf")
    move_packman(0)

    for i in range(3):
        d = real_lst[i]
        ni = pi + didj[d][0]
        nj = pj + didj[d][1]

        if sum(monsters[ni][nj]) > 0:
            dead[ni][nj] = 3
        monsters[ni][nj] = [0] * 8

        pi, pj = ni, nj

    #[4] 몬스터 시체 소멸
    for i in range (4):
        for j in range (4):
            if dead[i][j] > 0:
                dead[i][j] -= 1

    #[5] 몬스터 복제 완성
    for i in range (4):
        for j in range (4):
            for d in range (8):
                monsters[i][j][d] += eggs[i][j][d]

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(monsters[i][j])

print(ans)