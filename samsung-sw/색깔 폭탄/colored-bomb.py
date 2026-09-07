from collections import deque

#가장 큰 폭탄묶음을 찾는 bfs
def find_bomb_groups(si, sj):
    global max_group_cnt
    global bomb_groups

    q = deque()
    q.append([si, sj])
    visited[si][sj] = 1

    cur_group_cnt = 0
    cur_bomb_group = []

    while q:
        ci, cj = q.popleft()
        cur_group_cnt += 1
        if arr[ci][cj] != 0:
            cur_bomb_group.append([ci, cj])

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = ci + di
            nj = cj + dj

            #범위 내인지, 방문한 적 없는 곳인지.
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                #시작 지점이랑 같은 색 폭탄이든가 아니면 빨간 폭탄이든가.
                if arr[si][sj] == arr[ni][nj] or arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni, nj])

    cur_bomb_group = sorted(cur_bomb_group, key=lambda x: (-x[0], x[1]))


    #크기 갱신
    if cur_group_cnt > max_group_cnt:
        max_group_cnt = cur_group_cnt
        bomb_groups = []
        bomb_groups.append(cur_bomb_group)
    elif cur_group_cnt == max_group_cnt:
        bomb_groups.append(cur_bomb_group)

def delete_bombs(si, sj):
    q = deque()
    q.append([si, sj])

    visited_d = [[0] * N for _ in range (N)]
    visited_d[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited_d[ni][nj] == 0:
                #시작 지점이랑 같은 색 폭탄이든가 아니면 빨간 폭탄이든가.
                if arr[si][sj] == arr[ni][nj] or arr[ni][nj] == 0:
                    arr[ni][nj] = -2 #빈곳으로 만들어주기
                    q.append([ni, nj])
                    visited_d[ni][nj] = 1

    arr[si][sj] = -2 #본인도..


#중력작용하는 함수
def drop_bombs():
    for _ in range (N): #최대 N번 떨어지겠죠.
        for j in range (0, N):
            for i in range (N-1, 0, -1):
                if arr[i][j] == -2 and arr[i-1][j] != -1: #빈칸이고 떨어질 애가 검은 돌이 아니면, 떨어져.
                    arr[i][j] = arr[i-1][j]
                    arr[i-1][j] = -2
                elif arr[i][j] == -1:
                    continue


def back_red_bombs():
    for i, j in red_bombs:
        visited[i][j] = 0

def print_arr():
    for row in arr:
        print(*row)

#입력받기
#격자의 크기, 서로 다른 폭탄의 종류 1-M
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
total_score = 0

#반복합니다.. 더 이상 폭탄 묶음이 없을 때까지...
while True:
    max_group_cnt = 0

    #0. 빨간색 폭탄들의 위치를 기억한다.
    #왜냐하면.. visited를 돌려줘야 하기 때문에. 어디든 속할 수 있는 애라서.
    red_bombs = []
    for i in range (N):
        for j in range (N):
            if arr[i][j] == 0:
                red_bombs.append([i, j])


    visited = [[0] * N for _ in range (N)]
    bomb_groups = []

    #1.가장 큰 폭탄묶음(들)을 찾는다 -> bfs
    # 1-M의 폭탄들에 대해서만 bfs를 보낼 예정임,
    for i in range (N):
        for j in range (N):
            if 1 <= arr[i][j] <= M and visited[i][j] == 0: #검은 돌 아니고 빨간 폭탄 아닌 폭탄들에 대해서만.
                find_bomb_groups(i, j)
                back_red_bombs()


    #만약에 다 돌면서 폭탄묶음들을 찾았는데 그게 겨우 1짜리밖에 없다면..   -> 탈출
    if max_group_cnt <= 1:
        break

    #2. 폭탄묶음을 선택한다.(기준은 빨간색이 가장 적은 것, 그 다음은 행이 큰 것, 그 다음은 열이 적은 것)
    # 일단 bomb_groups에 있는 애들은 전체 폭탄묶음 개수는 같은 애들이다.
    # 근데 골라야 하는 건 어떤 녀석이 빨간색이 제일 적으냐 그게 우선이다.
    # bomb_groups를 순회하면서 len의 max를 구한다.
    max_cnt_without_red = 0
    for i in bomb_groups:
        max_cnt_without_red = max(max_cnt_without_red, len(i))

    tmp = []
    for i in range (len(bomb_groups)):
        if len(bomb_groups[i]) == max_cnt_without_red:
            tmp.append(bomb_groups[i][0])

    tmp = sorted(tmp, key=lambda x: (-x[0], x[1]))

    #3. 선택한 폭탄묶음을 제거한다. 기준점을 보낼 것이다. 빈곳으로 만드는 건 -2로 할까 한다.
    delete_bombs(tmp[0][0], tmp[0][1])

    #3.1. 점수를 계산한다. += 폭탄묶음의 폭탄 개수 * 폭탄묶음의 폭탄 개수
    total_score += max_group_cnt * max_group_cnt

    #4. 중력을 작용한다. (돌은 중력 영향 안 받는다.)
    drop_bombs()



    #5. 반시계 방향 90도 회전한다.
    arr =[list(row) for row in zip(*arr)][::-1]

    #6. 다시 중력을 작용한다. (돌은 중력 영향 안 받는다.)
    drop_bombs()


print(total_score)