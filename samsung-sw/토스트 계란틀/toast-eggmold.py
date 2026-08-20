from collections import deque

def bfs(start_i, start_j):

    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = 1

    eggs_cnt = arr[start_i][start_j]

    #현재 이 계란틀과 연결되어야 하는 계란틀들을 저장하는 array
    temp = [(start_i, start_j)]

    while q:
        cur_i, cur_j = q.popleft()

        #상하좌우
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni = cur_i + di
            nj = cur_j + dj

            #이동 가능한 좌표인지
            if 0 <= ni < N and 0 <= nj < N:
                #미방문 좌표인지
                if visited[ni][nj] == 0:
                    #현재 좌표 - 옆좌표 계란 양 차이 확인
                    if L <= abs(arr[ni][nj] - arr[cur_i][cur_j]) <= R:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        temp.append((ni, nj))
                        eggs_cnt += arr[ni][nj]


    #계란 이동처리를 시킬 필요가 없다면..
    if len(temp) <= 1:
        return False
    else:
        #편의상 소숫점은 버립니다.
        new_eggs_cnt = eggs_cnt // len(temp)
        # print(temp)
        #계란틀별 계란의 양 조정해주기
        for x, y in temp:
            arr[x][y] = new_eggs_cnt

        return True


#N*N, L은 최솟값, R은 최댓값(포함)
N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]

move_cnt = 0

while True:

    visited = [[0] * N for _ in range (N)]
    is_moved = False

    for i in range (N):
        for j in range (N):
            #처리되지 않은 좌표면 bfs 진행
            if visited[i][j] == 0:
                res = bfs(i, j)
                if res:
                    is_moved = True

    #계란 한 판을 싹 돌면서
    #계란의 이동이 한 번이라도 있었으면
    if is_moved:
        move_cnt += 1
    #계란의 이동이 한 번도 없었으면
    else:
        break

    #시간초과날까봐 보험
    if move_cnt >= 2000:
        break

# print(arr)
print(move_cnt)