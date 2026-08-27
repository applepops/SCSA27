#'지나갈 수 있는 행과 열'의 개수 구하기
#경사로를 두지 않은 경우에도 지나갈 수 있을 수 있음.

def check_way (n_arr):
    for i in range (1, len(n_arr)):
        d = abs(n_arr[i-1] - n_arr[i])
        #두 값이 같으면 지나간다.
        if d == 0:
            continue
        #1 차이가 나면 작은 애의 stairs를 확인한다.
        elif d == 1:
            if n_arr[i-1] < n_arr[i]:
                if stairs[i-1] == 1:
                    continue
                else:
                    return False
            else:
                if stairs[i] == 1:
                    continue
                else:
                    return False
        #두 값 차이가 2 이상이면 걍 안되는 놈이다.
        else:
            return False
    else:
        return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]
#행이랑 열을 그냥 모두 new_arr에 넣어줄거임.
new_arr = []
for row in arr:
    new_arr.append(row)

for row in list(zip(*arr)):
    new_arr.append(list(row))


ans = 0

for mini_new_arr in new_arr:

    stairs = [0] * N

    if check_way(mini_new_arr):
        ans += 1
        continue

    #L개씩 앞에서부터 싹 돈다.
    for i in range (N-L+1):
        tmp = mini_new_arr[i:i+L]

        #고른 L개가 다 같은 애들인지 확인하자
        for t in range (0, L-1):
            if tmp[t] != tmp[t+1]:
                break
            else:
                continue
        #다 같은 애들임이 판별났다.
        else:

            put_stairs_front = False
            put_stairs_back = False

            if 0 <= i-1 < N:
                if mini_new_arr[i-1] == tmp[0]+1:
                    put_stairs_front = True

            if 0 <= i+L < N:
                if mini_new_arr[i+L] == tmp[0]+1:
                    put_stairs_back = True

            #앞에도 뒤에도 다 큰 놈이 있어서 계단을 넣을 수 없다
            if put_stairs_front and put_stairs_back:
                continue
            #앞에도 뒤에도 다 큰 놈이 없다
            elif not put_stairs_front and not put_stairs_back:
                continue
            else:
                for plus in range (i, i+L):
                    #계단이 이미 있다 미친놈아 나가라
                    if stairs[plus] == 1:
                        break
                    else:
                        stairs[plus] = 1

    if check_way(mini_new_arr):
        # print("나는 체크되었다.")
        # print(stairs)
        # print(mini_new_arr)
        ans += 1


print(ans)
