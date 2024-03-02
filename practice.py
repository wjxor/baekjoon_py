num = []

for i in range(10):
    p = int(input())
    r = p % 42
    num.append(r)

result = set(num)
print(len(result))