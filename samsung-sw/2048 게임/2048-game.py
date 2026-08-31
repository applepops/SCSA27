#방향을 5개 뽑는 backtracking 함수
def pick_way(n):
    global max_num
    #종료조건: 5개 다 뽑음
    if n == 5:
        new_arr = [row[:] for row in arr[:]]
        for w in ways:
            move(w, new_arr)

        for i in range(N):
            for j in range(N):
                max_num = max(new_arr[i][j], max_num)

        return

    #상하좌우 중에 뽑기
    for i in range (0, 4):
        ways.append(i)
        pick_way(n+1)
        ways.pop()


#중력작용 및 합치기 함수
def move(way, new_arr):

    if way == 0: #왼쪽
        row_i = 0
        for row in new_arr:
            tmp_lst = []
            #0 아닌 숫자들만 집어넣기
            for i in range (N):
                if row[i] == 0:
                    continue
                else:
                    tmp_lst.append(row[i])
            #합치기 작용
            for i in range (len(tmp_lst)-1):
                if tmp_lst[i] == tmp_lst[i+1]:
                    tmp_lst[i] += tmp_lst[i+1]
                    tmp_lst[i+1] = 0

            new_row = [0] * N
            new_row_i = 0
            for i in range (len(tmp_lst)):
                if tmp_lst[i] == 0:
                    continue
                else:
                    new_row[new_row_i] = tmp_lst[i]
                    new_row_i += 1

            new_arr[row_i] = new_row[:]
            row_i += 1


    elif way == 1: #오른쪽
        row_i = 0
        for row in new_arr:
            tmp_lst = []
            # 0 아닌 숫자들만 집어넣기
            for i in range(N):
                if row[i] == 0:
                    continue
                else:
                    tmp_lst.append(row[i])

            tmp_lst = tmp_lst[::-1]

            # 합치기 작용
            for i in range(len(tmp_lst) - 1):
                if tmp_lst[i] == tmp_lst[i + 1]:
                    tmp_lst[i] += tmp_lst[i + 1]
                    tmp_lst[i + 1] = 0

            new_row = [0] * N
            new_row_i = N-1

            for i in range(len(tmp_lst)):
                if tmp_lst[i] == 0:
                    continue
                else:
                    new_row[new_row_i] = tmp_lst[i]
                    new_row_i -= 1

            new_arr[row_i] = new_row[:]
            row_i += 1

    elif way == 2: #위쪽
        for c in range (N):
            tmp_lst = []
            for r in range (N):
                if new_arr[r][c] == 0:
                    continue
                else:
                    tmp_lst.append(new_arr[r][c])
            #합치기 작용
            for i in range (len(tmp_lst)-1):
                if tmp_lst[i] == tmp_lst[i+1]:
                    tmp_lst[i] += tmp_lst[i+1]
                    tmp_lst[i+1] = 0

            new_col = [0] * N
            new_col_i = 0
            for i in range(len(tmp_lst)):
                if tmp_lst[i] == 0:
                    continue
                else:
                    new_col[new_col_i] = tmp_lst[i]
                    new_col_i += 1

            for i in range (N):
                new_arr[i][c] = new_col[i]


    elif way == 3: #아래쪽
        for c in range(N):
            tmp_lst = []
            for r in range(N):
                if new_arr[r][c] == 0:
                    continue
                else:
                    tmp_lst.append(new_arr[r][c])

            tmp_lst = tmp_lst[::-1]

            # 합치기 작용
            for i in range(len(tmp_lst) - 1):
                if tmp_lst[i] == tmp_lst[i + 1]:
                    tmp_lst[i] += tmp_lst[i + 1]
                    tmp_lst[i + 1] = 0

            new_col = [0] * N
            new_col_i = N-1
            for i in range(len(tmp_lst)):
                if tmp_lst[i] == 0:
                    continue
                else:
                    new_col[new_col_i] = tmp_lst[i]
                    new_col_i -= 1

            for i in range(N):
                new_arr[i][c] = new_col[i]
    else:
        return

def print_arr (arr_):
    for row in arr_:
        print(*row)


N = int(input())

arr = [list(map(int, input().split())) for _ in range (N)]
ways = []
#way는 0은 좌, 1은 우, 2는 위, 3은 아래로 하겠음.

max_num = 0
pick_way(0)

print(max_num)