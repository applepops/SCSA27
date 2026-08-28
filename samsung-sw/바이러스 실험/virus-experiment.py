from collections import deque
#from heapq import heappop, heappush

#배지의 크기 N*N, 바이러스 개수 m, 사이클 개수 k
N, M, K = map(int, input().split())

#주의: 마지막에 추가되는 양분의 양을 의미하는 정수가 들어온다..
#그러면 각 칸마다 양분의 양이 다 다를 수도 있는 건가?

#어쨌거나 초기 상태는 양분이 분명 5씩이라고 했음.

#사이클이 끝날 때마다 각 칸에 더해져야 하는 양분을 저장하는 array
yangboon_by_cycle = [list(map(int, input().split())) for _ in range (N)]

#초기 양분 상황
current_yangboon = [[5] * N for _ in range (N)]

hq = deque()

for _ in range (M):
    vr, vc, age = map(int, input().split())
    #0-based로 만들어주기
    vr -= 1
    vc -= 1
    #age를 먼저 넣어준다! 어린 놈부터 꺼내서 양분 먹어야 해!
    hq.append([age, vr, vc])

hq = deque(sorted(hq, key=lambda x: (x[0], x[1], x[2])))

#K번 동안 반복할 거임
for k in range (K):

    dead_virus_yangboon = [[0] * N for _ in range (N)]
    new_hq = deque()
    q = deque()

    #1) hq에 있는 애들 다 꺼내서 양분 섭취시키거나 죽인다
    for _ in range (len(hq)):
        #바이러스 한 놈 꺼낸다.
        n_age, nr, nc = hq.popleft()
        #바이러스의 나이만큼 이곳에 양분이 충분히 있다면.
        if current_yangboon[nr][nc] >= n_age:
            current_yangboon[nr][nc] -= n_age
            n_age += 1
            #살아남은 놈들은 새로운 hq에 저장해준다.
            new_hq.append([n_age, nr, nc])

            # 나이가 5의 배수가 된 놈들은 따로 큐에 추가로 저장해준다.
            if n_age % 5 == 0:
                q.append([n_age, nr, nc])

        #바이러스가 죽는 경우
        else:
            dead_virus_yangboon[nr][nc] += n_age // 2

    #2) 죽은 바이러스들의 양분을 그 칸에 더해준다.
    for i in range (N):
        for j in range (N):
            current_yangboon[i][j] += dead_virus_yangboon[i][j]

    #3) 나이가 5의 배수인 놈들이 번식한다.
    while q:
        c_age, cr, cc = q.pop()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
            ni = cr + di
            nj = cc + dj

            # 범위 내인지 확인
            if 0 <= ni < N and 0 <= nj < N:
                new_hq.appendleft([1, ni, nj])

    #4) 주어진 양분의 양에 따라 칸에 양분 추가
    for i in range (N):
        for j in range (N):
            current_yangboon[i][j] += yangboon_by_cycle[i][j]

    #큐를 스왑해준다.
    hq = new_hq

#살아있는 바이러스의 양..
print(len(hq))