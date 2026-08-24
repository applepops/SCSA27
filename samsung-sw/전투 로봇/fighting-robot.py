from collections import deque

def bfs (si, sj):

    q = deque()
    q.append((0, si, sj))
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    while q:
        cur_distance, cur_i, cur_j = q.popleft()

        if arr[cur_i][cur_j] != 0 and arr[cur_i][cur_j] < robot_level:
            monster_lst.append([cur_distance, cur_i, cur_j])


        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + cur_i
            nj = dj + cur_j

            #이동가능한 범위 내인지, 가본 적 없는지
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                #로봇보다 높은 레벨이 아닌지.. or 빈칸인지..
                if arr[ni][nj] <= robot_level:
                    q.append((cur_distance+1, ni, nj))
                    visited[ni][nj] = 1

    return

#격자판의 크기 N * N
N = int(input())

arr = [list(map(int, input().split())) for _ in range (N)]

#현재 나보다 낮은 레벨의 쥐어팰 수 있는 몬스터들을 담아두자.
#리스트로 [로봇과의 거리, i, j]순으로 요소들이 들어간다.
monster_lst = []
total_time = 0

robot_level = 2
killed_monster_cnt = 0

#초기값 설정하자.
#로봇은 초기에 2이다. 로봇보다 작은 레벨의 몬스터들 위치와
#로봇의 위치를 찾자.
for i in range (N):
    for j in range (N):
        if arr[i][j] == 9:
            robot_i, robot_j = i, j
            arr[robot_i][robot_j] = 0 #로봇 첫 위치 없애버린다. 걸리적거리니까.

while True:

    bfs(robot_i, robot_j)


    #거리가 가까운 순, 행 오름차순, 열 오름차순
    monster_lst = sorted(monster_lst, key = lambda x: (x[0], x[1], x[2]))

    if len(monster_lst) > 0:

        total_time += monster_lst[0][0] #시간 더해주기
        arr[monster_lst[0][1]][monster_lst[0][2]] = 0 #몬스터 없애주기

        #로봇 위치 갱신
        robot_i = monster_lst[0][1]
        robot_j = monster_lst[0][2]

        killed_monster_cnt += 1
        #본인 레벨과 같은 수의 몬스터를 없앨 때마다 레벨 업.
        if killed_monster_cnt == robot_level:
            robot_level += 1
            killed_monster_cnt = 0

        monster_lst = []

    #혹은 몬스터 리스트가 없다? 할 일이 없는 거다.
    else:
        break

print(total_time)

