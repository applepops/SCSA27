
from collections import deque

#격자의 크기, 리브로수를 키우는 총 년수
N, M = map(int, input().split())

#나무 상태 입력 받기
arr = [list(map(int, input().split())) for _ in range (N)]

#M년에 걸친 규칙들 입력 받기
rules = []
for _ in range (M):
    d, p = map(int, input().split())
    rules.append((d, p)) #형식에 주의


#초기 특수 영양제들의 위치. 좌하단 4개의 칸에 들어간다.
#N이 최소 3이니까 좌표밖을 나갈 일은 없다.
suksuks = [(N-1,  0), (N-1, 1), (N-2, 0), (N-2, 1)]

#원래 쓰고 싶었던 코드
#딕셔너리 제발 사용법 좀 익혀라
didr = {1:(0,1), 2:(-1,1), 3:(-1,0), 4:(-1,-1), 5:(0,-1), 6:(1,-1), 7:(1,0), 8:(1,1)}

#M년 동안 반복
for m in range (M):

    cur_d, cur_p = rules[m][0], rules[m][1]

    #좌표 가져오기
    di, dj = didr.get(cur_d, 0)

    q = deque()
    temp_suksuks = []

    for x, y in suksuks:
        x = (x + di * cur_p) % N
        y = (y + dj * cur_p) % N

        #좌표 이동된 특수영양제들의 좌표들을 큐에 넣어준다.
        q.append((x, y))

        # 일단 영양제 있는 땅의 리브로수 길이 1 먹여주기.
        arr[x][y] += 1

        #temp_suksuks의 용도는 해당 년도에 특수 영양제를 맞은 땅을 제외하기 위해
        temp_suksuks.append((x, y))

    #특수영양제 배열 초기화
    suksuks = []

    #대각선 인접한 리브로수 개수 기억하는 용도
    temp_arr = [[0] * N for _ in range (N)]

    while q:

        cur_i, cur_j = q.pop()

        for di, dj in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            ni = di + cur_i
            nj = dj + cur_j

            #격자 안의 리브로수인지 확인
            if 0 <= ni < N and 0 <= nj < N:
                #대각선에 인접한 리브로수가 1이상이면
                if arr[ni][nj] >= 1:
                    temp_arr[cur_i][cur_j] += 1


    #나무 마저 키워주기
    for i in range (N):
        for j in range (N):
            if temp_arr[i][j] != 0:
                arr[i][j] += temp_arr[i][j]

    #전체 돌면서 2이상인 리브로수는 높이 2를 베고 그 위치를 suksuks에 넣어준다.
    for i in range (N):
        for j in range (N):
            if arr[i][j] >= 2:
                # 해당 년도에 특수 영양제를 맞은 땅을 제외해야 함!!!!
                if not (i, j) in temp_suksuks:
                    arr[i][j] -= 2
                    #새롭게 쑥쑥 배열에 넣어준다
                    suksuks.append((i, j))

#남아있는 리브로수 높이들의 총합 구하기
ans = 0
for i in range (N):
    for j in range (N):
        ans += arr[i][j]

print(ans)
