def do_sort():
    global arr

    for i in range (len(arr)):
        lst = [0] * 101
        for j in range (len(arr[i])):
            if arr[i][j] != 0: #0은 무시
                lst[arr[i][j]] += 1
        tmp = []
        for n in range (1, len(lst)):
            if lst[n]:
                tmp.append([n, lst[n]])

        tmp = sorted(tmp, key=lambda x: (x[1], x[0]))
        tmp = [n for row in tmp for n in row]
        arr[i] = tmp

def fill_zero():

    global arr

    max_col = 0
    for i in range (len(arr)):
        max_col = max(max_col, len(arr[i]))

    new_arr = [[0] * max_col for _ in range (len(arr))]

    for i in range (len(arr)):
        for j in range (len(arr[i])):
            new_arr[i][j] = arr[i][j]

    arr = new_arr

R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (3)]
time = 0

while True:
    
    if 0 <= R-1 < len(arr) and 0 <= C-1 < len(arr[0]):
        if arr[R-1][C-1] == K:
            break
    
    time += 1

    if time > 100:
        time = -1
        break

    #행의 개수랑 열의 개수 비교
    row_cnt = len(arr)
    col_cnt = len(arr[0])

    #행에 대한 정렬
    if row_cnt >= col_cnt:
        do_sort()
        fill_zero()

    #열에 대한 정렬
    else:
        arr = [list(row) for row in zip(*arr)][::-1]
        do_sort()
        fill_zero()
        arr = [list(row) for row in zip(*arr[::-1])]


print(time)