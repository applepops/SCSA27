def figure_out_peoples(group_points):

    group1_points = group_points[:]

    x = group1_points[0][0]
    y = group1_points[0][1]
    while True:
        x -= 1
        y += 1
        if x == group1_points[1][0] and y == group1_points[1][1]:
            break
        group1_points.append((x, y))

    x = group1_points[1][0]
    y = group1_points[1][1]
    while True:
        x -= 1
        y -= 1
        if x == group1_points[2][0] and y == group1_points[2][1]:
            break
        group1_points.append((x, y))

    x = group1_points[2][0]
    y = group1_points[2][1]
    while True:
        x += 1
        y -= 1
        if x == group1_points[3][0] and y == group1_points[3][1]:
            break
        group1_points.append((x, y))

    x = group1_points[3][0]
    y = group1_points[3][1]
    while True:
        x += 1
        y += 1
        if x == group1_points[0][0] and y == group1_points[0][1]:
            break
        group1_points.append((x, y))

    group2_p_cnt = 0
    group3_p_cnt = 0
    group4_p_cnt = 0
    group5_p_cnt = 0

    #group2의 인구 수 구하기:
    for i in range (0, group1_points[3][0]):
        for j in range (0, group1_points[2][1]+1):
            if (i, j) in group1_points:
                break
            else:
                group2_p_cnt += arr[i][j]


    #group 3의 인구 수 구하기
    for j in range (N-1, group1_points[2][1], -1):
        for i in range (0, group1_points[1][0]+1):
            if (i, j) in group1_points:
                break
            else:
                group3_p_cnt += arr[i][j]

    #group 4의 인구 수 구하기
    for j in range (0, group1_points[0][1]):
        for i in range (N-1, group1_points[3][0]-1, -1):
            if (i, j) in group1_points:
                break
            else:
                group4_p_cnt += arr[i][j]


    #group 5의 인구 수 구하기
    for i in range (N-1, group1_points[1][0], -1):
        for j in range (N-1, group1_points[0][1]-1, -1):
            if (i, j) in group1_points:
                break
            else:
                group5_p_cnt += arr[i][j]

    total_people = sum(map(sum, arr))

    group1_p_cnt = total_people - group2_p_cnt - group3_p_cnt - group4_p_cnt - group5_p_cnt

    max_people = max(group1_p_cnt, group2_p_cnt, group3_p_cnt, group4_p_cnt, group5_p_cnt)
    min_people = min(group1_p_cnt, group2_p_cnt, group3_p_cnt, group4_p_cnt, group5_p_cnt)

    return max_people - min_people

#포인트는 0번부터 1, 2, 3번까지 뽑을 건데
# 3번은 자동으로 정해지니까 1이랑 2까지만 뽑을 거임.
def backtracking(point):

    global min_gap

    #종료조건
    if point == 2:
        #이제 3번을 알아내자.
        #3번이 불가능하면 그건 또 return 시켜야 함.

        di = point_lst[0][0] - point_lst[1][0] #양수일 것이다.
        dj = point_lst[0][1] - point_lst[1][1] #음수일 것이다.

        ni = point_lst[2][0] + di
        nj = point_lst[2][1] + dj

        #3번째 꼭짓점을 찾았다.
        if 0 <= ni < N and 0 <= nj < N:
            point_lst.append((ni, nj))

            #여기에서 이제 각각 인구 알아내고 그래야 됨!!!
            res = figure_out_peoples(point_lst)
            min_gap = min(min_gap, res)

            point_lst.pop()

            return
        #3번째 꼭짓점이 불가능하다. 그냥 return
        else:
            return

    if point == 0:
        cur_i = point_lst[0][0]
        cur_j = point_lst[0][1]
        #시작점이 전혀 이동이 불가능한 좌표인 경우
        if cur_i == 0 or cur_j == N-1:
            return

        while cur_i-1 >= 0 and cur_j+1 <= N-1:
            #1번 꼭짓점을 뽑은 거임.
            point_lst.append((cur_i-1, cur_j+1))
            backtracking(1)
            point_lst.pop()

            cur_i -= 1
            cur_j += 1

    if point == 1:
        cur_i = point_lst[1][0]
        cur_j = point_lst[1][1]

        if cur_i == 0:
            return

        while cur_i-1 >= 0 and cur_j-1 >= 0:
            #2번 꼭짓점을 뽑은 거임.
            point_lst.append((cur_i-1, cur_j-1))
            backtracking(2)
            point_lst.pop()

            cur_i -= 1
            cur_j -= 1

    else:
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]

min_gap = float("INF")

point_lst = []
for i in range (N):
    for j in range (N):
        #귀찮아서 일단 모든 지점에 대해서 백트래킹 보낼게.
        point_lst.append((i, j))
        backtracking(0)
        point_lst.pop()

print(min_gap)