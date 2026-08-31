#회전을 다 돌고 나서 지우는 건 한 번에 한다는 걸까? -> 예시 보니까 그런듯.
#원판의 number는 1-based 주의

def rotate_wonpans (xx, dd, kk):
    for i in range (1, N+1):
        if i % xx == 0:
            #시계방향
            if dd == 0:
                for _ in range (kk):
                    tmp = arr[i].pop(-1)
                    arr[i].insert(0, tmp) #문법주의 (idx, 넣을 값)

            #반시계방향
            elif dd == 1:
                for _ in range(kk):
                    tmp = arr[i].pop(0)
                    arr[i].append(tmp)
        else:
            continue


def delete_numbers ():
    for i in range (1, N+1):
        for j in range (M):
            #한 원판 안에서의 양쪽 옆 비교
            if arr[i][j] == arr[i][(j + 1) % M]:
                need_to_delete[i][j] = 1
                need_to_delete[i][(j + 1) % M] = 1
            if arr[i][j] == arr[i][(j - 1) % M]:
                need_to_delete[i][j] = 1
                need_to_delete[i][(j - 1) % M] = 1
            #첫번째 원판이면
            if i == 1:
                if arr[i][j] == arr[i+1][j]:
                    need_to_delete[i][j] = 1
                    need_to_delete[i+1][j] = 1
            #마지막 원판이면
            elif i == N:
                if arr[i][j] == arr[i-1][j]:
                    need_to_delete[i][j] = 1
                    need_to_delete[i-1][j] = 1
            #그외 원판이면
            else:
                if arr[i][j] == arr[i-1][j]:
                    need_to_delete[i][j] = 1
                    need_to_delete[i - 1][j] = 1
                if arr[i][j] == arr[i+1][j]:
                    need_to_delete[i][j] = 1
                    need_to_delete[i + 1][j] = 1

def print_arr ():
    for row in arr:
        print(*row)


#원판의 개수, 원판 내 수의 개수, 회전정보 개수
N, M, Q = map(int, input().split())

#원판 number를 1-based로 만들어주기 위해서 앞에다가 더미 붙였음.
arr = [[0] * M] + [list(map(int, input().split())) for _ in range (N)]

need_to_delete = [[0] * M for _ in range (N+1)]

for _ in range (Q):
    x, d, k = map(int, input().split())
    rotate_wonpans(x, d, k)

delete_numbers()

#지워진 숫자가 없는 경우
if sum(map(sum, need_to_delete)) == 0:
    total_mean = sum(map(sum, arr)) // (N * M)
    for i in range (1, N+1):
        for j in range (M):
            if arr[i][j] > total_mean:
                arr[i][j] -= 1
            elif arr[i][j] < total_mean:
                arr[i][j] += 1
            else:
                continue

    print(sum(map(sum, arr)))
#지워진 숫자가 있는 경우
else:
    res = 0
    for i in range (1, N+1):
        for j in range (M):
            if need_to_delete[i][j] == 0:
                res += arr[i][j]

    print(res)


