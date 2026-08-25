#열의 개수 구하기
def find_max_c():
    max_c = -1
    for i in range (100):
        for j in range (100):
            if arr[i][j] == 0:
                temp = j - 1
                max_c = max(max_c, temp)
                break
        else:
            max_c = max(max_c, 100)
            return max_c
    return max_c + 1

#행의 개수 구하기
def find_max_r():
    max_r = -1
    for j in range(100):
        for i in range(100):
            if arr[i][j] == 0:
                temp = i - 1
                max_r = max(max_r, temp)
                break
        else:
            max_r = max(max_r, 100)
            return max_r
    return max_r + 1

def print_arr(cur_r, cur_c):
    for i in range (cur_r):
        for j in range (cur_c):
            print(arr[i][j], end=" ")
        print()

ans_r, ans_c, ans_k = map(int, input().split())
ans_r -= 1
ans_c -= 1

#그냥 100*100으로 선언하자..
arr = [[0] * 100 for _ in range (100)]

#초기 3*3 넣어주기
for i in range (3):
    temp_arr = list(map(int, input().split()))
    arr[i][0:3] = temp_arr

cur_time = 0

while True:

    #엣지케이스: 게임을 진행하지 않아도 이미 답이 나온 경우
    if arr[ans_r][ans_c] == ans_k:
        print(cur_time)
        break

    cur_time += 1

    cur_r = find_max_r()
    cur_c = find_max_c()
    max_cur = max(cur_r, cur_c)

    #행의 개수가 열의 개수보다 크거나 같은 경우
    if cur_r >= cur_c:
        #i는 처리해줄 이번 행이다.
        for i in range (cur_r):
            cur_r_dict = dict()
            for j in range (cur_c):
                if arr[i][j] == 0:
                    continue
                else:
                    if arr[i][j] in cur_r_dict.keys():
                        cur_r_dict[arr[i][j]] += 1
                    else:
                        cur_r_dict[arr[i][j]] = 1
            temp_lst = []
            for key, cnt in cur_r_dict.items():
                #출현 빈도 수, 해당 숫자
                temp_lst.append((cnt, key))
                temp_lst = sorted(temp_lst, key=lambda x: (x[0], x[1]))

            #다시 배열에 넣어주기
            temp_j = 0
            for c, n in temp_lst:
                if temp_j + 1 < 100:
                    arr[i][temp_j] = n
                    arr[i][temp_j+1] = c
                temp_j += 2

            if len(temp_lst)*2-1 < max_cur:
                for tmp in range (len(temp_lst)*2, max_cur+1):
                    arr[i][tmp] = 0


    #열의 개수가 행의 개수보다 큰 경우
    else:
        # j는 처리해줄 이번 열이다.
        for j in range(cur_c):
            cur_c_dict = dict()

            for i in range(cur_r):
                if arr[i][j] == 0:
                    continue
                else:
                    if arr[i][j] in cur_c_dict.keys():
                        cur_c_dict[arr[i][j]] += 1
                    else:
                        cur_c_dict[arr[i][j]] = 1

            temp_lst = []
            for key, cnt in cur_c_dict.items():
                # 출현 빈도 수, 해당 숫자
                temp_lst.append((cnt, key))
                temp_lst = sorted(temp_lst, key=lambda x: (x[0], x[1]))

            # 다시 배열에 넣어주기
            temp_i = 0
            for c, n in temp_lst:
                if temp_i + 1 < 100:
                    arr[temp_i][j] = n
                    arr[temp_i + 1][j] = c
                temp_i += 2


            if len(temp_lst) * 2 - 1 < max_cur:
                for tmp in range(len(temp_lst) * 2, max_cur + 1):
                    arr[tmp][j] = 0


    if arr[ans_r][ans_c] == ans_k:
        print(cur_time)
        break

    if cur_time > 100:
        print(-1)
        break
