#하드코딩은 기세다.
#모양은 총 19가지
#매칸마다 계산 때려보자. 난 모르겠다.


def check_a_1(cur_i, cur_j):
    ans = 0

    di = [0, 0, 0]
    dj = [1, 2, 3]

    for i in range (3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_a_2(cur_i, cur_j):
    ans = 0
    di = [1, 2, 3]
    dj = [0, 0, 0]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_b(cur_i, cur_j):
    ans = 0
    di = [0, 1, 1]
    dj = [1, 0, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_c_1(cur_i, cur_j):
    ans = 0
    di = [1, 1, 2]
    dj = [0, 1, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_c_2(cur_i, cur_j):
    ans = 0
    di = [0, -1, -1]
    dj = [1, 1, 2]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_c_3(cur_i, cur_j):
    ans = 0
    di = [0, 1, 1]
    dj = [1, 1, 2]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_c_4(cur_i, cur_j):
    ans = 0
    di = [1, 1, 2]
    dj = [0, -1, -1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_d_1(cur_i, cur_j):
    ans = 0
    di = [1, 1, 1]
    dj = [-1, 0, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_d_2(cur_i, cur_j):
    ans = 0
    di = [0, 1, 0]
    dj = [-1, 0, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_d_3(cur_i, cur_j):
    ans = 0
    di = [1, 1, 2]
    dj = [0, 1, 0]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_d_4(cur_i, cur_j):
    ans = 0
    di = [1, 1, 2]
    dj = [-1, 0, 0]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_1(cur_i, cur_j):
    ans = 0
    di = [1, 1, 1]
    dj = [0, 1, 2]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_2(cur_i, cur_j):
    ans = 0
    di = [1, 1, 1]
    dj = [0, -1, -2]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_3(cur_i, cur_j):
    ans = 0
    di = [1, 2, 2]
    dj = [0, 0, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_4(cur_i, cur_j):
    ans = 0
    di = [1, 2, 2]
    dj = [0, 0, -1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_5(cur_i, cur_j):
    ans = 0
    di = [0, 0, 1]
    dj = [1, 2, 0]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_6(cur_i, cur_j):
    ans = 0
    di = [0, 0, 1]
    dj = [1, 2, 2]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_7(cur_i, cur_j):
    ans = 0
    di = [0, 2, 1]
    dj = [1, 0, 0]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans

def check_e_8(cur_i, cur_j):
    ans = 0
    di = [0, 1, 2]
    dj = [1, 1, 1]
    for i in range(3):
        ni = di[i] + cur_i
        nj = dj[i] + cur_j

        if 0 <= ni < N and 0 <= nj < M:
            ans += arr[ni][nj]
        else:
            return -1

    return ans


#입력받기
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]
max_sum = 0

for i in range (N):
    for j in range (M):
        #본인 값
        temp = arr[i][j]
        if check_a_1(i, j) != -1:
            max_sum = max(temp+check_a_1(i, j), max_sum)
        if check_a_2(i, j) != -1:
            max_sum = max(temp + check_a_2(i, j), max_sum)
        if check_b(i, j) != -1:
            max_sum = max(temp+check_b(i, j), max_sum)
        if check_c_1(i, j) != -1:
            max_sum = max(temp + check_c_1(i, j), max_sum)
        if check_c_2(i, j) != -1:
            max_sum = max(temp + check_c_2(i, j), max_sum)
        if check_c_3(i, j) != -1:
            max_sum = max(temp + check_c_3(i, j), max_sum)
        if check_c_4(i, j) != -1:
            max_sum = max(temp + check_c_4(i, j), max_sum)
        if check_d_1(i, j) != -1:
            max_sum = max(temp + check_d_1(i, j), max_sum)
        if check_d_2(i, j) != -1:
            max_sum = max(temp + check_d_2(i, j), max_sum)
        if check_d_3(i, j) != -1:
            max_sum = max(temp + check_d_3(i, j), max_sum)
        if check_d_4(i, j) != -1:
            max_sum = max(temp + check_d_4(i, j), max_sum)
        if check_e_1(i, j) != -1:
            max_sum = max(temp + check_e_1(i, j), max_sum)
        if check_e_2(i, j) != -1:
            max_sum = max(temp + check_e_2(i, j), max_sum)
        if check_e_3(i, j) != -1:
            max_sum = max(temp + check_e_3(i, j), max_sum)
        if check_e_4(i, j) != -1:
            max_sum = max(temp + check_e_4(i, j), max_sum)
        if check_e_5(i, j) != -1:
            max_sum = max(temp + check_e_5(i, j), max_sum)
        if check_e_6(i, j) != -1:
            max_sum = max(temp + check_e_6(i, j), max_sum)
        if check_e_7(i, j) != -1:
            max_sum = max(temp + check_e_7(i, j), max_sum)
        if check_e_8(i, j) != -1:
            max_sum = max(temp + check_e_8(i, j), max_sum)


print(max_sum)