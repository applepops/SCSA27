from collections import deque

N, M, Q = map(int, input().split())
arr = []
for _ in range (N):
    tmp_q = deque(list(map(int, input().split())))
    arr.append(tmp_q)

for _ in range (Q):
    checked = [[False] * M for _ in range (N)]
    x, d, k = map(int, input().split())

    if d == 0:
        d = 1
    else:
        d = -1

    #회전하기
    for wonpan in range (N):
        if (wonpan+1) % x == 0:
            for _ in range (k):
                arr[wonpan].rotate(d)

    #지우기
    for i in range (N):
        for j in range (M):
            if arr[i][j] == 0:
                continue
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = di + i
                nj = (dj + j) % M

                if 0 <= ni < N:
                    if arr[i][j] == arr[ni][nj]:
                        checked[i][j] = True
                        checked[ni][nj] = True
    erased_cnt = 0
    for i in range (N):
        for j in range (M):
            if checked[i][j]:
                arr[i][j] = 0
                erased_cnt += 1

    if erased_cnt == 0:
        #정규화 실시
        #원판에 남은 수가 없으면 진행 ㄴ
        if sum(map(sum, arr)) == 0:
            continue

        total_sum = 0
        total_cnt = 0

        for i in range (N):
            for j in range (M):
                if arr[i][j] != 0:
                    total_sum += arr[i][j]
                    total_cnt += 1

        average = total_sum // total_cnt
        for i in range (N):
            for j in range (M):
                if arr[i][j] != 0:
                    if arr[i][j] > average:
                        arr[i][j] -= 1
                    elif arr[i][j] < average:
                        arr[i][j] += 1

print(sum(map(sum, arr)))