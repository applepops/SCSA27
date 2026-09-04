#나는 이미 풀었다.
from collections import deque

def bfs(si, sj, cur_group_num):
    q = deque()
    q.append((si, sj))

    groups[si][sj] = cur_group_num
    cur_group_cnt = 0

    while q:

        ci, cj = q.popleft()
        cur_group_cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and groups[ni][nj] == 0 and arr[si][sj] == arr[ni][nj]:
                groups[ni][nj] = cur_group_num
                q.append((ni, nj))


    return cur_group_cnt #지금 만들어진 그룹 안의 요소 개수를 돌려준다.



def make_groups():

    cur_group_num = 0

    for i in range (N):
        for j in range (N):
            if groups[i][j] == 0:
                cur_group_num += 1
                res = bfs(i, j, cur_group_num)
                in_group_cnt.append(res)
                in_group_num.append(arr[i][j])


def print_groups():
    for row in groups:
        print(*row)

#입력받기
# 판의 크기
N = int(input())

arr = [list(map(int, input().split())) for _ in range (N)]
total_score = 0

#초기 예술 점수 구하기

in_group_cnt = [0] #그룹 안에 요소가 각각 몇 개인지., 맨 앞은 더미
in_group_num = [0] #그룹 안을 채우는 숫자가 각각 뭔지., 맨 앞은 더미
groups = [[0] * N for _ in range (N)] #그룹 만들 때마다 선언해줘야 됨.

#1. 그룹을 만든다.
make_groups()

#2. 접한 부분들을 알아낸다.
close_to = [[0] * len(in_group_num) for _ in range (len(in_group_num))]

for i in range (N):
    for j in range (N):
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N:
                if arr[i][j] != arr[ni][nj]:
                    close_to[groups[i][j]][groups[ni][nj]] += 1

#3. 예술성 점수를 계산해서 total score 갱신한다.
for i in range (1, len(in_group_num)-1):
    for j in range (i+1, len(in_group_num)):
        if close_to[i][j] > 0:
            total_score += (in_group_cnt[i] + in_group_cnt[j]) * in_group_num[i] * in_group_num[j] * close_to[i][j]
            #print(f"그룹 {i}랑 {j} 더해서 {total_score} 갱신")

for _ in range (3):
#3번 회전하고 점수 구하자.
#1. 가로 세로 중앙 애들 반시계 방향으로 바꿔주기
    garo = []
    sero = []
    for j in range (N):
        garo.append(arr[N//2][j])
    garo.reverse()

    for i in range (N):
        sero.append(arr[i][N//2])

    #세로를 가로 자리에 넣어주기
    arr[N//2] = sero[:]
    #가로를 세로 자리에 넣어주기
    for i in range (N):
        arr[i][N//2] = garo[i]

    #2. 그외 곁다리 네모들 90도 회전해주기
    #1번 네모(왼위)
    tmp_arr = [row[0:N//2] for row in arr[0: N//2]]
    tmp_arr = list(zip(*tmp_arr))
    for i in range (len(tmp_arr)):
        tmp_arr[i] = list(tmp_arr[i])
    tmp_arr_90 = []
    for row in tmp_arr:
        tmp_arr_90.append(row[::-1])
    for i in range (0, N//2):
        for j in range (0, N//2):
            arr[i][j] = tmp_arr_90[i][j]

    #2번 네모(왼아래)
    tmp_arr = [row[0:N//2] for row in arr[N//2+1: N]]
    tmp_arr = list(zip(*tmp_arr))
    for i in range (len(tmp_arr)):
        tmp_arr[i] = list(tmp_arr[i])
    tmp_arr_90 = []
    for row in tmp_arr:
        tmp_arr_90.append(row[::-1])
    for i in range (N//2+1, N):
        for j in range (0, N//2):
            arr[i][j] = tmp_arr_90[i-(N//2+1)][j]

    #3번 네모(우위)
    tmp_arr = [row[N//2+1: N] for row in arr[0:N//2]]
    tmp_arr = list(zip(*tmp_arr))
    for i in range (len(tmp_arr)):
        tmp_arr[i] = list(tmp_arr[i])
    tmp_arr_90 = []
    for row in tmp_arr:
        tmp_arr_90.append(row[::-1])
    for i in range (0, N//2):
        for j in range (N//2+1, N):
            arr[i][j] = tmp_arr_90[i][j-(N//2+1)]

    #4번 네모(우아래)
    tmp_arr = [row[N//2+1: N] for row in arr[N//2+1: N]]
    tmp_arr = list(zip(*tmp_arr))
    for i in range (len(tmp_arr)):
        tmp_arr[i] = list(tmp_arr[i])
    tmp_arr_90 = []
    for row in tmp_arr:
        tmp_arr_90.append(row[::-1])
    for i in range (N//2+1, N):
        for j in range (N//2+1, N):
            arr[i][j] = tmp_arr_90[i-(N//2+1)][j-(N//2+1)]

    #회전 후 예술 점수 구하기
    in_group_cnt = [0]  # 그룹 안에 요소가 각각 몇 개인지., 맨 앞은 더미
    in_group_num = [0]  # 그룹 안을 채우는 숫자가 각각 뭔지., 맨 앞은 더미
    groups = [[0] * N for _ in range(N)]  # 그룹 만들 때마다 선언해줘야 됨.

    #1. 그룹을 만든다.
    make_groups()

    #2. 접한 부분들을 알아낸다.
    close_to = [[0] * len(in_group_num) for _ in range (len(in_group_num))]

    for i in range (N):
        for j in range (N):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N:
                    if arr[i][j] != arr[ni][nj]:
                        close_to[groups[i][j]][groups[ni][nj]] += 1

    #3. 예술성 점수를 계산해서 total score 갱신한다.
    for i in range (1, len(in_group_num)-1):
        for j in range (i+1, len(in_group_num)):
            if close_to[i][j] > 0:
                total_score += (in_group_cnt[i] + in_group_cnt[j]) * in_group_num[i] * in_group_num[j] * close_to[i][j]


print(total_score)