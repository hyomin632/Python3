# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고,
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한 여러 코드들을 함수화하면 프로그램의 흐름을 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시, 코드가 섞이지 않게 하기 위한 목적도 있음 -> 모듈

def startSensor():
    print('온도 센서를 작동합니다')

def stopSensor():
    print('온도 센서를 중지합니다')

startSensor()
stopSensor()

# 노트북 인치 알아내기
# 1cm -> 0.393701 inch

def converstCm2Inch(cm):
     return (f'{cm * 0.393701:.2f}')
    # print(cm * 0.393701)

cm = int(input('파우치 길이를 입력하세요 '))
print(converstCm2Inch(cm))
# convertCm2Inch(cm)


# 이동 거리 계산
def computeDistance(time, speed):
    print(f'이동 거리는 {time * speed}km 입니다')

time = float(input('이동 시간을 입력하세요 '))
speed = float(input('이동 속도를 입력하세요 '))
computeDistance(time, speed)

def add():
    print(a + b)

a = int(input('a는? '))
b = int(input('b는? '))

add()
