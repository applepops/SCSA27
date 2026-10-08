from collections import deque

didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#[1]. 남쪽으로 내려가기 확인
def check_down(m, mr, mc):

    mmr, mmc = mr + didj[2][0], mc + didj[2][1]
    ijs = []
    for di, dj in didj:
        ni = mmr + di
        nj = mmc + dj
        ijs.append([ni, nj])

    for i, j in ijs:
        if not (0 <= i < R+3 and 0 <= j < C) or forest[i][j] != 0:
            return False
    else:
        #여기서 몬스터 갱신해준다.
        monster_info[m][0] = mmr
        monster_info[m][1] = mmc
        return True

def check_west(m):
    mr, mc, md = monster_info[m]

    mmr, mmc = mr + didj[3][0], mc + didj[3][1]
    ijs = []
    for di, dj in didj:
        ni = mmr + di
        nj = mmc + dj
        ijs.append([ni, nj])

    for i, j in ijs:
        if not (0 <= i < R+3 and 0 <= j < C) or forest[i][j] != 0:
            return False
    else:
        if (check_down(m, mmr, mmc)):
            monster_info[m][2] = (monster_info[m][2] - 1) % 4
            return True

def check_east(m):
    mr, mc, md = monster_info[m]

    mmr, mmc = mr + didj[1][0], mc + didj[1][1]
    ijs = []
    for di, dj in didj:
        ni = mmr + di
        nj = mmc + dj
        ijs.append([ni, nj])

    for i, j in ijs:
        if not (0 <= i < R+3 and 0 <= j < C) or forest[i][j] != 0:
            return False
    else:
        if (check_down(m, mmr, mmc)):
            monster_info[m][2] = (monster_info[m][2] + 1) % 4
            return True

def bfs(si, sj):
    q = deque()
    q.append([si, sj])

    visited = [[0] * C for _ in range (R+3)]
    visited[si][sj] = 1

    max_row = 1

    while q:
        ci, cj = q.popleft()

        max_row = max(ci, max_row)

        if forest[ci][cj] < 0:
            for di, dj in didj:
                ni = di + ci
                nj = dj + cj

                if 0 <= ni < R + 3 and 0 <= nj < C and visited[ni][nj] == 0 and forest[ni][nj] != 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1

        else:
            for di, dj in didj:
                ni = di + ci
                nj = dj + cj

                if 0 <= ni < R+3 and 0 <= nj < C and visited[ni][nj] == 0 and forest[ni][nj] in [forest[ci][cj], -forest[ci][cj]]:
                    q.append([ni, nj])
                    visited[ni][nj] = 1

    return max_row

def update_forest():
    for m in monster_info.keys():
        sr, sc, sd = monster_info[m]
        forest[sr][sc] = m
        for di, dj in didj:
            ni = sr + di
            nj = sc + dj
            forest[ni][nj] = m

        ni = sr + didj[sd][0]
        nj = sc + didj[sd][1]
        forest[ni][nj] = -m

def reset_forest():
    global forest
    forest = [[0] * C for _ in range(R + 3)]


R, C, K = map(int, input().split())
forest = [[0] * C for _ in range (R+3)]
monster_info = dict()
score = 0

for k in range (1, K+1):
    # print()
    # print(f"{k}번 골렘 출발합니다.")
    sr = 1
    sc, d = map(int, input().split())
    sc -= 1

    monster_info[k] = [sr, sc, d]

    while True:
        mr, mc, md = monster_info[k]
        if check_down(k, mr, mc):
            continue
        elif check_west(k):
            continue
        elif check_east(k):
            continue
        else:
            break

    mr, mc, md = monster_info[k]
    if 0 <= mr < 4:
        reset_forest()
        monster_info = dict() #초기화
        continue

    # print("현재 골렘들 상태")
    # print(monster_info)
    update_forest()
    # print("현재 숲 상태")
    # for row in forest:
    #     print(*row)

    score += bfs(mr, mc) - 2
print(score)



