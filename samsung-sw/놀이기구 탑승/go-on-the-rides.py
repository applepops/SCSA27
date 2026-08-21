def find_fav_friends(ci, cj, c_student):

    fav_friends_cnt = 0

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = di + ci
        nj = dj + cj

        #이동 가능한 좌표인지
        if 0 <= ni < N and 0 <= nj < N:
            #빈자리가 아님
            if arr[ni][nj] != 0:
                for f in students[c_student]:
                    #내가 좋아하는 친구가 있다면..
                    if arr[ni][nj] == f:
                        fav_friends_cnt += 1

        friends_cnt_by_location[ci][cj] = fav_friends_cnt

def find_blank_seats(ci, cj):

    blank_seats_cnt = 0

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = di + ci
        nj = dj + cj

        # 이동 가능한 좌표인지
        if 0 <= ni < N and 0 <= nj < N:
            #빈자리 발견..
            if arr[ni][nj] == 0:
                blank_seats_cnt += 1

    #자리 후보지에 자리 위치와 함께 빈자리 개수를 넣어준다.
    seat_candidates.append((blank_seats_cnt, ci, cj))

def find_points(ci, cj, c_student):

    global total_points

    fav_friends_cnt = 0

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = di + ci
        nj = dj + cj

        #이동 가능한 좌표인지
        if 0 <= ni < N and 0 <= nj < N:
            #빈자리가 아님
            for f in students[c_student]:
                #내가 좋아하는 친구가 있다면..
                if arr[ni][nj] == f:
                    fav_friends_cnt += 1

    if fav_friends_cnt == 1:
        total_points += 1
    elif fav_friends_cnt == 2:
        total_points += 10
    elif fav_friends_cnt == 3:
        total_points += 100
    elif fav_friends_cnt == 4:
        total_points += 1000


N = int(input())

#맨앞은 더미, 1-based니까.
students = [[] for _ in range (N*N+1)]

#들어가는 애들 순서 기억하려고.
friend_order = []

#애들마다 좋아하는 친구들 입력받기
#index가 본인, 그 안에 든 요소가 좋아하는 친구들
for i in range (N*N):
    temp = list(map(int, input().split()))
    s = temp[0]
    friend_order.append(s)

    for f in temp[1:]:
        students[s].append(f)

#학생들이 최종적으로 들어갈 위치/초기값이 0이라서 visited로도 사용할 거임.
arr = [[0] * N for _ in range (N)]

#총 N*N명의 학생의 자리를 찾아줘야 하니까.
for i in range (N*N):

    #현재 자리 찾아줘야 하는 학생 데려오기.
    cur_student = friend_order[i]

    #0은 있을 수 있는 경우니까 -1로 하겠음.
    friends_cnt_by_location = [[-1] * N for _ in range (N)]

    for i in range (N):
        for j in range (N):
            #빈자리인지 체크
            if arr[i][j] == 0:
                find_fav_friends(i, j, cur_student)

    #제일 친구가 많은 경우의 max값 찾기
    max_friends_by_location = 0
    for i in range (N):
        for j in range (N):
            max_friends_by_location = max(friends_cnt_by_location[i][j], max_friends_by_location)

    seat_candidates = []
    for i in range (N):
        for j in range (N):
            if friends_cnt_by_location[i][j] == max_friends_by_location:
                find_blank_seats(i, j)


    seat_candidates = sorted(seat_candidates, key=lambda x: (-x[0], x[1], x[2]))

    arr[seat_candidates[0][1]][seat_candidates[0][2]] = cur_student


#이제 모든 학생들이 놀이기구에 탑승한 이후의 최종 점수 구하기
total_points = 0

for i in range (N):
    for j in range (N):
        find_points(i, j, arr[i][j])

print(total_points)