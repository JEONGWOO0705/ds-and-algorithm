# DATE : 20240215   
# FILE : ds_17_circularQueue.py
# DESC : 원형큐 구현, 원형 큐에서는 rear|front % size 개념이 핵심


# circular Queue 풀함수
def isQueueFull() :
    global SIZE, rear, queue, front
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False

# Queue 엠티 확인 함수
def isQueueEmpty():
    global SIZE, rear, queue, front
    if front == rear:
        return True
    else:
        return False
    
# Queue 데이터 삽입 함수
def enQueue(data):
    global SIZE, rear, queue, front
    if isQueueFull() == True:   # queue가 꽉차서 데이터 입력 불가
        print('큐가 가득 찼습니다')
        return
    else:
        rear  = (rear + 1) % SIZE   # 원형 큐에서 데이터 입력 공간 확보
        queue[rear] = data


# Queue 데이터 추출 함수
def deQueue():
    global SIZE, rear, queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다')
        return
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

# 추출 데이터 확인 함수
def peek():
    global SIZE, rear, queue, front
    if isQueueEmpty() == True:
        print('Empty!!')
        return None
    else:
        return queue[(front +1) % SIZE ]    # (front + 1) % SIZE != front +1 % SIZE


# 전역 변수

SIZE = int(input('큐 크기를 입력하시오 (정수) : '))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == '__main__':  # 메인 시작
    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x) : ')

        if select.lower() == 'e':
            data = input('입력 데이터 : ')
            enQueue(data)
            print(f'큐 상태 : {queue}')

        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'p':  
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'x':
            break
        else:
            continue  
