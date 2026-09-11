def custom_print(arr_):
    print("===================")
    for row in arr_:
        print(*row)
    print("===================")

def move_people(pi, pj):

    ei, ej = exit[0], exit[1] #탈출구 좌표

    if ei < pi and not (1 <= arr[pi-1][pj] <= 9): #상하를 우선적으로..
        return pi-1, pj
    elif ei > pi and not (1 <= arr[pi+1][pj] <= 9):
        return pi+1, pj
    elif ei == pi: #같으면../ 좌우 처리
        if ej < pj and not (1 <= arr[pi][pj-1] <= 9):
            return pi, pj-1
        elif ej > pj and not (1 <= arr[pi][pj+1] <= 9):
            return pi, pj+1
        else:
            return pi, pj #상하가 같은데 좌우에 벽이 있어서 못 간다
    elif ej < pj and not (1 <= arr[pi][pj-1] <= 9): # 상하에 벽이 있어서 못 가는 경우 좌우 처리
        return pi, pj - 1
    elif ej > pj and not (1 <= arr[pi][pj+1] <= 9):
        return pi, pj+1
    else:
        return pi, pj #아무데도 못 간다.

def in_range (i):
    return 0 <= i < N

def find_square():
    for length in range (2, N+1):
        for r in range (0, N-length+1):
            for c in range (0, N-length+1):
                #이게 꼭짓점을 지금 찾은 것임. 시작점.
                flag1 = False
                flag2 = False

                if r <= exit[0] <= r + length-1 and c <= exit[1] <= c + length-1:
                    flag1 = True
                for m in range (M):
                    if not did_people_get_out[m]: #탈출한 사람 빼고
                        if r <= people_ijs[m][0] <= r + length-1 and c <= people_ijs[m][1] <= c+length-1:
                            flag2 = True
                            break

                if flag1 and flag2:
                    return r, c, r+length-1, c+length-1

    else: #여기 올 일은 없겠지만.
        return -1, -1, -1, -1

def rotate(si, sj, ei, ej):

    start_i = min(si, ei)
    start_j = min(sj, ej)

    end_i = max(si, ei)
    end_j = max(sj, ej)

    tmp_mini_arr = [row[start_j:end_j+1] for row in arr[start_i:end_i+1]]

    tmp_mini_people_arr = [
        [inner[:] for inner in row[start_j:end_j + 1]]
        for row in people_arr[start_i:end_i + 1]
    ]

    tmp_mini_arr = [row for row in zip(*tmp_mini_arr[::-1])] #시계방향 90도 회전
    tmp_mini_people_arr = [row for row in zip(*tmp_mini_people_arr[::-1])]

    for r in range (start_i, end_i+1):
        for c in range (start_j, end_j+1):
            arr[r][c] = tmp_mini_arr[r-start_i][c-start_j]

    for r in range (start_i, end_i+1):
        for c in range (start_j, end_j+1):
            people_arr[r][c] = tmp_mini_people_arr[r-start_i][c-start_j]

    for r in range (N):
        for c in range (N):
            lst = people_arr[r][c]
            for m in lst:
                people_ijs[m][0] = r #갱신했어.
                people_ijs[m][1] = c

#[입력받기]
#N*N, M명의 참가자, K번 반복
N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]
people_ijs = [] #사람들 좌표
for _ in range (M):
    i, j = map(int, input().split())
    people_ijs.append([i-1, j-1])

i, j = map(int, input().split())
exit = [i-1, j-1] #탈출지 좌표

arr[exit[0]][exit[1]] = 10 #탈출지 저장해둘게 / 벽이랑 겹칠 일은 없다. 참가자 좌표랑도 안 겹친다.
did_people_get_out = [False] * M #0-based, 탈출 확인용

people_arr = [[[] for _ in range (N)] for _ in range (N)] #얘도 갱신해줘야됨 그러면.
for m in range (M):
    people_arr[people_ijs[m][0]][people_ijs[m][1]].append(m) #저장해줬다.

total_moved_distance = 0

# custom_print(arr)


#K초 동안 반복합니다.
for k in range (K):
    # print(f"{k+1}회차")
    # print("원래 인간")
    # custom_print(people_arr)

    #[1]모든 참가자의 이동(단, 이미 탈출한 사람 빼고.)
    #   [주의] 벽 조건 확인 및 사람 위치, update
    #   [주의] 탈출했는지도 확인시켜라, update
    #   [주의] 움직일 수 있다면 total_moved_distance += 1

    new_people_arr = [[[] for _ in range(N)] for _ in range(N)]

    for m in range (M):
        if not did_people_get_out[m]: #이미 탈출한 사람 빼고
            new_i, new_j = move_people(people_ijs[m][0], people_ijs[m][1])
            # 움직인 경우
            if (new_i, new_j) != (people_ijs[m][0], people_ijs[m][1]):
                total_moved_distance += 1
            people_ijs[m][0], people_ijs[m][1] = new_i, new_j #갱신
            #움직여서 탈출에 성공한 경우
            if (new_i, new_j) == (exit[0], exit[1]):
                did_people_get_out[m] = True
            else:
                new_people_arr[new_i][new_j].append(m)
    # print("점수")
    # print(total_moved_distance)
    people_arr = new_people_arr #갱신

    # print("인간 이동")
    # custom_print(people_arr)

    #[1.1] 참가자들이 다 탈출했는지 확인하고 만약에 했으면 break
    flag = True
    for i in range (M):
        if not did_people_get_out[i]: #탈출 못한 사람이 있다면
            flag = False
    if flag:
        break

    #[2] 가장 작은 정사각형 찾기.
    r1, c1, r2, c2 = find_square()
    # print("사각형 찾음")
    # print(r1, c1, r2, c2)

    # [3] 회전
    rotate(r1, c1, r2, c2)

    #[4] 벽 깎기
    for r in range (r1, r2+1):
        for c in range (c1, c2+1):
            if 1 <= arr[r][c] <= 9:
                arr[r][c] -= 1

    # print("격자 상황")
    # custom_print(arr)
    # print("인간 상황")
    # custom_print(people_arr)

    #[5] 새로운 출구 찾고 출구 업데이트해주기
    for r in range (N):
        for c in range (N):
            if arr[r][c] == 10:
                exit[0], exit[1] = r, c


print(total_moved_distance)
print(exit[0]+1, exit[1]+1)