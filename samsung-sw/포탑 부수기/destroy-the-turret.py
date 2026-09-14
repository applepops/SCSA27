from collections import deque

def pick_attacker():

    min_power = float("inf")
    attacker_hubo = []

    #0을 제외한 가장 낮은 공격력 찾기
    for i in range (N):
        for j in range (M):
            if arr[i][j] != 0 and arr[i][j] < min_power:
                min_power = arr[i][j]

    #후보에 넣기
    for i in range (N):
        for j in range (M):
            if arr[i][j] == min_power:
                attacker_hubo.append([i, j, recently_attacked_arr[i][j], i+j, j])

    #정렬하기: 최근 공격, 행+열이 큰 것, 열이 큰 것
    attacker_hubo = sorted(attacker_hubo, key= lambda x: (-x[2], -x[3], -x[4]))

    #최근 공격 자료구조 갱신, 공격한 시점을 적어주자.
    recently_attacked_arr[attacker_hubo[0][0]][attacker_hubo[0][1]] = k

    #결정된 attacker의 i, j를 반환할게
    return attacker_hubo[0][0], attacker_hubo[0][1]

def pick_victim(ai, aj):
    max_power = -float("inf")
    victim_hubo = []

    #0을 제외한 가장 큰 공격력 찾기
    for i in range (N):
        for j in range (M):
            if arr[i][j] != 0 and arr[i][j] > max_power and (i, j) != (ai, aj):
                max_power = arr[i][j]

    #후보에 넣기
    for i in range (N):
        for j in range (M):
            if arr[i][j] == max_power and (i, j) != (ai, aj):
                victim_hubo.append([i, j, recently_attacked_arr[i][j], i+j, j])

    # 정렬하기: 오래된 공격, 행+열이 작은 것, 열이 작은 것
    victim_hubo = sorted(victim_hubo, key=lambda x: (x[2], x[3], x[4]))

    # 결정된 피공격자의 i, j를 반환할게
    return victim_hubo[0][0], victim_hubo[0][1]

def backtracking(n, ci, cj, vi, vj, visited_):

    if n == visited_[vi][vj]:
        if (ci, cj) == (vi, vj):
            lst_hubo.append(lst[:])
        return

    if lst_hubo:
        return

    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni = di + ci
        nj = dj + cj

        # 어린왕자 처리
        if ni == N:
            ni = 0
        if nj == M:
            nj = 0
        if ni == -1:
            ni = N - 1
        if nj == -1:
            nj = M - 1

        if visited_[ci][cj] + 1 == visited_[ni][nj]:
            lst.append([ni, nj])
            backtracking(n+1, ni, nj, vi, vj, visited_)
            lst.pop()


def laser(ai, aj, vi, vj):

    q = deque()
    visited = [[-1] * M for _ in range (N)]
    q.append([ai, aj])
    visited[ai][aj] = 0
    is_found = False

    while q:

        ci, cj = q.popleft()

        if (ci, cj) == (vi, vj):
            is_found = True
            break

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni = ci + di
            nj = cj + dj

            #어린왕자 처리
            if ni == N:
                ni = 0
            if nj == M:
                nj = 0
            if ni == -1:
                ni = N-1
            if nj == -1:
                nj = M-1

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and arr[ni][nj] != 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj]+1

    # print("===bfs visited 찍어보기===")
    # for row in visited:
    #     print(*row)
    # print("========================")

    if not is_found:
        return
    else:
        backtracking(0, ai, aj, vi, vj, visited)

def potop(ai, aj, vi, vj, power):
    ci, cj = vi, vj

    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)):
        ni = ci + di
        nj = cj + dj

        # 어린왕자 처리
        if ni == N:
            ni = 0
        if nj == M:
            nj = 0
        if ni == -1:
            ni = N - 1
        if nj == -1:
            nj = M - 1

        #피공격자 주변 8개 피해
        if arr[ni][nj] != 0 and (ni, nj) != (ai, aj): #공격자에게 피해가면 안됨.
            related_to_attack_arr[ni][nj] = True #공격과 관련되었는지 처리
            arr[ni][nj] -= power // 2
            if arr[ni][nj] < 0:
                arr[ni][nj] = 0

    arr[vi][vj] -= power #피공격자 본인
    if arr[vi][vj] < 0:
        arr[vi][vj] = 0


def custom_print():
    print("포탄들 지금 상태 찍어볼게.")
    for row in arr:
        print(*row)
    print("=======================")

def custom_print2():
    print("공격 최근에 언제 했는지 지금 상태 찍어볼게.")
    for row in recently_attacked_arr:
        print(*row)
    print("=======================")

#입력받기
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

recently_attacked_arr = [[0] * M for _ in range (N)] #언제 최근에 공격했는지

#K턴 반복
for k in range (1, K+1):

    # print(f"{k}회차*********")

    #공격과 관련 있는 애들은 True로 바꿔주는 배열
    related_to_attack_arr =  [[False] * M for _ in range (N)]

    #[1] 공격자 선정
    attacker_i, attacker_j = pick_attacker()
    # print("공격자")
    # print(attacker_i, attacker_j)
    #[1.1] 공격과 관련되었는지 처리해주기
    related_to_attack_arr[attacker_i][attacker_j] = True
    #[1.2] 공격자 공격 power 계산 [실수]: 피공격자 고르고 계산했어야 했다.
    attacker_power = arr[attacker_i][attacker_j] + N + M
    #[1.3] 공격자 파워 갱신
    arr[attacker_i][attacker_j] = attacker_power

    #[2] 피공격자 선정 - [주의] 공격자 고르면 안됨!
    victim_i, victim_j = pick_victim(attacker_i, attacker_j)
    # print("피공격자")
    # print(victim_i, victim_j)
    #[2.1] 공격과 관련되었는지 처리해주기
    related_to_attack_arr[victim_i][victim_j] = True

    #[3] 레이저 공격 시도
    lst_hubo = []
    lst = []
    laser(attacker_i, attacker_j, victim_i, victim_j)

    if lst_hubo:
        real_lst = lst_hubo[0] #맨앞놈이 ㄹㅇ 길임
        #print(real_lst)
        #레이저 공격 이후 처리: 공격력 감소 및 공격 관련 되었다는 처리
        for i in range (len(real_lst)-1):
            if arr[real_lst[i][0]][real_lst[i][1]] >= attacker_power // 2:
                arr[real_lst[i][0]][real_lst[i][1]] -= attacker_power // 2
            else:
                arr[real_lst[i][0]][real_lst[i][1]] = 0
            related_to_attack_arr[real_lst[i][0]][real_lst[i][1]] = True

        #victim은 더 크게 공격을 받지.
        arr[real_lst[-1][0]][real_lst[-1][1]] -= attacker_power
        if arr[real_lst[-1][0]][real_lst[-1][1]] < 0:
            arr[real_lst[-1][0]][real_lst[-1][1]] = 0
    else:
        #[4] 3실패시 포탄 공격
        # print("길이 없어")
        potop(attacker_i, attacker_j, victim_i, victim_j, attacker_power)

    #[5] 포탑 정비
    for i in range (N):
        for j in range (M):
            if arr[i][j] != 0 and related_to_attack_arr[i][j] == False:
                arr[i][j] += 1

    # print("포탑정비 완료")
    # custom_print()

    #[6] 종료조건에 해당하는지 확인절차
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt += 1

    if cnt <= 1:
        break

#출력하기 -> 남은 포탑 중 가장 강한 포탑의 공격력
print(max(map(max, *arr)))