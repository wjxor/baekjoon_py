N, M = map(int, input().split())
# list 선언 후 각 번호에 해당되는 공 넣기
basket = [i for i in range(1, N + 1)]
temp = 0

for i in range(M):
    i, j = map(int, input().split())

    # 교환 시작
    temp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = temp
    # 교환 끝

for i in range(N):
    print(basket[i], end=' ')