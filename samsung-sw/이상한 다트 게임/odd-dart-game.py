#회전을 다 돌고 나서 지우는 건 한 번에 한다는 걸까? -> 예시 보니까 그런듯.
#아니 근데 그러면 왜 '원판에 남은 수가 없을 경우에는' 정규화를 진행하지 않는다고 하지?
#n하고 m은 최소 2씩이라 원판에 남은 수가 없을 수가 있나?
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
    need_to_delete = [[0] * M for _ in range(N + 1)]

    for i in range (1, N+1):
        for j in range (M):

            #이미 지워진 애면.. 넘어가..
            if arr[i][j] == 0:
                continue

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

    #만약에 지워져야 하는 애면 0으로..
    for i in range (1, N+1):
        for j in range (M):
            if need_to_delete[i][j] == 1:
                arr[i][j] = 0

    return sum(map(sum, need_to_delete))

def print_arr ():
    for row in arr:
        print(*row)


#원판의 개수, 원판 내 수의 개수, 회전정보 개수
N, M, Q = map(int, input().split())

#원판 number를 1-based로 만들어주기 위해서 앞에다가 더미 붙였음.
arr = [[0] * M] + [list(map(int, input().split())) for _ in range (N)]
need_to_delete = [[0] * M for _ in range(N + 1)]

total_num_cnt = N * M

for _ in range (Q):
    x, d, k = map(int, input().split())
    rotate_wonpans(x, d, k)
    deleted_num_cnt = delete_numbers()

    #지워진 숫자가 없는 경우
    if deleted_num_cnt == 0 and total_num_cnt > 0:
        total_mean = sum(map(sum, arr)) // total_num_cnt
        for i in range (1, N+1):
            for j in range (M):
                if arr[i][j] == 0:
                    continue
                if arr[i][j] > total_mean:
                    arr[i][j] -= 1
                elif arr[i][j] < total_mean:
                    arr[i][j] += 1
                else:
                    continue
    else:
        total_num_cnt -= deleted_num_cnt


res = 0
for i in range (1, N+1):
    for j in range (M):
        if arr[i][j] != 0:
            res += arr[i][j]

print(res)


