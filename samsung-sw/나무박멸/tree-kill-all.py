# 1. 나무의 성장
def grow ():
    for i in range (N):
        for j in range (N):
            near_tree_cnt = 0
            if arr[i][j] >= 1:

                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni = di + i
                    nj = dj + j
                    #범위 내인지
                    if 0 <= ni < N and 0 <= nj < N:
                        #나무가 있는 곳인지
                        if arr[ni][nj] >= 1:
                            near_tree_cnt += 1
            arr[i][j] += near_tree_cnt


# 2. 나무의 번식
# 조건은 벽, 다른 나무, 제초제가 없는 칸
def spread():
    add_tree_arr = [[0] * N for _ in range (N)]

    for i in range (N):
        for j in range (N):
            put_tree_ij = []
            #나무를 찾아
            if arr[i][j] >= 1:
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni = di + i
                    nj = dj + j
                    # 범위 내인지
                    if 0 <= ni < N and 0 <= nj < N:
                        # 다른 나무나 벽이 없는 곳인지 + 제초제가 없는 곳인지
                        if arr[ni][nj] == 0 and jecho_arr[ni][nj] == 0:
                            put_tree_ij.append((ni, nj))

            for t in range (len(put_tree_ij)):
                add_tree_arr[put_tree_ij[t][0]][put_tree_ij[t][1]] += arr[i][j] // len(put_tree_ij)

    for i in range (N):
        for j in range (N):
            arr[i][j] += add_tree_arr[i][j]

# 3. 제초제 뿌리기
# 나무 박멸...
def pick_jecho():
    global total_killed_tree

    #제초제가 들어갈 초기 위치
    jecho_i = 0
    jecho_j = 0
    max_killed_tree = 0

    for i in range (N):
        for j in range (N):
            cur_killed_tree = 0
            #제초제를 뿌리는 곳에 나무가 아예 없는 경우.
            if arr[i][j] == 0:
                continue
            #제초제를 뿌리는 곳에 나무가 있으면..
            elif arr[i][j] >= 1:
                cur_killed_tree += arr[i][j]
                for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for k in range(1, K+1):
                        ni = di * k + i
                        nj = dj * k + j
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == -1 or arr[ni][nj] == 0:
                                break
                            else:
                                cur_killed_tree += arr[ni][nj]
            #제초제를 벽에 어떻게 뿌리니.
            else:
                continue

            if cur_killed_tree > max_killed_tree:
                max_killed_tree = cur_killed_tree
                jecho_i = i
                jecho_j = j

    total_killed_tree += max_killed_tree
    return jecho_i, jecho_j

def spread_jecho(si, sj):

    jecho_arr[si][sj] = C
    arr[si][sj] = 0

    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for k in range(1, K+1):
            ni = di * k + si
            nj = dj * k + sj

            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == -1 or arr[ni][nj] == 0:
                    jecho_arr[ni][nj] = C
                    break
                else:
                    jecho_arr[ni][nj] = C
                    arr[ni][nj] = 0


N, M, K, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]
jecho_arr = [[0] * N for _ in range (N)]

total_killed_tree = 0

for m in range (M):
    grow()
    spread()
    ji, jj = pick_jecho()
    #제초제가 닳는다..
    for i in range (N):
        for j in range (N):
            if jecho_arr[i][j] >= 1:
                jecho_arr[i][j] -= 1
    spread_jecho(ji, jj)


print(total_killed_tree)