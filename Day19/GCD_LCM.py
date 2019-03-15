import sys
sys.stdin = open('gcd_lcm.txt','r')


# 유클리드 호제법
num1, num2 = map(int, input().split())

if num1 > num2:
    front = num1
    rear = num2
else:
    front = num2
    rear = num1

while True:
    if front % rear ==0:
        break
    mod = front%rear
    front = rear
    rear = mod

print(rear)
print(num1*num2//rear)