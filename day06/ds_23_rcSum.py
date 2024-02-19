# DATE : 20240219
# FILE : ds_23_rcSum.py
# DESC : 재귀 호출 합산 함수

def addNumber(num):
    if num <= 1:
        return 1
    
    return num + addNumber(num - 1) # 5 + addNumber(4)[4 + addNumber(3)[3 + addNumber(2)[2 + addNumber(1)]]] --> 5+4+3+2+1

sum = addNumber(5)  # 15