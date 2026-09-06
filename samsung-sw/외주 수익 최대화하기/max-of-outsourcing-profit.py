def backtracking (n, cur_profit):
    global max_profit

    if n > N+1:
        return

    if n == N+1:
        max_profit = max(cur_profit, max_profit)
        return

    t, p = works[n]
    backtracking(n+t, cur_profit+p) #n일째의 일을 넣는다
    backtracking(n+1, cur_profit) #n일째의 일을 안 넣는다.

#입력받기
#N일
N = int(input())
works = [[] for _ in range (N+1)] #1-based를 위해 dummy
for n in range (1, N+1):
    t, p = map(int, input().split())
    works[n] = [t, p]

max_profit = 0
backtracking(1, 0)

print(max_profit)

