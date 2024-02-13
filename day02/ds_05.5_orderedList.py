# DATE : 20240213
# FILE : ds_05_orderedList.ipynb
# DESC : 선형 리스트

## 함수 선언 부분

def printPoly(t_x,p_x):
    polyStr = 'P(x) = '

    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]

        if (coef>=0):
            polyStr += "+"
        polyStr += str(coef) + 'x^' + str(term) + ''

    return polyStr

def calcPoly(xVal, t_x, p_x):
    retValue = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xValue ** term
    
    return retValue

## 전역변수 선언 부분##

tx = [300,200,0]
px = [7,-4,5]

## 메인 코드 부분 ##

if __name__ =='__main__':
    pStr = printPoly(tx,px)
    print(pStr)

    xValue = int(input('x값 --> '))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)
