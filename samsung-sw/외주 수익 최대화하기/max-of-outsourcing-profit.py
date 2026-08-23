def backtracking(n, profit_sum):

    global max_profit_sum

    #N일까지는 처리해야 하니까 종료조건은 N+1
    if n == N+1:
        for i in range (1, N+1):
            if visited[i] >= 2:
                break
        else:
            max_profit_sum = max(max_profit_sum, profit_sum)
        return



    #n 날짜에 외주 작업 수행함
    for i in range (n, n+works[n][0]):
        visited[i] += 1
    backtracking(n+1, profit_sum + works[n][1])
    #원상복구
    for i in range (n, n+works[n][0]):
        visited[i] -= 1
    #n 날짜에 외주 작업 수행 안함
    backtracking(n+1, profit_sum)



#부분집합?
#전체 날짜
N = int(input())

#각 일자에 수행하는 외주 작업의 기한과 수익 입력 받기
#각 일자는 1-based. 맨앞은 더미
works = [[] for _ in range (N+1)]

for i in range (1, N+1):
    days, profit = map(int, input().split())
    works[i] = [days, profit]

visited = [0] * (N+1)
max_profit_sum = -float("INF")
#날짜, 수익 합계
backtracking(1, 0)

print(max_profit_sum)

