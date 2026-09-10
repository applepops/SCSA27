#이동 선이 서로 겹치지 않는다는 게 어디까지일까? 이것만 30분 이상 고민함.

def dfs (ci, cj, gn):

    groups[ci][cj] = gn

    if arr[ci][cj] == 4:
        people_by_group[gn].append(-1) #4는 그냥 -1로 만들 거야.
    else:
        people_by_group[gn].append(arr[ci][cj])

    ij_by_group[gn].append([ci, cj])


    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni = ci + di
        nj = cj + dj

        if 0 <= ni < N and 0 <= nj < N and 1 <= arr[ni][nj] <= 4 and groups[ni][nj] == 0:
            dfs(ni, nj, gn)

def put_people_back():
    global arr

    for i in range(1, M + 1):
        for p in range(len(people_by_group[i])):
            pi, pj = ij_by_group[i][p]
            arr[pi][pj] = people_by_group[i][p]


def custom_print(arr_):
    print("===============")
    for row in arr_:
        print(*row)
    print("===============")

#입력받기
#N*N, 팀 개수, 라운드 수(1-based)
N, M, K = map(int, input().split())
K-=1 #0-based로 만들게

arr = [list(map(int,  input().split())) for _ in range (N)]

#그룹을 확인하는 arr를 만들거임. dfs에서 visited로도 사용하고..
groups = [[0] * N for _ in range (N)]

people_by_group = [[] for _ in range (M+1)]
ij_by_group = [[] for _ in range (M+1)]

group_num = 1
total_score = 0

for i in range (N):
    for j in range (N):
        if arr[i][j] > 0 and groups[i][j] == 0:
            dfs(i, j, group_num)
            group_num += 1

groups_are_heading_to = [False] * (M+1) #False가 오른쪽이고 True가 왼쪽임.

#사람들 번호를 이쁘게 다시 맥여주자.
for i in range (1, M+1):

    #방향을 알아보자...
    flag = False

    #왼쪽으로 가는 사람들인지 알아보자
    for p in range(1, len(people_by_group[i])):

        if people_by_group[i][p] == -1 or people_by_group[i][p-1] == -1:
            continue

        if people_by_group[i][p] > people_by_group[i][p-1]:
            continue
        else:
            break
    else:
        flag = True #왼쪽으로 간다는 뜻임.
        groups_are_heading_to[i] = True

    if flag: #왼쪽으로 가는 사람들
        for p in range(0, len(people_by_group[i])):
            if people_by_group[i][p] == 1:
                start_idx = p

        people_cnt = 0
        for p in range(0, len(people_by_group[i])):
            if people_by_group[i][p] >= 1:
                people_cnt+=1
        p_num = 1
        for _ in range (people_cnt):
            if people_by_group[i][start_idx] >= 1:
                people_by_group[i][start_idx] = p_num
                p_num += 1
            start_idx = (start_idx + 1) % len(people_by_group[i])


    elif not flag: #오른쪽으로 가는 사람들
        for p in range(len(people_by_group[i])-1, 0, -1):
            if people_by_group[i][p] == 1:
                start_idx = p

        people_cnt = 0
        for p in range(0, len(people_by_group[i])):
            if people_by_group[i][p] >= 1:
                people_cnt += 1
        p_num = 1
        for _ in range (people_cnt):
            if people_by_group[i][start_idx] >= 1:
                people_by_group[i][start_idx] = p_num
                p_num += 1
            start_idx = (start_idx - 1) % len(people_by_group[i])


#이제 다시 집어 넣는다.. 이게 뭔짓이지? 으엥
put_people_back()


for k in range (0, K+1): #1-based
    #이제 기본 세팅은 다 끝났고.. 라운드 반복하자.
    #K번 반복되는 라운드....
    #[1] 각 사람은 머리사람을 따라서 한 칸 이동한다.
    for i in range (1, M+1):
        if groups_are_heading_to[i] == False: #오른쪽으로 가고 있는 애들이면..
            tmp = people_by_group[i].pop(-1)
            people_by_group[i].insert(0, tmp)
        else:
            tmp = people_by_group[i].pop(0)
            people_by_group[i].append(tmp)

        put_people_back()

    did_we_visit_this_group = [0] * (M+1) #매라운드마다 새롭게 초기화를 시켜야 하는 놈.

    #[2] 현재 k가 무엇인지에 따라서 공을 처 받을 것이다.

    tmp_k = k % (4*N) #4N번 넘어가는 미친 놈을 위해 tmp_k를 만들자.
    # print(f"나의 지금 라운드 {tmp_k}")

    if 0 <= tmp_k <= N-1: #위에서 아래로 내려가는 row
        for j in range (0, N):
            if did_we_visit_this_group[groups[tmp_k][j]] == 0 and arr[tmp_k][j] >= 1:
                did_we_visit_this_group[groups[tmp_k][j]] = 1 #이제 못 가게 해야지
                total_score += (arr[tmp_k][j] * arr[tmp_k][j])

    elif N <= tmp_k <= 2*N-1: #왼쪽에서 오른쪽으로 가는 col
        tmp_k -= N
        for i in range (N-1, -1, -1):
            if did_we_visit_this_group[groups[i][tmp_k]] == 0 and arr[i][tmp_k] >= 1:
                did_we_visit_this_group[groups[i][tmp_k]] = 1 #이제 못 가게 해야지
                total_score += (arr[i][tmp_k] * arr[i][tmp_k])

    elif 2*N <= tmp_k <= 3*N-1: #아래에서 위로 가는 row
        tmp_k -= 2*N
        tmp_k = (N-1) - tmp_k
        for j in range (N-1, -1, -1):
            if did_we_visit_this_group[groups[tmp_k][j]] == 0 and arr[tmp_k][j] >= 1:
                did_we_visit_this_group[groups[tmp_k][j]] = 1 #이제 못 가게 해야지
                total_score += (arr[tmp_k][j] * arr[tmp_k][j])

    elif 3*N <= tmp_k <= 4*N-1: #오른쪽에서 왼쪽으로 가는 col
        tmp_k -= 3*N
        tmp_k = (N-1) - tmp_k
        for i in range (0, N):
            if did_we_visit_this_group[groups[i][tmp_k]] == 0 and arr[i][tmp_k] >= 1:
                did_we_visit_this_group[groups[i][tmp_k]] = 1 #이제 못 가게 해야지
                total_score += (arr[i][tmp_k] * arr[i][tmp_k])

    #[3] 획득한 그룹은 방향을 바꿔야됨.
    for g in range (1, len(did_we_visit_this_group)):
        if did_we_visit_this_group[g] == 1:

            if groups_are_heading_to[g]:
                groups_are_heading_to[g] = False
            else:
                groups_are_heading_to[g] = True

            ccnt = 0
            for people in range (len(people_by_group[g])):
                if people_by_group[g][people] >= 1:
                    ccnt += 1 #인간 수

            for people in range(len(people_by_group[g])):
                if people_by_group[g][people] >= 1:
                    people_by_group[g][people] -= (ccnt +1)
                    people_by_group[g][people] *= -1

print(total_score)