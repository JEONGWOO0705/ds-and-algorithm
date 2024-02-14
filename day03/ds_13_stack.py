# DATE : 20240214
# FILE : ds_11_stack.py
# DESC : 스택 전체 구현

import webbrowser
import time

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
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드
if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'nate.com', 'bing.com', 'github.com']

    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1)

    print('방문 종료')
    print(stack)
    time.sleep(5) # 5초 동안 아무것도 하지 않고 대기

    print(stack)

    while True:
        url = pop() # 여기 url은 for 문의 url과 다름!
        if url == None: break

        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1)
    print('방문 종료')