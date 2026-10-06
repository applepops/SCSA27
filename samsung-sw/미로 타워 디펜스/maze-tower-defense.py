def count_monsters():
    return sum(map(sum, arr))

def kill_monsters(direction, how_much):
    global ans

    ci, cj = N//2, N//2

    for dd in range (1, how_much+1):
        ni = ci + didj[direction][0] * dd
        nj = cj + didj[direction][1] * dd
        ans += arr[ni][nj]

        arr[ni][nj] = 0

def get_snail():

    monsters = []
    for i in range (len(snail_ijs)):
        tmp = arr[snail_ijs[i][0]][snail_ijs[i][1]]
        if tmp != 0:
            monsters.append(tmp)

    return monsters

def erase_monster(monsters):
    global ans

    while True:

        new_lst = []

        new_lst.append([1, monsters[0]])
        for i in range (1, len(monsters)):
            if monsters[i] == monsters[i-1]:
                new_lst[-1][0] += 1
            else:
                new_lst.append([1, monsters[i]])

        new_new_lst =[]
        for i in range (len(new_lst)):
            if new_lst[i][0] >= 4:
                ans += new_lst[i][0] * new_lst[i][1]
                continue
            new_new_lst.append(new_lst[i])

        new_monsters = []
        for i in range (len(new_new_lst)):
            for _ in range (new_new_lst[i][0]):
                new_monsters.append(new_new_lst[i][1])

        if monsters != new_monsters:
            monsters = new_monsters
        else:
            break

    return monsters



def put_snail(monsters):
    if len(monsters) < len(snail_ijs):
        monsters += [0] * (len(snail_ijs)- len(monsters))

    for i in range(len(snail_ijs)):
        arr[snail_ijs[i][0]][snail_ijs[i][1]] = monsters[i]

#########################
#입력받기
#########################
didj = [(0, 1), (1, 0), (0, -1), (-1, 0)] #우하좌상

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
ans = 0

#########################
#달팽이 기초 공사
#########################
snail_dirs = []
snail_ijs = []

ci, cj = N//2, N//2
s_d = 2

for m in range (1, N):
    for _ in range (2):
        for _ in range (m):
            snail_dirs.append(s_d)
            snail_ijs.append([ci + didj[s_d][0], cj + didj[s_d][1]])
            ci, cj = ci + didj[s_d][0], cj + didj[s_d][1]
        s_d = (s_d - 1) % 4

snail_dirs += [(s_d)] * (N-1)
for _ in range (N-1):
    snail_ijs.append([ci + didj[s_d][0], cj + didj[s_d][1]])
    ci, cj = ci + didj[s_d][0], cj + didj[s_d][1]

#########################

for k in range (1, K+1):

    orginal_cnt = count_monsters()
    d, p = map(int, input().split())

    #[1] 플레이어의 공격
    kill_monsters(d, p)

    monsters_lst = get_snail()

    #[2] 연쇄적으로 없애기
    monsters_lst = erase_monster(monsters_lst)

    new_lst = []

    new_lst.append([1, monsters_lst[0]])
    for i in range(1, len(monsters_lst)):
        if monsters_lst[i] == monsters_lst[i - 1]:
            new_lst[-1][0] += 1
        else:
            new_lst.append([1, monsters_lst[i]])

    new_lst = [data for row in new_lst for data in row]

    #[3] 처리 후 다시 넣기
    put_snail(new_lst)


print(ans)