from collections import deque

def count_food(tmp_lst):
       cnt = 0
       for i in range (3):
              if tmp_lst[i]:
                     cnt+=1
       return cnt


def find_group_and_return_daepyo(si, sj):
       q = deque()
       q.append([si, sj])

       daepyo_hubo = []

       while q:
              ci, cj = q.popleft()
              daepyo_hubo.append([belif_arr[ci][cj], ci, cj])

              for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                     ni = di + ci
                     nj = dj + cj
                     if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and food_arr[si][sj] == food_arr[ni][nj]:
                            q.append([ni, nj])
                            visited[ni][nj] = 1

       #대표자 선정
       daepyo_hubo = sorted(daepyo_hubo, key=lambda x:(-x[0], x[1], x[2]))
       daepyo = daepyo_hubo[0]

       #신앙심 넘기기
       daepyo[0] += len(daepyo_hubo) - 1
       belif_arr[daepyo[1]][daepyo[2]] = daepyo[0] #업데이트

       for d in range (1, len(daepyo_hubo)):
              daepyo_hubo[d][0] -= 1
              belif_arr[daepyo_hubo[d][1]][daepyo_hubo[d][2]] = daepyo_hubo[d][0] #업데이트

       daepyo = [count_food(food_arr[si][sj])] + daepyo #무슨 음식을 좋아하는지 맨앞에 추가

       return daepyo

##################################################
#[초기세팅]
lst = [[1, 0, 0], [0, 1, 0], [0, 0, 1], #민트/초코/우우
       [0, 1, 1], [1, 0, 1], [1, 1, 0],  #초코우유/민트우유/민트초코
       [1, 1, 1]] #민트초코우유

didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#[입력]
N, T = map(int, input().split())

i_food_arr = [list(input().strip()) for _ in range (N)]
belif_arr = [list(map(int, input().split())) for _ in range (N)]
food_arr = [[[] for _ in range (N)] for _ in range (N)]


for i in range (N):
       for j in range (N):
              if i_food_arr[i][j] == 'T': #민트
                     food_arr[i][j] = lst[0].copy() #아 제발. 딥카피. 미쳤어.
              elif i_food_arr[i][j] == 'C': #초코
                     food_arr[i][j] = lst[1].copy()
              elif i_food_arr[i][j] == 'M': #우유
                     food_arr[i][j] = lst[2].copy()

##################################################

for t in range (1, T+1):

       got_jeonpa = [[False] * N for _ in range (N)]

       #[1] 아침
       #신앙심을 모두 1씩 더해준다.
       for i in range (N):
              for j in range (N):
                     belif_arr[i][j] += 1

       #[2] 점심
       visited = [[0] * N for _ in range (N)]
       daepyos_lst = []
       for i in range (N):
              for j in range (N):
                     if visited[i][j] == 0:
                            visited[i][j] = 1
                            cur_daepyo = find_group_and_return_daepyo(i, j)
                            daepyos_lst.append(cur_daepyo)

       #[3] 저녁
       #대표자들 정렬하기
       daepyos_lst = sorted(daepyos_lst, key=lambda x:(x[0], -x[1], x[2], x[3]))
       # print(daepyos_lst)

       #전파하기
       for d in range (len(daepyos_lst)):
              # print()
              # print("지금 대표자...")
              # print(daepyos_lst[d])

              #전파 전 세팅
              d_belif = daepyos_lst[d][1]
              d_ganjeol = d_belif - 1
              d_i, d_j = daepyos_lst[d][2], daepyos_lst[d][3]
              d_foods = food_arr[d_i][d_j].copy()

              #이미 누군가에게 전파를 당한 전파자면, pass
              if got_jeonpa[d_i][d_j]:
                     continue

              d_dir = d_belif % 4
              n_i, n_j = d_i, d_j

              while True:

                     n_i, n_j = didj[d_dir][0] + n_i, didj[d_dir][1] + n_j

                     #종료조건
                     if not (0 <= n_i < N and 0 <= n_j < N):
                            break

                     if d_ganjeol <= 0:
                            break

                     # print(f"{n_i} {n_j}로 가자.")

                     #전파 대상과 신봉 음식이 완전히 같은 경우
                     if food_arr[n_i][n_j] == d_foods:
                            continue

                     #전파 대상과 신봉 음식이 다른 경우 -> 전파 진행
                     else:
                            got_jeonpa[n_i][n_j] = True

                            #강한 전파
                            if d_ganjeol > belif_arr[n_i][n_j]:
                                   food_arr[n_i][n_j] = d_foods.copy() #딥카피 잊지말자.
                                   d_ganjeol -= (belif_arr[n_i][n_j] + 1)
                                   belif_arr[n_i][n_j] += 1
                                   # print(f"{n_i} {n_j}에 강한 전파 하고 난 후...")
                                   # for row in food_arr:
                                   #        print(*row)

                            #약한 전파
                            else:
                                   for food in range (0, 3):
                                          if d_foods[food] == 1:
                                                 food_arr[n_i][n_j][food] = 1

                                   belif_arr[n_i][n_j] += d_ganjeol
                                   d_ganjeol = 0
                                   # print(f"{n_i} {n_j}에 약한 전파 하고 난 후...")
                                   # for row in food_arr:
                                   #        print(*row)


              #전파자 신앙심 업데이트
              belif_arr[daepyos_lst[d][2]][daepyos_lst[d][3]] = 1

       score = [0, 0, 0, 0, 0, 0, 0]
       for i in range (N):
              for j in range (N):
                     score[lst.index(food_arr[i][j])] += belif_arr[i][j]
       score.reverse()
       print(*score)