N, M = map(int, input().split())
# list 선언 후 0으로 초기화
basket = [0 for _ in range(N)]

# M번동안 i, j, k의 값을 받기위해 for loop
for _ in range(M):
    i, j, k = map(int, input().split())
    # i ~ j까지이기에 (i, j + 1)
    # list는 0번부터 시작하므로 -1
    for n in range(i, j + 1):
        basket[n - 1] = k

for n in range(N):
    print(basket[n], end = ' ')