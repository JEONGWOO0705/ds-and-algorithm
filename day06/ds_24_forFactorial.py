# DATE : 20240219
# FILE : ds_24_forFactorial.py
# desc : 반복문으로 팩토리얼 구하기 fact(n) = n! = 1 x 2 x 3 ...x (n-1) x n
n = 20
factValue = 1   # 곱셈이므로 1부터

for i in range(n,0,-1):    # n부터 1까지 역순으로
    factValue *= i

print(f' {n}! = {factValue}')


# 재귀 호출 Factorial

def factorial(num):
    if num <= 1:
        return 1
    
    return num * factorial(num -1)

print(f' {n}! = {factorial(n)}')

# n = 10 --> 3628800
# n = 20
    