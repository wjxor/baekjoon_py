N, M = map(int, input().split())

# 바구니에 번호 부여
basket = [n for n in range(1, N + 1)]

for _ in range(M):
    i, j = map(int , input().split())
    
    #뒤바꾸기 위해 temp에 보관
    temp = basket[i - 1:j]
    temp.reverse()
    basket[i -1:j] = temp

for i in range (N):
    print(basket[i], end=" ")