from collections import deque

#무빙워크의 길이, 실험종료하는 판의 개수
N, K = map(int, input().split())

#입력받기
arr = list(map(int, input().split()))

#무빙워크를 큐로 관리할 거임
total_moving_walk_q = deque()

#큐에다가 넣고 관리해줄 애들은
#순서대로 판의 idx(예시와 동기화를 위해 1-based)
#사람이 있는지 여부, 그리고 판의 안정성

#사람이 없으면 0, 있으면 1
for i in range (len(arr)):
    total_moving_walk_q.append([i+1, 0, arr[i]])

experiment_cnt = 0

while True:

    #과정이 '종료'될 때 몇 번째 실험이었는지 확인해야 하니
    #맨앞에서 실험 횟수 세준다.
    experiment_cnt += 1

    # print(f"{experiment_cnt}회차 실험")

    #1. 무빙워크의 시계방향 회전
    temp = total_moving_walk_q.pop()
    total_moving_walk_q.appendleft(temp)

    #회전하고 난 뒤에 마지막 칸 사람 처리해야지
    #N번째 칸에 사람이 위치한 경우, 내리게 하자.
    if total_moving_walk_q[N-1][1] == 1:
        total_moving_walk_q[N-1][1] = 0

    # print("무빙워크 시계방향 회전 후")
    # print(total_moving_walk_q)

    #2. 사람이 시계방향으로 한 칸씩 이동
    #'가장 먼저 무빙워크에 올라간 사람'부터 -> 실수 주의

    for i in range (N-2, -1, -1):
        #현재 사람이 이 칸에 있다.
        if total_moving_walk_q[i][1] == 1:
            #다음 칸에 사람이 없고 안정성이 0이 아니면
            #사람을 이동시키고 다음 칸 안정성 -1 처리
            if total_moving_walk_q[i+1][1] != 1 and total_moving_walk_q[i+1][2] != 0:
                #사람 이동
                total_moving_walk_q[i+1][1] = 1
                total_moving_walk_q[i][1] = 0
                #안정성 처리
                total_moving_walk_q[i+1][2] -= 1
            #다음 칸에 사람이 있거나 다음 칸의 안정성이 0이면
            else:
                #사람이 움직이지 않는다..
                continue

    # print("있는 사람들 이동시킨 후")
    # print(total_moving_walk_q)

    #사람들 이동시킨 후 마지막 칸 또 처리해야지.
    #N번째 칸에 사람이 위치한 경우, 내리게 하자.
    if total_moving_walk_q[N-1][1] == 1:
        total_moving_walk_q[N-1][1] = 0

    #3. 무빙워크 맨앞에 사람 올리기
    #첫 칸에 사람이 없고 안정성이 0이 아니면
    if total_moving_walk_q[0][1] != 1 and total_moving_walk_q[0][2] != 0:
        #사람 올리기
        total_moving_walk_q[0][1] = 1
        #안정성 처리
        total_moving_walk_q[0][2] -= 1

    # print("사람 올린 후")
    # print(total_moving_walk_q)

    check_k = 0
    for i in range (0, 2*N): #아 미친 여기서 실수함.
        if total_moving_walk_q[i][2] == 0:
            check_k += 1

    #K '이상'일 때 실험 종료
    #하마터면 K개일 때만 종료할 뻔. 진짜 죽고싶냐?
    if check_k >= K:
        break


print(experiment_cnt)