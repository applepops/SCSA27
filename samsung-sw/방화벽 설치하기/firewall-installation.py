#방화벽을 제외하고 불이 퍼지지 않는 영역 크기의 최댓값
#전체 크기 - 방화벽 총 개수 - 불 퍼진 영역 개수가 가장 큰 것을 출력하자.
from collections import deque

def bfs ():
    q = deque()
    visited = [[0] * M for _ in range (N)]

    fire_cnt = 0

    for fire_i, fire_j in fires:
        q.append((fire_i, fire_j))
        visited[fire_i][fire_j] = 1

    while q:

        cur_i, cur_j = q.pop()
        fire_cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = cur_i + di
            nj = cur_j + dj

            #이동 가능한 좌표인가
            if 0 <= ni < N and 0 <= nj < M:
                #빈칸이면, 그리고 아직 불이 닿은 적 없으면.
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))

    return fire_cnt


N, M = map(int, input().split())

#영역 입력받기
arr = [list(map(int, input().split())) for _ in range (N)]

fires = [] #불들의 위치 기억하려고
walls = [] #기존 방화벽들의 위치 기억하려고
blanks = [] #얘가 방화벽이 될 후보지들이 된다.

max_cnt = 0

for i in range (N):
    for j in range (M):
        if arr[i][j] == 0:
            blanks.append((i, j))
        elif arr[i][j] == 1:
            walls.append((i, j))
        elif arr[i][j] == 2:
            fires.append((i, j))


for i in range (len(blanks)-2):
    for j in range (i+1, len(blanks)-1):
        for k in range (j+1, len(blanks)):
            #방화벽 추가하기...
            arr[blanks[i][0]][blanks[i][1]] = 1
            arr[blanks[j][0]][blanks[j][1]] = 1
            arr[blanks[k][0]][blanks[k][1]] = 1

            res = bfs()
            #전체 영역 크기 - 불 붙은 영역 - 방화벽이 있는 영역 = 불 안 퍼진 영역
            temp = N*M - res - (len(walls) + 3)
            max_cnt = max(temp, max_cnt)

            #다시 빈칸으로 되돌리기...
            arr[blanks[i][0]][blanks[i][1]] = 0
            arr[blanks[j][0]][blanks[j][1]] = 0
            arr[blanks[k][0]][blanks[k][1]] = 0

print(max_cnt)