def add_1(now_pizza):
   min_flour = min(now_pizza)
   for i in range (len(now_pizza)):
       if now_pizza[i] == min_flour:
           now_pizza[i]+= 1

def push_pizza(now_pizza):

    max_col = -1

    for i in range (0, len(now_pizza)):
        if len(now_pizza[i]) > max_col:
            max_col = len(now_pizza[i])

    tmp = [[0] * max_col for _ in range (len(now_pizza))] #0 채워넣기 용도
    add_tmp = [[0] * max_col for _ in range (len(now_pizza))] #얼마 더해줄지 계산용

    for i in range (0, len(now_pizza)):
        for j in range (0, len(now_pizza[i])):
            tmp[i][j] = now_pizza[i][j]

    for i in range (0, len(now_pizza)):
        for j in range (0, len(now_pizza[i])):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = di + i
                nj = dj + j

                if 0 <= ni < len(now_pizza) and 0 <= nj < max_col and tmp[ni][nj] != 0 and tmp[i][j] > tmp[ni][nj]:
                    gap = abs(tmp[i][j] - tmp[ni][nj]) // 5
                    add_tmp[i][j] -= gap
                    add_tmp[ni][nj] += gap

    for i in range (0, len(now_pizza)):
        for j in range (0, len(now_pizza[i])):
            tmp[i][j] += add_tmp[i][j]

    return tmp

def make_into_line(now_pizza):

    col_len = len(now_pizza[0])
    pizza_line = []

    for j in range (0, col_len):
        for i in range (len(now_pizza)-1, -1, -1):
            if now_pizza[i][j] == 0:
                continue
            pizza_line.append(now_pizza[i][j])

    return pizza_line

#[입력받기]
N, K = map(int, input().split())
input_pizza = list(map(int, input().split()))
now_pizza = input_pizza[:]
turn = 0

########################
#실행부
########################

while True:

    max_flour, min_flour = max(now_pizza), min(now_pizza)
    if max_flour - min_flour <= K:
        break

    turn += 1

    #[1] 밀가루 더해...
    add_1(now_pizza)

    now_pizza = [now_pizza[:]] #2차원으로 만들기
    cut = 1

    #[2] 피자 말아..
    while True:
        tmp_pizza = [row[0:cut] for row in now_pizza]
        bottom_pizza = [now_pizza[-1][cut:]]

        tmp_pizza = [list(row) for row in zip(*tmp_pizza[::-1])]

        if len(bottom_pizza[0]) < len(tmp_pizza[0]):
            break

        now_pizza = tmp_pizza + bottom_pizza
        cut = len(now_pizza[0])

    #[3] 도우를 꾹 눌러요
    now_pizza = push_pizza(now_pizza)

    #[3.1] 열작 행큰 순으로 1차원 리스트로 만들어준다.
    now_pizza = [make_into_line(now_pizza)]

    #[4] 도우를 두 번 반으로 접어준다.
    cut = N // 2
    for _ in range (2):
        tmp_pizza = [row[0:cut] for row in now_pizza]
        bottom_pizza = [row[cut:] for row in now_pizza[:]]
        tmp_pizza = [row[::-1] for row in tmp_pizza[::-1]]

        now_pizza = tmp_pizza + bottom_pizza
        cut //= 2

    #[4] 또 눌러
    now_pizza = push_pizza(now_pizza)
    #[4.1] 또 리스트로 만들어
    now_pizza = make_into_line(now_pizza)


print(turn)