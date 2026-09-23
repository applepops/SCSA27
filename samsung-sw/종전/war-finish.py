didj = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

def find_each_group(square_lst):

       #디버깅용 찍어보기
       group_arr = [[0] * N for _ in range (N)]

       square_lst = sorted(square_lst, key=lambda x:(x[0]))
       up_point = square_lst[0]
       square_lst = sorted(square_lst, key=lambda x: (-x[0]))
       down_point = square_lst[0]
       square_lst = sorted(square_lst, key=lambda x: (x[1]))
       left_point = square_lst[0]
       square_lst = sorted(square_lst, key=lambda x: (-x[1]))
       right_point = square_lst[0]

       group1, group2, group3, group4, group5 = 0, 0, 0, 0, 0

       for i in range (N):
              for j in range (N):
                     if i+j < up_point[0] + up_point[1] and 0 <= i < left_point[0] and 0 <= j <= up_point[1]:
                            group_arr[i][j] = 2
                            group2 += arr[i][j]
                     elif i+j > down_point[0] + down_point[1] and right_point[0] < i < N and down_point[1] <= j < N:
                            group_arr[i][j] = 5
                            group5 += arr[i][j]
                     elif i-j > left_point[0] - left_point[1] and left_point[0] <= i < N and 0 <= j < down_point[1]:
                            group_arr[i][j] = 4
                            group4 += arr[i][j]
                     elif i - j < right_point[0] - right_point[1] and up_point[1] < j < N and 0 <= i <= right_point[0]:
                            group_arr[i][j] = 3
                            group3 += arr[i][j]
                     else:
                            group_arr[i][j] = 1
                            group1 += arr[i][j]

       # for row in group_arr:
       #        print(*row)

       return abs(max(group1, group2, group3, group4, group5) - min(group1, group2, group3, group4, group5))


def backtracking(si, sj, ci, cj, c_dir, cnt, total_cnt):

       global min_gap

       if cnt >= 4:
              return

       #성공 조건
       if (si, sj) == (ci, cj) and cnt == 3:
              res = find_each_group(lst[:])
              min_gap = min(res, min_gap)
              return

       # 직진
       ni = ci+didj[c_dir][0]
       nj = cj+didj[c_dir][1]
       if 0 <= ni < N and 0 <= nj < N:
              lst.append([ni, nj])
              backtracking(si, sj, ni, nj, c_dir, cnt, total_cnt+1)
              lst.pop()

       #꺾기
       if total_cnt != 0:
              c_dir = (c_dir + 1) % 4
              ni = ci + didj[c_dir][0]
              nj = cj + didj[c_dir][1]
              if 0 <= ni < N and 0 <= nj < N:
                     lst.append([ni, nj])
                     backtracking(si, sj, ni, nj, c_dir, cnt + 1, total_cnt+1)
                     lst.pop()




N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]
min_gap = float("inf")

for i in range (N):
       for j in range (N):
              lst = []
              backtracking(i, j, i, j, 0, 0, 0)

print(min_gap)