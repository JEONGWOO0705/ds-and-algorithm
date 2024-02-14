# DATE : 20240214
# FILE : ds_14_stackBracelet.py
# DESC : 스택 수식 정합 여부 판단

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

# 수식 괄호 판단 함수 
def checkBracket(expr): # '(a+b)'
    for ch in expr: # '(' 'a' '+' 'b' ')'   
        if ch in '({[<': # 여는 괄호가 있으면
            push(ch)
        elif ch in ')}]>': # 닫는 괄호가 있으면
            out = pop()
            if ch == ')' and out == '(':
               pass # continue
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False

    if isStackEmpty() == True:
        return True
    else:
        return False

# 전역 변수 선언
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드
if __name__ == '__main__':

    arr = ['(a+b)', ')a*b(', '((a+b)-c)', '(a+b]', '(<a+{b+c}/[c*d]>)']

    print(arr.pop())

    # for expr in arr:
    #     top = -1
    #     print(f'{expr} ==> {checkBracket(expr)}')

