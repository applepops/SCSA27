# from pprint import pprint
N, M, K = map(int, input().split())

yangboon = [list(map(int, input().split())) for _ in range (N)]
current_yangboon = [[5] * N for _ in range (N)]
virus_arr = [[[] for _ in range (N)] for _ in range (N)]

for _ in range (M):
    r, c, age = map(int, input().split())
    r, c = r-1, c-1
    virus_arr[r][c].append(age)

for k in range (K):

    virus_5 = []

    for i in range (N):
        for j in range (N):
            if virus_arr[i][j]:
                now_virus = virus_arr[i][j]
                dead_virus = []
                new_virus = []

                for v in now_virus:
                    if current_yangboon[i][j] >= v:
                        new_virus.append(v+1)
                        current_yangboon[i][j] -= v
                        if (v+1) % 5 == 0:
                            virus_5.append([i, j])
                    else:
                        dead_virus.append(v)

                virus_arr[i][j] = new_virus

                for v in dead_virus:
                    current_yangboon[i][j] += v//2

    for ci, cj in virus_5:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                virus_arr[ni][nj].insert(0, 1)

    for i in range (N):
        for j in range (N):
            current_yangboon[i][j] += yangboon[i][j]

    # print(f"{k}턴 종료 후:")
    # pprint(virus_arr)
    # print()
    # pprint(current_yangboon)

ans = 0
for i in range (N):
    for j in range (N):
        ans += len(virus_arr[i][j])

print(ans)