from collections import deque

didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def update_knight_arr():
    global knights_arr

    new_knights_arr = [[0] * N for _ in range (N)]
    for m in knights_info.keys():
        si, sj, h, w = knights_info[m]
        for i in range (si, si+h):
            for j in range (sj, sj+w):
                new_knights_arr[i][j] = m

    knights_arr = new_knights_arr

def find_related_knights(knight_num, d):

    related_knights = set()

    q = deque()
    visited = [[0] * N for _ in range (N)]
    si, sj, h, w = knights_info[knight_num]
    for i in range(si, si + h):
        for j in range(sj, sj + w):
            visited[i][j] = 1
            q.append([i, j, knight_num])

    while q:
        ci, cj, cnum = q.popleft()
        related_knights.add(cnum)

        ni = didj[d][0] + ci
        nj = didj[d][1] + cj

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and knights_arr[ni][nj] != 0:
            new_kn = knights_arr[ni][nj]
            si, sj, h, w = knights_info[new_kn]

            for i in range(si, si + h):
                for j in range(sj, sj + w):
                    visited[i][j] = 1
                    q.append([i, j, new_kn])

    return list(related_knights)

def check_movable(klst, d):
    for k in klst:
        si, sj, h, w = knights_info[k]
        si = si + didj[d][0]
        sj = sj + didj[d][1]

        for i in range(si, si + h):
            for j in range(sj, sj + w):
                if not (0 <= i < N and 0 <= j < N) or arr[i][j] == 2:
                    return False
    else:
        return True

def move(klst, d):
    for k in klst:
        si, sj, h, w = knights_info[k]
        si = si + didj[d][0]
        sj = sj + didj[d][1]
        knights_info[k] = [si, sj, h, w]

def get_damage(klst, knum):

    for k in klst:
        #명령 받은 기사는 넘어가
        if k == knum:
            continue
        si, sj, h, w = knights_info[k]
        for i in range(si, si + h):
            for j in range(sj, sj + w):
                if arr[i][j] == 1:
                    knights_blood[k] -= 1

    #체력 다 닳은 애들 없애기
    for k in list(knights_blood.keys()):
        if knights_blood[k] <= 0:
            knights_blood.pop(k)
            knights_info.pop(k)

#격자 크기, 기사 수, 명령 수
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
knights_info = dict()
knights_blood = dict()
knights_arr = [[0] * N for _ in range (N)]

for m in range (1, M+1):
    si, sj, h, w, blood = map(int, input().split())
    knights_info[m] = [si-1, sj-1, h, w]
    knights_blood[m] = blood

update_knight_arr()
copied_knights_blood = knights_blood.copy()

for k in range (K):
    knight_num, d = map(int, input().split())

    #없는 기사에 대한 명령이 들어올 수 있으니까.
    if knights_info.get(knight_num):
        lst = find_related_knights(knight_num, d)

        #움직일 수 있다.
        if check_movable(lst, d):
            # print(True)
            move(lst, d)
            # print("이동 후")
            # for row in knights_arr:
            #     print(*row)
            # print()
            get_damage(lst, knight_num)
            update_knight_arr()
            # print(knights_blood)
            # print(copied_knights_blood)

ans = 0
for k in knights_blood.keys():
    original_blood = copied_knights_blood[k]
    remained_blood = knights_blood[k]

    ans += original_blood - remained_blood

print(ans)
