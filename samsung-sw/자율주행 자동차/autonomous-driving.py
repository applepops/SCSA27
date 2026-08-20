from collections import deque

#격자의 위아래양옆은 모두 인도로 둘러싸져있다. -> 이동가능한 좌표인지 확인 안해도 되려나

#북: 0, 동: 1, 남: 2, 서: 3
#현재 방향을 기준으로 왼쪽 방향으로 가려면 방향벡터를 -1처리 하면 됨.
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs():

    q = deque()
    #row 좌표, col 좌표, 현재 방향, 방향 바꾼 횟수 이렇게 큐에 넣을 거임.
    q.append((start_i, start_j, start_dir, 0))

    #초기 상태의 방문면적은 일단 1이 된다.
    visited[start_i][start_j] = 1

    while q:

        cur_i, cur_j, cur_dir, dir_cnt = q.pop()

        if dir_cnt == 4:
            #한 바퀴 다 돌았는데도 못 간다?
            #현재 방향 기준으로 한 칸 후진한다.
            ni = cur_i + di[(cur_dir - 2) % 4]
            nj = cur_j + dj[(cur_dir - 2) % 4]

            #인도가 아니면?
            if arr[ni][nj] != 1:
                #dir_cnt 초기화
                q.append((ni, nj, cur_dir, 0))
                visited[ni][nj] = 1
            #못 가면?
            else:
                #함수 끝내버려.. 이제 그만
                return

        else:
            # 현재 방향 기준 왼쪽 방향의 다음 블럭
            ni = cur_i + di[(cur_dir - 1) % 4]
            nj = cur_j + dj[(cur_dir - 1) % 4]

            #현재방향 기준 왼쪽 방향으로 간 적 없는 경우, 인도가 아닌 경우
            if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                visited[ni][nj] = 1
                q.append((ni, nj, (cur_dir-1)%4, 0))

            #현재방향 기준 왼쪽 방향으로 간 적 있거나 인도라서 못 가는 경우
            elif visited[ni][nj] == 1 or arr[ni][nj] == 1:
                #cur_dir -1해주고 dir_cnt+1해서 다시 큐에 넣어준다.
                q.append((cur_i, cur_j, (cur_dir-1)%4, dir_cnt+1))




N, M = map(int, input().split())
start_i, start_j, start_dir = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]
visited = [[0] * M for _ in range (N)]

bfs()
ans = 0

for i in range (N):
    for j in range (M):
        if visited[i][j] == 1:
            ans += 1

print(ans)
