import keyword

myName = "Yoon Go Eun"
myMajor = "Global tourism management"

print(myName)
print(myMajor)

myName = 100
myName = True
myName = False
myName = 3.141519

intro = 'Hello'
print(intro)
intro = '안녕하세요'
print(intro)

nickname = '별명'
nickname

print(keyword.kwlist)
# print(keyword.softkwlist)

bigint = 1234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345
print(bigint)

bigfloat = 1.23451234512345123451243512345123451234512345
print(bigfloat)

a = 123
b = '456'

a = a + 1
# b = b + 1  '' 안에 있어서 문자형 되었음. 그래서 더하기가 안되었음
# 논리형은 true false 앞에 대문자로 써놓아야함

print(type('안녕하세요'))
print(type(123))
print(type(1.23))
print(type(True))

# 다중 선언
x = 1
y = 1
z = 1

x = y = z = 3

# 자릿수 구분
million = 1000000
million = 1_000_000

# 논리값 확인 : bool
bool(True)
bool(1)
bool(100)
bool(-100)
bool(0)

# 자료형 변환
str(123)
int('456')
float('3.14')

# 58p 확인문제
currentTemp = 25
targetTemp = 30
print('현재온도')
print(currentTemp)
print('설정온도')
print(targetTemp)
print('설정 온도와 현재 온도의 차이')
print(targetTemp - currentTemp)

# 데이터 복사
var1 = 123
var2 = var1
print(var2)
var1 = 321
print(var1)

# input() 함수 () 안에다 입력받을때 출력할 문자 출력 가능
# userData = input('이름을 입력하세요 : ')
# print(userData)

# 성적 처리 프로그램
name = input('이름을 입력하세요 : ')
kor = int(input('국어 : '))
eng = int(input('영어 : '))
mat = int(input('수학 : '))
tot = kor + eng + mat
avg = int(tot / 3)
print('이름:{}, 국어:{}, 영어:{}, 수학:{}, 총점:{}, 평균:{}'.format(name, kor, eng, mat, tot, avg) )
