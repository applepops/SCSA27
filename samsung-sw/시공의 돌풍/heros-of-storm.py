didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def snail(si, sj, which_way, start_dir):
    munji_list = []
    dir = start_dir
    ci, cj = si + didj[dir][0], sj + didj[dir][1]
    munji_list.append(arr[ci][cj])
    while (ci, cj) != (si, sj):
        ni, nj = ci + didj[dir][0], cj + didj[dir][1]
        if 0 <= ni < N and 0 <= nj < M:
            ci, cj = ni, nj
            munji_list.append(arr[ci][cj])
        else:
            dir = (dir + which_way) % 4

    return munji_list

def put_them_back(si, sj, which_way, start_dir, lst):
    dir = start_dir
    ci, cj = si + didj[dir][0], sj + didj[dir][1]
    lst_pointer = 0
    arr[ci][cj] = lst[lst_pointer]
    while (ci, cj) != (si, sj):
        ni, nj = ci + didj[dir][0], cj + didj[dir][1]
        if 0 <= ni < N and 0 <= nj < M:
            ci, cj = ni, nj
            lst_pointer+=1
            arr[ci][cj] = lst[lst_pointer]
        else:
            dir = (dir + which_way) % 4


def spread():
    tmp_munji = [[0] * M for _ in range (N)]
    for i in range (N):
        for j in range (M):
            if arr[i][j] != -1:
                cnt = 0
                for di, dj in didj:
                    ni = di + i
                    nj = dj + j
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1:
                        tmp_munji[ni][nj] += arr[i][j] // 5
                        cnt += 1

                arr[i][j] -= (arr[i][j] // 5 * cnt)

    for i in range (N):
        for j in range (M):
            arr[i][j] += tmp_munji[i][j]


N, M, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

dolpung_ijs = []
for i in range (N):
    for j in range (M):
        if arr[i][j] == -1:
            dolpung_ijs.append([i, j])


for _ in range (t):

    spread()

    lst1 = snail(dolpung_ijs[0][0], dolpung_ijs[0][1], -1, 1)
    lst2 = snail(dolpung_ijs[1][0], dolpung_ijs[1][1], 1, 1)

    lst1 = lst1[:-2:]
    lst2 = lst2[:-2:]
    lst1.insert(0, 0)
    lst2.insert(0, 0)

    lst1.insert(len(lst1), -1)
    lst2.insert(len(lst2), -1)

    put_them_back(dolpung_ijs[0][0], dolpung_ijs[0][1], -1, 1, lst1)
    put_them_back(dolpung_ijs[1][0], dolpung_ijs[1][1], 1, 1, lst2)

print(sum(map(sum, arr)) + 2)