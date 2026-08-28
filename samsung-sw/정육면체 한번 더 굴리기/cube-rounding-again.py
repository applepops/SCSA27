from collections import deque

#오른, 아래, 왼, 위 순서로..
#시계방향으로 가야하면 +1이고 반시계방향이면 -1이고 반대방향이면 +2
didj = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move_dice (lst, way):
    #오른
    if way == 0:
        new_list = [lst[2], lst[3], lst[1], lst[0], lst[4], lst[5]]
    #아래
    elif way == 1:
        new_list = [lst[5], lst[4], lst[2], lst[3], lst[0], lst[1]]
    #왼
    elif way == 2:
        new_list = [lst[3], lst[2], lst[0], lst[1], lst[4], lst[5]]
    #위
    elif way == 3:
        new_list = [lst[4], lst[5], lst[2], lst[3], lst[1], lst[0]]

    else:
        return

    return new_list

def bfs (si, sj):

    global score

    q = deque()
    q.append((si, sj))
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    tmp_cnt = 0

    while q:
        ci, cj = q.popleft()
        tmp_cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[si][sj] == arr[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

    score += tmp_cnt * arr[si][sj]
    return


#초기 주사위의 상태
#순서대로 위, 아래, 왼, 오른, 앞, 뒤에 있는 숫자임.
dice = [1, 6, 4, 3, 2, 5]
#초기 이동 방향: 오른쪽
cur_dir = 0
#초기 주사위 좌표: 0,0
nr, nc = 0, 0

#N*N판, M은 횟수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

score = 0

for _ in range (M):

    # 주사위의 좌표 업데이트
    nr = nr + didj[cur_dir][0]
    nc = nc + didj[cur_dir][1]

    if 0 <= nr < N and 0 <= nc < N:
        # 주사위의 굴리기
        dice = move_dice(dice, cur_dir)

        # 점수얻기
        bfs(nr, nc)

        # 비교하기 -> 방향 업데이트
        if dice[1] > arr[nr][nc]:
            cur_dir = (cur_dir + 1) % 4 #시계방향 회전
        elif dice[1] < arr[nr][nc]:
            cur_dir = (cur_dir -1) % 4 #반시계방향 회전

    #이동좌표가 갈 수 없는 곳이다..
    else:
        #방향 정반대로 바꾸기
        cur_dir = (cur_dir + 2) % 4

        #그 방향으로 두 번 가야됨.
        nr = nr + didj[cur_dir][0] * 2
        nc = nc + didj[cur_dir][1] * 2

        # 주사위의 굴리기
        dice = move_dice(dice, cur_dir)

        # 점수얻기
        bfs(nr, nc)

        # 비교하기 -> 방향 업데이트
        if dice[1] > arr[nr][nc]:
            cur_dir = (cur_dir + 1) % 4  # 시계방향 회전
        elif dice[1] < arr[nr][nc]:
            cur_dir = (cur_dir - 1) % 4  # 반시계방향 회전


print(score)

