num1 = 10
num2 = 20
num3 = num1 + num2 # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2 # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2 # 정수 + 실수 = 실수

# 매출액 구하기
print('1분기 매출을 구합니다')
january = int(input('1월 매출을 입력하세요'))
february = int(input('2월 매출을 입력하세요'))
march = int(input('3월 매출을 입력하세요'))
quater1 = january + february + march
print('1분기 매출액은 ' + quater1 + '원입니다')

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
num3 = float(num3)
num3 = int(num3)

# 수익 구하기
print('1분기 수익을 구합니다')
sales = int(input('1분기 매출을 입력하세요'))
purchase = int(input('1분기 매입을 입력하세요'))
revenue = sales - purchase
print('1분기 수익은 ' + revenue + '원입니다')

# 방 넓이 구하기
print('방의 넓이를 구합니다')
width = float(input('방의 폭을 입력하세요'))
length = float(input('방의 높이를 입력하세요'))
area = width * length
print('방의 넓이는 ' + area + '입니다')

str1 = 'Hello, python '
str1 * 3

# BMI 구하기
print('BMI를 구합니다')
height = float(input('키를 입력하세요'))
weight = float(input('몸무게를 입력하세요'))
height = height / 100

BMI = weight / (height * height)
print('BMI는 {0:.2f}입니다'.format((BMI)))
print(f'BMI는 {BMI:.2f}입니다') # f-string: py 3.6부터 지원

# print 출력 속도: .format > % > f-string

'hello' / 2

# 동전 갯수 알아보기
print('동전의 갯수를 알아봅니다')
coin = int(input('손 안에 있는 동전의 갯수를 입력하세요'))

isEven = coin % 2
print(f'동전의 홀짝 여부 (0:짝 / 1:홀) {isEven}')

10 / 3
10 // 3

# 빵 분배하기
# 빵, 나눠줄 빵의 갯수 입력받음
# 최대 몇 명까지 나눠줄 수 있는지와 나머지 출력
bread = int(input('빵의 총 갯수는? '))
diver = int(input('나눠줄 빵의 갯수는? '))

stud = bread // diver
divmod = bread % diver

print(f'{bread}개의 빵은 {diver}개씩, {stud}명의 학생에게 나눠줄 수 있고,')
print(f'{divmod}개의 빵이 남았습니다')

2 ** 3
2 ** 8
2 ** 7

2 ** 30

# 복리 계산기
# 원금, 유치 기간, 연 이율을 입력받아 복리 계산 후, 총 수령액 출력
# 1년차 -> 원금 * 이율 = 원금
# ...
# 5년차 -> 원금 * 이율 = 원금

money = 5_000_000
duration = 5
interest = 5.0

takes = money + (money * 0.05) # 1년차
# takes = takes + (takes * 0.05) # 2년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 3년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 4년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 5년차
takes += takes * 0.05

# 어린이 범퍼카 탑승 가능 판별하기
height = int(input('어린이의 신장을 입력하세요'))
isRide = height >= 120
print(f'탑승 가능 여부: {isRide} (True: 탑승 가능)')

'a' == 'b'
'a' > 'b' # 아스키코드로 변환 후 비교

# 범퍼카 탑승 가능 여부 확인
height = int(input('어린이의 신장을 입력하세요'))
# isRide = height >= 120 and height < 170
isRide = 120 <= height < 170
print(f'탑승 가능 여부: {isRide} (True: 탑승 가능')

temp = 0
temp <= 16 or temp > 28

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15) # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15) # True and False

# (num1 < 5) and xyz # py38만 지원

# 삼항 연산자
# 참일 때 값 if 조건식 else 거짓일 때 값

num = 11
'짝수' if (num % 2 == 0) else '홀수'

# 적자/흑자 판단하기
income = int(input('수입은? '))
outcome = int(input('지출은? '))
result = '흑자' if (income > outcome) else '적자'
print(result)

# 윤년 여부 알아보기
# 4로 나눠 떨어지고, 100으로 나눠 떨어지지 않음
# 400으로 나눠 떨어짐
year = int(input('연도는? '))
isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
result = '윤년' if (isLeap) else '평년'
print(result)

# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 20) # 정수 몫: //
op.truediv(10, 20) # 실수 몫: /
op.mod(10, 3)
op.pow(2, 30)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.gt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급재난지원금 대상자 판별하기
income = int(input('월 소득을 입력하세요 '))
resource = int(input('다른 지원금을 받고 있습니까? 1: 받고 있다 / 2: 받고 있지 않다 '))
isTarget = op.and_(op.le(income, 4_000_000) and op.eq(resource, 2))
result = '수급 대상자' if (isTarget) else '해당 사항 없음'
print(result)

# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램
gugudan = int(input('출력할 구구단의 단을 입력하세요 '))
print

# 키보드로 정수를 하나 입력받아 그 값이 정수, 음수, 0인지 구분하는 프로그램
# 각각의 경우에 따라 “정수입니다”, “음수입니다”, “0입니다”라고 출력

# 지금 현재 수지의 통장잔액이 25,000원이다. 은행 이자가 연 6%라 가정할 때,
# 몇 년이 지나야 통장 잔액이 지금의 2배를 넘는지 알아보는 프로그램