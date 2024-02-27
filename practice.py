# 1에서 30까지 배열 생성
stu = [i for i in range(1, 31)]

# for loop로 받은 학번은 remove로 배열에서 제거
for i in range(28):
    asg = int(input())
    stu.remove(asg)

print(min(stu))
print(max(stu))