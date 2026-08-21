from collections import deque

didj = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4:(1, 0), 5:(1, -1), 6: (0, -1), 7:(-1, -1)}

#격자 크기 N*N, 원자 개수, 실험시간
N, M, K = map(int, input().split())

wonja = deque()

for _ in range (M):
    #위치 정보, 질량, 속력, 방향
    x, y, m, s, d = map(int, input().split())
    #0-based로 만들어주기
    x -= 1
    y -= 1

    wonja.append([x, y, m, s, d])

#실험시간 K초 동안 반복함.
for _ in range (K):

    arr = [[[] for _ in range (N)] for _ in range (N)]

    #1.원자들 이동시키기
    #큐에서 모두 꺼내면서 이동시킨 후 3차원 배열에 넣어줄 거임.

    while wonja:

        cur_i, cur_j, cur_m, cur_s, cur_d = wonja.pop()

        di, dj = didj.get(cur_d, 0)

        ni = (di * cur_s + cur_i) % N
        nj = (dj * cur_s + cur_j) % N

        #3차원 배열에 넣어주기
        arr[ni][nj].append([ni, nj, cur_m, cur_s, cur_d])

    #2. 원소 합성처리
    for i in range (N):
        for j in range (N):
            if len(arr[i][j]) == 1:
                wonja.append(arr[i][j][0])
            elif len(arr[i][j]) >= 2:
                #합성해야 하는 애들
                new_m = 0 #새로운 질량
                new_s  = 0 #새로운 속력
                flag1 = False #상하좌우 있는지
                flag2 = False #대각선 있는지

                for cur_x, cur_y, cur_m, cur_s, cur_d in arr[i][j]:
                    new_m += cur_m
                    new_s += cur_s

                    if cur_d in [0, 2, 4, 6]:
                        flag1 = True
                    else:
                        flag2 = True

                new_m = new_m // 5

                #질량이 0이면 소멸합니다..
                if new_m == 0:
                    continue

                new_s = new_s // len(arr[i][j])

                #상하좌우 대각 둘 다 나왔다. -> 원소들이 대각선 네 방향의 값을 가진다.
                if flag1 and flag2:
                    wonja.append([cur_x, cur_y, new_m, new_s, 1])
                    wonja.append([cur_x, cur_y, new_m, new_s, 3])
                    wonja.append([cur_x, cur_y, new_m, new_s, 5])
                    wonja.append([cur_x, cur_y, new_m, new_s, 7])

                #상하좌우만 나왔다. -> 상하좌우로 간다.
                elif flag1 and not flag2:
                    wonja.append([cur_x, cur_y, new_m, new_s, 0])
                    wonja.append([cur_x, cur_y, new_m, new_s, 2])
                    wonja.append([cur_x, cur_y, new_m, new_s, 4])
                    wonja.append([cur_x, cur_y, new_m, new_s, 6])

                #대각만 나왔다. -> 상하좌우로 간다.
                elif not flag1 and flag2:
                    wonja.append([cur_x, cur_y, new_m, new_s, 0])
                    wonja.append([cur_x, cur_y, new_m, new_s, 2])
                    wonja.append([cur_x, cur_y, new_m, new_s, 4])
                    wonja.append([cur_x, cur_y, new_m, new_s, 6])


total_m = 0

while wonja:

    cur_i, cur_j, cur_m, cur_s, cur_d = wonja.pop()
    total_m += cur_m

print(total_m)