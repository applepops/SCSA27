didj = [(0, 1), (1, 0), (0, -1), (-1, 0)] #오, 아래, 좌, 위

#몬스터들을 달팽이에서 꺼내오는 함수
def get_monster():
    ci, cj = N // 2, N // 2
    c_way = 2
    tmp_lst = [i for i in range(1, N) for _ in range(2)]
    for t in tmp_lst:
        for _ in range(t):
            ni = ci + didj[c_way][0]
            nj = cj + didj[c_way][1]

            if arr[ni][nj] != 0:
                monsters.append(arr[ni][nj])

            ci = ni
            cj = nj

        c_way = (c_way - 1) % 4

    for _ in range(N - 1):
        ni = ci + didj[c_way][0]
        nj = cj + didj[c_way][1]

        if arr[ni][nj] != 0:
            monsters.append(arr[ni][nj])

        ci = ni
        cj = nj

#몬스터들을 달팽이에 다시 집어넣는 함수
def put_monster():
    ci, cj = N // 2, N // 2
    c_way = 2
    m = 0
    tmp_lst = [i for i in range(1, N) for _ in range(2)]
    for t in tmp_lst:
        for _ in range(t):
            ni = ci + didj[c_way][0]
            nj = cj + didj[c_way][1]

            arr[ni][nj] = monsters[m]

            ci = ni
            cj = nj
            m += 1

        c_way = (c_way - 1) % 4

    for _ in range(N - 1):
        ni = ci + didj[c_way][0]
        nj = cj + didj[c_way][1]

        arr[ni][nj] = monsters[m]

        ci = ni
        cj = nj
        m += 1


#계속해서 같은 몬스터가 등장하면 삭제하는 함수.. 진짜 계속 삭제해야 함.
def delete_monster(monsters):

    global total_score

    while True:
        need_to_delete_idx = set()
        for i in range (len(monsters)-1):
            tmp_idx = []
            tmp_idx.append(i)
            for j in range (i+1, len(monsters)):
                if monsters[i] != monsters[j]:
                    break
                if monsters[i] == monsters[j]:
                    tmp_idx.append(j)
            if len(tmp_idx) >= 4:
                for idx in tmp_idx:
                    need_to_delete_idx.add(idx)

        if not need_to_delete_idx:
            break

        #몬스터 삭제해서 new_monster에 넣어주기
        new_monsters = []
        for i in range (len(monsters)):
            if i in need_to_delete_idx:
                total_score += monsters[i] #점수계산
                continue
            else:
                new_monsters.append(monsters[i])
        #갱신
        monsters = new_monsters


    return monsters


def custom_print():
    for row in arr:
        print(*row)


#입력받기
#격자 크기, 라운드의 횟수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

total_score = 0

#M회 반복합니다..
for _ in range (M):
    d, p = map(int, input().split())

    #1. 플레이어의 공격
    ci, cj = N//2, N//2
    for _ in range (p):
        ni = ci + didj[d][0]
        nj = cj + didj[d][1]
        # 1.1 점수 계산
        total_score += arr[ni][nj]
        arr[ni][nj] = 0
        ci = ni
        cj = nj

    #2. 몬스터들 꺼내오기
    monsters = []
    get_monster()

    #3. 몬스터 반복적으로 죽이기
    #3.1 점수 계산
    monsters = delete_monster(monsters[:])

    new_monsters = []
    visited = [0] * len(monsters)
    #4. 몬스터 같은 숫자끼리 짝 지어주기
    for i in range(len(monsters)):
        if visited[i] == 1:
            continue
        tmp_cnt = 1
        for j in range(i + 1, len(monsters)):
            if monsters[i] != monsters[j]:
                break
            if monsters[i] == monsters[j]:
                visited[j] = 1
                tmp_cnt += 1
        new_monsters.append(tmp_cnt)
        new_monsters.append(monsters[i])

    monsters = new_monsters

    #4.1 몬스터가 달팽이보다 크면 뒷부분 잘라주기
    monsters = monsters[:N*N]
    monsters = monsters[:len(monsters)] + [0] * (N*N-1 -len(monsters))

    #5. 몬스터 집어넣기
    put_monster()

print(total_score)
