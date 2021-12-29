import math
import sys

size = int(input('Map Size: '))

if size % 2 == 0:
    sys.exit('Map Size는 홀수로만 입력 해주세요!')

sizeCircle = int(input('Circle Size: '))

if sizeCircle > (size * 2) + 1:
    sys.exit('해당 맵이 작아  원이 들어갈수 없습니다.')

rad = math.pi / 180

center = math.floor(size / 2) # 배열의 중심

array = [[0 for col in range(size)] for row in range(size) ]

def CircularMeasure(r, deg): # r은 반지름
    return [round(center + r * math.cos(deg * rad)), round(center + r * math.sin(deg * rad))]

def GenerateCircle():
    global array
    for theta in range(360):
        x, y = CircularMeasure(sizeCircle, theta)
        array[x][y] = '●'

def render():
    global array

    for y in range(size):
        for x in range(size):
            print(array[y][x], end=' ')
        print()



array[center][center] = '●'
GenerateCircle()
render()
