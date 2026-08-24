from collections import deque
from heapq import heappop, heappush

def bfs (si, sj):

    global robot_i
    global robot_j

    hq = []
    heappush(hq, (0, si, sj))
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    while hq:

        cur_distance, cur_i, cur_j = heappop(hq)

        if arr[cur_i][cur_j] != 0 and arr[cur_i][cur_j] < robot_level:
            arr[cur_i][cur_j] = 0 #몬스터 없애주기
            robot_i = cur_i #로봇 위치 재계산
            robot_j = cur_j

            return cur_distance

        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni = di + cur_i
            nj = dj + cur_j

            #이동가능한 범위 내인지, 가본 적 없는지
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                #로봇보다 높은 레벨이 아닌지.. or 빈칸인지..
                if arr[ni][nj] <= robot_level:
                    heappush(hq, (cur_distance+1, ni, nj))
                    visited[ni][nj] = 1

    #큐를 다 돌아도 그 몬스터에 도달할 수 없으면 걍 inf 반환
    return float("INF")

#현재 로봇 레벨보다 낮은 몬스터들 좌표 찾기
def find_monster_not_big_as_robot():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and arr[i][j] < robot_level:
                monster_lst.append([float("INF"), i, j])

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

    new_distance = bfs(robot_i, robot_j)

    if new_distance !=  float("INF"):
        total_time += new_distance

        killed_monster_cnt += 1
        # 본인 레벨과 같은 수의 몬스터를 없앨 때마다 레벨 업.
        if killed_monster_cnt == robot_level:
            robot_level += 1
            killed_monster_cnt = 0
    else:
        break

print(total_time)
