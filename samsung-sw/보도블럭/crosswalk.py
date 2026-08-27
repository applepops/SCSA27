#'지나갈 수 있는 행과 열'의 개수 구하기
#경사로를 두지 않은 경우에도 지나갈 수 있을 수 있음.

#순회를 싹하면서 값 차이가 0.5 초과하면 False 아니면 True 반환
def check_reachable(lst):
    for i in range (len(lst)-1):
        if abs(lst[i] - lst[i+1]) > 0.5:
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

    if check_reachable(mini_new_arr):
        # print(mini_new_arr)
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

            if put_stairs_front and put_stairs_back:
                continue
            elif not put_stairs_front and not put_stairs_back:
                continue
            else:
                for plus in range (i, i+L):
                    mini_new_arr[plus] += 0.5

                #값을 더해주고 나서 지나갈 수 있는 길이 되었는지 확인하자..
                if check_reachable(mini_new_arr):
                    # print(mini_new_arr)
                    ans += 1
                    break


print(ans)
