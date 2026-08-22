def backtracking(n, plus_cur_cnt, minus_cur_cnt, mul_cur_cnt):

    #종료 조건
    if n == N-1:
        temp = arr[0]
        for i in range (1, len(arr)):
            if lst[i-1] == '+':
                temp += arr[i]
            elif lst[i-1] == '-':
                temp -= arr[i]
            elif lst[i-1] == '*':
                temp *= arr[i]
        res.append(temp)

        return

    for i in range (3):
        if i == 0 and plus_cur_cnt+1 <= cnts[i]:
            lst.append('+')
            backtracking(n+1, plus_cur_cnt+1, minus_cur_cnt, mul_cur_cnt)
            lst.pop()
        elif i == 1 and minus_cur_cnt+1 <= cnts[i]:
            lst.append('-')
            backtracking(n+1, plus_cur_cnt, minus_cur_cnt+1, mul_cur_cnt)
            lst.pop()
        elif i == 2 and mul_cur_cnt+1 <= cnts[i]:
            lst.append('*')
            backtracking(n+1, plus_cur_cnt, minus_cur_cnt, mul_cur_cnt+1)
            lst.pop()

N = int(input())
arr = list(map(int, input().split()))
cnts = list(map(int, input().split()))

lst = []
res = []
#들어가는 애들은
#순서대로 뽑은 횟수, 덧셈 사용 횟수, 뺄셈 사용 횟수, 곱셈 사용 횟수
backtracking(0, 0, 0, 0)

print(min(res), max(res))
