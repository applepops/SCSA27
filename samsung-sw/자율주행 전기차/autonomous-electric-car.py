from collections import deque

# 자동차의 현재 위치를 입력으로 받는다.
def pick_customer(taxi_si, taxi_sj):

    q = deque()
    q.append((taxi_si, taxi_sj, 0))

    visited = [[0] * N for _ in range (N)]
    visited[taxi_si][taxi_sj] = 1

    min_distance_to_customer = float("inf")

    hubo = []

    while q:

        ci, cj, cd = q.popleft()

        #굳이 멀리 나가지 말자.
        if min_distance_to_customer < cd:
            continue

        #뽑은 놈이 승객의 위치다!
        if arr[ci][cj] < 0:
            if min_distance_to_customer >= cd:
                min_distance_to_customer = cd
                hubo.append((arr[ci][cj]*-1, ci, cj, cd))

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj
            #범위 내인지 체크
            if 0 <= ni < N and 0 <= nj < N:
                #가본 적 없는 곳이고 벽이 아니면
                if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                    q.append((ni, nj, cd + 1))
                    visited[ni][nj] = 1

    # 만약에 큐를 다 돌았는데 승객을 찾을 수가 없어서 후보가 비어버렸다면..
    # -1 출력 후 끝내.
    if not hubo: #손님을 하나도 못 찾았다.
        print(-1)
        exit()
    else:
        hubo = sorted(hubo, key=lambda x: (x[3], x[1], x[2]))
        # print(hubo)
        return hubo[0] #승객번호랑 위치랑 거리 반환한다.

    #주의: 현재 위치에 승객이 있을 수도 있으니까 처음 위치부터 큐에 넣어야 한다 헷갈리면 안됨.


#자동차의 현재위치랑 도착해야 하는 곳을 입력으로 받는다.
def go_dest(taxi_si, taxi_sj, dest_i, dest_j):

    #거리를 알아온다.
    q = deque()
    q.append((taxi_si, taxi_sj, 0))

    visited = [[0] * N for _ in range(N)]
    visited[taxi_si][taxi_sj] = 1

    while q:

        ci, cj, cd = q.popleft()

        if ci == dest_i and cj == dest_j:
            return cd #return한다.

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj
            #범위 내인지 체크
            if 0 <= ni < N and 0 <= nj < N:
                # 가본 적 없는 곳이고 벽이 아니면
                if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                    q.append((ni, nj, cd + 1))
                    visited[ni][nj] = 1

    # 근데 만약에 목적지가 가로막혀있어서 갈 수 없을지도 모르잖아.
    # -1을 return하자. 이동시킬 수 없는 경우니까.
    return -1


def custom_print():
    print("================")
    for row in arr:
        print(*row)
    print("================")

#입력 받기
#격자 크기, 승객의 수, 초기 배터리 충전량
N, M, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]

taxi_i, taxi_j = map(lambda x: int(x) - 1, input().split())
customer_dests = [[] for _ in range (M+1)]

for m in range (1, M+1):
    si, sj, ei, ej = map(lambda x: int(x) - 1, input().split()) #0-based로 맞추기
    arr[si][sj] = m*-1 #승객의 위치만 arr에 추가함.
    customer_dests[m].append(ei) #도착지는 여기에 기억함.
    customer_dests[m].append(ej)

#M번 반복한다.
for _ in range (M):
    #1. 승객을 고른다.
    c_n, c_i, c_j, c_d = pick_customer(taxi_i, taxi_j)

    #1.1 자동차 위치를 update한다.
    taxi_i = c_i
    taxi_j = c_j

    #1.2 거리만큼 배터리가 닳는다. -> 배터리가 0 혹은 음수면 -1을 출력하고 종료.
    C -= c_d
    if C <= 0:
        print(-1)
        exit()

    #1.3 array에 태운 승객 위치를 0으로 update한다.
    arr[c_i][c_j] = 0

    #1.4 고른 승객의 목적지를 알아온다.
    d_i, d_j = customer_dests[c_n][0], customer_dests[c_n][1]

    #2. 고른 승객을 승객의 목적지에 데려다준다. -> 목적지까지의 거리를 알아온다.
    d_d = go_dest(taxi_i, taxi_j, d_i, d_j)

    #2.0 -1을 리턴 받았다면 -1을 출력하고 종료. 목적지를 찾지 못했으니.
    if d_d == -1:
        print(-1)
        exit()

    #2.1 자동차 위치를 update한다.
    taxi_i = d_i
    taxi_j = d_j

    #2.2 거리만큼 배터리가 닳는다. 0이 되는 건 괜찮지만 음수가 되면 -1을 출력하고 종료.
    C -= d_d
    if C < 0:
        print(-1)
        exit()

    #3. 자동차 배터리를 충전한다.
    C += (d_d * 2)

    #다 했다.
    # custom_print()
    # print(f"현재 차 위치: {taxi_i}, {taxi_j}")
    # print(f"현재 차 남은 연료 {C}")

print(C)