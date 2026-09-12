'''
문제이해 및 구상 (20분)
구현
디버깅
검증

'''

#파이팅
#묘수 금지

#입력으로 한 줄을 받을게, 그리고 몇 번째 줄인지. 왜냐면 표시해야 됨.
def put_stairs(lst, i, which_arr):
    for j in range (N-L+1):
        is_same = True
        is_already = False
        front = False
        back = False
        is_gap_okay = True

        for jj in range (j, j+L-1):
            if lst[jj] != lst[jj+1]: #L동안의 값이 다 같냐?
                is_same = False
                break
            if which_arr == 0: #이미 보도블럭을 설치한 곳 아냐?
                if stairs_row_arr[i][jj] == 1:
                    is_already = True
                    break
            else:
                if stairs_col_arr[i][jj] == 1:
                    is_already = True
                    break

        #앞 혹은 뒤 딱 하나만 1차이가 나?
        if 0 <= j-1 < N and lst[j-1] == lst[j]+1:
            front = True
        if 0 <= j+L < N and lst[j+L] == lst[j]+1:
            back = True
        if front and back:
            is_gap_okay = False
        elif not front and not back:
            is_gap_okay = False
        else:
            is_gap_okay = True

        #인제 진짜로 경사로 올릴게.
        if is_gap_okay and not is_already and is_same:
            for jj in range(j, j + L):
                if which_arr == 0:
                    stairs_row_arr[i][jj] = 1
                else:
                    stairs_col_arr[i][jj] = 1








N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

#기초공사
row_arr = arr
col_arr = [list(row) for row in zip(*arr[::-1])]

cnt = 0

#경사로를 올렸는지 확인하는 용도의 배열. 0이면 없고 1이면 있고.
stairs_row_arr = [[0]*N for _ in range (N)]
stairs_col_arr = [[0]*N for _ in range (N)]

#[1] 경사로 설치하기

for r in range(len(row_arr)):
    put_stairs(row_arr[r], r, 0)

# for row in stairs_row_arr:
#     print(*row)

for r in range (len(col_arr)):
    put_stairs(col_arr[r], r, 1)
# 
# print()
#
# for row in stairs_col_arr:
#     print(*row)

#[2] 지나갈 수 있는 곳인지 확인하기
for r in range (len(row_arr)):
    for i in range (N-1):
        if row_arr[r][i] == row_arr[r][i+1]:
            continue
        elif row_arr[r][i] == row_arr[r][i+1] + 1 and stairs_row_arr[r][i+1] == 1:
            continue
        elif row_arr[r][i] + 1 == row_arr[r][i+1] and stairs_row_arr[r][i] == 1:
            continue
        else:
            break
    else:
        cnt += 1

for r in range (len(col_arr)):
    for i in range (N-1):
        if col_arr[r][i] == col_arr[r][i+1]:
            continue
        elif col_arr[r][i] == col_arr[r][i+1] + 1 and stairs_col_arr[r][i+1] == 1:
            continue
        elif col_arr[r][i] + 1 == col_arr[r][i+1] and stairs_col_arr[r][i] == 1:
            continue
        else:
            break
    else:
        cnt += 1

print(cnt)




