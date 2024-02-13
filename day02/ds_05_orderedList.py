# DATE : 20240213
# FILE : ds_05_orderedList.ipynb
# DESC : 선형 리스트

## 함수 선언 부분

def printPoly(p_x):
    term = len(p_x) -1
    polyStr = 'P(x) = '

    for i in range(len(px)):
        coef = p_x[i]

        if(coef >= 0):
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + ''
        term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x)-1
    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue


## 전역 변수 선언 부분 ##
px = [7,-4,0,5]

## 메인 코드 부분 ##
if __name__ =='__main__':
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('X값 -> '))
    pxValue = calcPoly(xValue, px)
    print(pxValue)
