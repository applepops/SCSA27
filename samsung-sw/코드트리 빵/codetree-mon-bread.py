#문제를 받아들이자.
#문제를 이해하고 구상하자.
#다... 할 수 있어....
from collections import deque

def go_gs25(i, j, gs25i, gs25j):
    q = deque()
    q.append([i, j, 0])

    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while q:
        ci, cj, cd = q.popleft()
        if (ci, cj) == (gs25i, gs25j):
            return cd

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            # 갈 수 있는 곳인지, 미방문인지, 격자 내인지.
            if 0 <= ni < N and 0 <= nj < N and cant_go_arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj, cd + 1])

    #도착 못하는 경우는 최댓값을 넣을게.
    return float("inf")


def find_basecamp(i, j): #편의점 위치가 들어간다.
    q = deque()
    q.append([i, j, 0])

    visited = [[0] * N for _ in range (N)]
    visited[i][j] = 1

    min_distance = float("inf")
    hubo = []

    while q:
        ci, cj, cd = q.popleft()

        #꺼낸 놈이 베이스 캠프다.
        if arr[ci][cj] == 1:
            if min_distance > cd:
                hubo = [] #초기화해줄 거임.
                hubo.append([ci, cj])
                min_distance = cd
            elif min_distance == cd: #같은 애들은 넣어주고.
                hubo.append([ci, cj])
            else:
                continue #그냥 지나갈 거임. 너무 먼 애들만 남아있겠지.

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            #갈 수 있는 곳인지, 미방문인지, 격자 내인지.
            if 0 <= ni < N and 0 <= nj < N and cant_go_arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj, cd + 1])

    #베이스 캠프 개수는 무조건 m개 이상이니까
    #후보가 무조건 있기는 할 거임.
    hubo = sorted(hubo, key=lambda x: (x[0], x[1]))#행과 열이 작은 순.
    return hubo[0][0], hubo[0][1] #도착해야 하는 베이스캠프 위치를 반환한다.

#입력받기
#격자의 크기, 사람의 수
N, M = map(int, input().split())

#빈칸은 0, 베이스캠프는 1
arr = [list(map(int, input().split())) for _ in range (N)]

#편의점 위치들 저장할 건데 0은 더미. 사람에 맞추려고.
gs25_ijs = [] #1부터 돌아라.
gs25_ijs.append([-1, -1])

for _ in range (M):
    i, j = map(lambda x: int(x)-1, input().split())
    gs25_ijs.append([i, j])

#사람 위치 저장할 건데 0은 더미.
people_ijs = [[-1, -1] for _ in range (M+1)] #1부터 돌아라.
#시간
t = 0
#못 지나가는 곳 표시할 거임. 0은 지나갈 수 있음. 1은 못 지나감.
cant_go_arr = [[0] * N for _ in range (N)]
#사람들 도착했는지 여부를 저장할 거임.
did_people_arrive = [False] * (M+1) #0은 더미. #1부터 돌아라.

didj = [[-1, 0], [0, -1], [0, 1], [1, 0]] #위 왼 오 아래 순으로 우선순위

while True:
    t += 1

    # print(f"{t}회차, 사람은 지금 여기 있다.")
    # print(people_ijs)

    #매턴마다 생기는 애. 못 지나가는 좌표들을 임시 저장하고 마지막에 싹 저장.
    tmp_cant_go_lst = []

    #[1] 도착 안한 사람들 모두 원하는 편의점 방향으로 1씩 이동.
    #    이동 후 그 사람 위치 갱신해주기
    for i in range (1, M+1):
        if did_people_arrive[i] == False and (people_ijs[i][0], people_ijs[i][1]) != (-1, -1): #아직 도착 안한 사람이면 한 번 가야지, 아직 베캠 안 간 사람이면 pass
            distances = []
            for d in range (4):#내 위치에서 한 칸 이동한 거랑 편의점 위치를 보낸다.
                if 0 <= people_ijs[i][0] + didj[d][0] < N and 0 <= people_ijs[i][1] + didj[d][1] < N and cant_go_arr[people_ijs[i][0] + didj[d][0]][people_ijs[i][1] + didj[d][1]] == 0: #[주의]: 또 빼먹음 미친놈.
                    res = go_gs25(people_ijs[i][0] + didj[d][0], people_ijs[i][1] + didj[d][1], gs25_ijs[i][0], gs25_ijs[i][1])
                    distances.append(res)
                else:
                    distances.append(float("inf"))
            min_distance = min(distances)

            # print(f"{i}번째 인간")
            # print(distances)

            real_d = distances.index(min_distance)

            #위치 갱신
            people_ijs[i][0], people_ijs[i][1] = people_ijs[i][0] + didj[real_d][0], people_ijs[i][1] + didj[real_d][1]

            #[2] 편의점에 도착한 경우에 갈 수 없는 위치 추가해주기.
            #    그 사람도 도착했다고 표시해주기
            if (people_ijs[i][0], people_ijs[i][1]) == (gs25_ijs[i][0], gs25_ijs[i][1]):
                did_people_arrive[i] = True
                tmp_cant_go_lst.append([gs25_ijs[i][0], gs25_ijs[i][1]]) #[주의] 또 빼먹었다. 미친놈.

    #[4] 못 지나가는 칸 추가해주기 #여기에도 넣어보자. 순서가 어케되는건지 헷갈린다.
    for i, j in tmp_cant_go_lst:
        cant_go_arr[i][j] = 1

    #[3] t번 사람이 원하는 편의점에 가까운 베이스 캠프 찾기
    #    그 사람 위치 갱신해주기
    #    갈 수 없는 위치 추가해주기
    if t <= M:
        new_i, new_j = find_basecamp(gs25_ijs[t][0], gs25_ijs[t][1])
        people_ijs[t][0], people_ijs[t][1] = new_i, new_j #갱신

        tmp_cant_go_lst.append([new_i, new_j])

    # print("도착여부")
    # print(did_people_arrive)

    #[4] 못 지나가는 칸 추가해주기
    for i, j in tmp_cant_go_lst:
        cant_go_arr[i][j] = 1
    #
    # for row in cant_go_arr:
    #     print(*row)

    #[5] 다들 도착했는지 확인 한 번 해주고 다 도착했으면 while문 끝내기
    #    다들 아직 안 도착했으면 계속 돌기
    flag = 0
    for p in range (1, M+1):
        if did_people_arrive[p] == False:
            flag = 1

    if flag == 0: #다 도착해부렀어.
        break

print(t)