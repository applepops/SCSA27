didj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
ci, cj, cdir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
visited = [[0] * M for _ in range (N)]

#[기초공사]
visited[ci][cj] = 1
cnt = 0

while True:

    #4번 다 돌았는데...
    if cnt >= 4:
        tmp_dir = (cdir + 2) % 4

        ni = didj[tmp_dir][0] + ci
        nj = didj[tmp_dir][1] + cj

        if arr[ni][nj] == 1:
            break
        else:
            ci, cj = ni, nj
            cnt = 0

    else:

        #좌회전으로 틀어...
        cdir = (cdir - 1) % 4
        ni = didj[cdir][0] + ci
        nj = didj[cdir][1] + cj


        #갈 수 있는 경우
        if visited[ni][nj] == 0 and arr[ni][nj] == 0:
            visited[ni][nj] = 1
            cnt = 0
            ci, cj = ni, nj

        #갈 수 없는 경우
        else:
            cnt += 1
# 
# for row in visited:
#     print(*row)

print(sum(map(sum, visited)))