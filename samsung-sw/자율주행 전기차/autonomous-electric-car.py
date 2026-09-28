from collections import deque
def pick_cutstomer(si, sj):
    q = deque()
    q.append([si, sj, 0])
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    distance = float("inf")
    hubo = []

    while q:
        ci, cj, cd = q.popleft()

        if arr[ci][cj] < 0:
            if distance >= cd:
                distance = cd
                hubo.append([-arr[ci][cj], ci, cj, cd])
            else:
                continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] <= 0:
                q.append([ni, nj, cd + 1])
                visited[ni][nj] = 1

    if hubo:
        hubo = sorted(hubo, key=lambda x: (x[1], x[2]))
        arr[hubo[0][1]][hubo[0][2]] = 0 #승객의 흔적을 지워
        return hubo[0][0], hubo[0][3] #승객번호랑 거리 반환
    else:
        return -1, -1

def go_dest(si, sj, ei, ej):

    q = deque()
    q.append([si, sj, 0])
    visited = [[0] * N for _ in range (N)]
    visited[si][sj] = 1

    while q:
        ci, cj, cd = q.popleft()

        if (ei, ej) == (ci, cj):
            return cd


        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append([ni, nj, cd + 1])
                visited[ni][nj] = 1

    return -1


N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
taxi_i, taxi_j = map(lambda x: int(x)-1, input().split())
customer_sisj = [[] for _ in range (M+1)] #맨앞 더미
customer_eiej = [[] for _ in range (M+1)]
cur_battery = C

for m in range (1, M+1):
    si, sj, ei, ej = map(lambda x: int(x)-1, input().split())
    customer_sisj[m].append(si)
    customer_sisj[m].append(sj)
    customer_eiej[m].append(ei)
    customer_eiej[m].append(ej)

for m in range (1, M+1):
    i, j = customer_sisj[m][0], customer_sisj[m][1]
    arr[i][j] = -m

for _ in range (M):

    #[1] 승객 고르기
    cur_customer, cur_distance = pick_cutstomer(taxi_i, taxi_j)
    if (cur_customer, cur_distance) == (-1, -1):
        cur_battery = -1
        break

    #[2] 승객 태우러 가기
    cur_battery -= cur_distance
    if cur_battery <= 0:
        cur_battery = -1
        break

    taxi_i, taxi_j = customer_sisj[cur_customer][0], customer_sisj[cur_customer][1]

    #[3] 도착지로 모시기
    ei, ej = customer_eiej[cur_customer][0], customer_eiej[cur_customer][1]
    d = go_dest(taxi_i, taxi_j, ei, ej)

    if d == -1:
        cur_battery = -1
        break

    cur_battery -= d
    if cur_battery < 0:
        cur_battery = -1
        break
    taxi_i, taxi_j = ei, ej
    cur_battery += d * 2


print(cur_battery)