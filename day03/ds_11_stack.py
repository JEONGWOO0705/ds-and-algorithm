# DATE : 20240214
# FILE : ds_11_stack.py
# DESC : 스택 전체 구현

# 스택 상태 확인 함수
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE -1):
        return True    # 스택이 꽉 찼음
    else:
        return False
    

# Push 함수
def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print('스택이 가득 찼습니다.')
        return
    else:
        top += 1
        stack[top] = data

# isStackEmpty 함수
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1:
        return True # 스택이 비었음
    else:
        return False
    
# pop 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다')
    else: 
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
# peek 함수
def peek():
    global SIZE, top, stack
    if isStackEmpty == True:
        print('스택이 비어있습니다')
        return None
    else:
        return stack[top]
    

# 전역 변수 선언
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드
if __name__ == '__main__':

    while True:
        select = input('PUSH(p), POP(o), PEEK(e), Exit(x) > ')

        if select.lower() == 'p':
            data = input('입력 데이터 >>')
            push(data)
            print(f'스택 상태 : {stack}')
        elif select.lower() =='o':
            data = pop()
            print(f'추출 데이터는 : {data}')
            print(f'스택 상태 : {stack}')
        elif select.lower() =='e':
            data = peek()
            print(f'추출 데이터는 : {data}')
            print(f'스택 상태 : {stack}')
        elif select.lower() == 'x':
            exit(0)
        else: 
            continue

