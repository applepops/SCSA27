from pprint import pprint

def rotate_info(d):
    new_info = [row[:] for row in info]

    if d == 0:
        new_info = [row[:] for row in zip(*new_info)][::-1]
        return new_info
    elif d == 2:
        new_info = [row[:] for row in zip(*new_info[::-1])]
        return new_info
    elif d == 1:
        new_info = [row[::-1] for row in new_info[::-1]]
        return new_info
    else:
        return new_info


N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]
didj = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ans = 0
info = [[0, 0, 0.05, 0, 0],
        [0, 0.1, 0, 0.1, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0]]

#[1] 달팽이 만들기
lst = []
cur_dir = 0
for i in range (1, N):
    for _ in range (2):
        for _ in range (i):
            lst.append(cur_dir)
        cur_dir = (cur_dir + 1) % 4
lst = lst + [cur_dir] * (N-1)

#[2] 청소하자.
ci, cj = N//2, N//2
for d in lst:
    ni = didj[d][0] + ci
    nj = didj[d][1] + cj
    cur_munji = 0
    cur_ij_munji = arr[ni][nj]

    cur_info = rotate_info(d)
    for i in range (5):
        for j in range (5):
            if 0 <= i - 2 + ni < N and 0 <= j - 2 + nj < N:
                arr[i - 2 + ni][j - 2 + nj] += int(cur_ij_munji * cur_info[i][j])
            else:
                ans += int(cur_ij_munji * cur_info[i][j])
            cur_munji += int(cur_ij_munji * cur_info[i][j]) #a%를 알기 위해서 모으기

    ai, aj = ni + didj[d][0], nj + didj[d][1]
    if 0 <= ai < N and 0 <= aj < N: #[주의] 얘도 격자밖으로 나갈 수 있잖아.
        arr[ai][aj] += cur_ij_munji - cur_munji
    else:
        ans += cur_ij_munji - cur_munji
    arr[ni][nj] = 0

    ci = ni
    cj = nj

print(ans)
