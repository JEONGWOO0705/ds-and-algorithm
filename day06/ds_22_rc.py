# DATE : 20240219
# FILE : ds_22_rc.py
# DESC : 재귀 호출

## 재귀호출은 무한 루프 같지만 시간이 지나면 오류가 나면서 멈추게 됨!!!

import time

def open_box():
    global count
    print(f'{count} 번째 상자를 엽니다')
    count -= 1
    if count == 0:
        print(' 반지를 넣고 반환 합니다.')
        return  # 반복 종료 선언문  -->> 이걸 빼면 계속해서 진행됨
    time.sleep(0.5) # 0.5초 동안 딜레이
    open_box()
    print('상자를 닫습니다.')

# 전역 변수
count = 10

if __name__ == '__main__':
    open_box()