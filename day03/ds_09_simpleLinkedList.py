# DATE : 20240214
# FILE : ds_09_simpleLinkedList.py
# DESC : 단순연결리스트 전체 구현

# 노드 클래스
class Node():
    data = None # 실제 데이터 변수
    link = None # 다음 노드를 지정하는 변수

    def __init__(self) -> None:
        # data = None  --->>> 이것은 위에 data와 다름 , 지역변수 데이터로 위에 data와 다른 변수가 됨
        self.data = None    # 클래스 자신이 self이므로 클래스의 변수에 접근하려면 반드시 self
        self.Link = None    


# start부터 시작해서 끝까지 노드의 data를 출력 함수
        
def printNodes(start):  
    global curr
    curr = start    # start == head
    if curr == None: return # break, continue는 반복문이 없으면 안됨
    while True:
        if curr.link == None:   # 뒤에 연결할 노드가 더이상 없으면
            print(curr.data)    # 자기 데이터만 출력하고   
            break               # 반복문을 탈출
        else:
            print(curr.data, end= ' -> ')   #연결할 노드가 있을때는, 연결 표시 ->를 해주고
            curr= curr.link                 # 자기 뒤의 데이터를 curr로 바꿔줌
    print()

# 노드 삽입 함수
def insertNode(find, data):
    global head, prev, curr # 전역 변수를 insertNode()에 사용하겠다 선언

    if head.data == find:   # 맨 첫번째 노드
        node = Node()
        node.data = data
        node.link = head
        head = node
        return  # 함수 탈출
    
    curr = head
    while curr.link != None:    # 중간에 새 노드 삽입
        prev = curr
        curr = curr.link
        if curr.data == find:
            node = Node()
            node.data = data
            node.link = curr    # 찾은 노드 앞에 새 노드 연결
            prev.link = node    # 이전 노드 뒤에 새 노드 연결
            return  # 함수 탈출
        
    node = Node()   # 맨 마지막 노드 삽입
    node.data = data
    curr.link = node
    return

# 노드 삭제 함수
def deleteNode(data):
    global head, curr, prev

    if head.data == data: # 첫번째 노드 삭제
        curr = head
        head = head.link
        del(curr)
        return  # 함수 탈출
    
    curr = head
    while curr.link != None:    # 첫번째 이외 노드 삭제
        prev = curr
        curr = curr.link

        if curr.data == data:
            prev.link = curr.link
            del(curr)
            return

# 노드 검색 함수
def findNode(find):
    global curr, head
    curr = head
    if curr.data == find:
        return curr # 현재 노드를 리턴해주고 함수 탈출
    
    while curr.link != None:
        curr = curr.link    # 다음 노드로 넘어감
        if curr.data == find:
            return curr
    return Node()   # 위에 만족못하면 빈 노드를 생성하고 리턴, 함수 탈출
    

# 전역 변수 선언
head, prev, curr  = None, None, None
originData = ['다현', '정연', '쯔위', '사나', '지효']

# 메인코드 영역

if __name__ == "__main__":
    node = Node()
    node.data = originData[0]   # '다현'이라는 데이터를 할당
    head = node # head는 node를 가르킨다
    
    for name in originData[1:]: # 1번 인덱스 부터 리스트 끝까지
        prev = node
        node = Node()
        node.data = name
        prev.link = node

 # 연결리스트 구성 완료
    print('최초 구성된 연결리스트')
    printNodes(head) # 구성된 연결리스트가 맞는지 출력 확인 
    
    # 다현 -> 정연 -> 쯔위 -> 사나 -> 지효

    print('맨앞 노드 삽입')
    insertNode('다현', '정국')
    printNodes(head)

    # 정국 -> 다현 -> 정연 -> 쯔위 -> 사나 -> 지효


    print('중간 노드 삽입')
    insertNode('사나', '미미')
    printNodes(head)

    # 정국 -> 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효


    insertNode('재남', '알엠') # 재남이란 노드가 없으니 마지막 삽입
    print('마지막 노드 삽입')
    printNodes(head)

    # 정국 -> 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효 -> 알엠

    # 노드 삭제
    deleteNode('정국')
    print('맨앞 노드 삭제')
    printNodes(head)
    # 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효 -> 알엠

    deleteNode('쯔위')
    print('중간 노드 삭제')
    printNodes(head)
    # 다현 -> 정연 -> 미미 -> 사나 -> 지효 -> 알엠

    deleteNode('재남')
    print('없는 노드 삭제')
    printNodes(head)

    # 노드 검색
    fNode = findNode('다현')
    print(f'찾은 노드 : {fNode.data}')
    
    fNode = findNode('쯔위')
    print(f'찾은 노드 : {fNode.data}')
