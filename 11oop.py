# 파이썬 oop
# 파이썬 객체지향 프로그래밍
# OOP: Object Orientied Programming
# 프로그램을 명령어들의 단순 그룹체라고 보는 시각에서 벗어나,
# 하나의 독립된 객체들의 모음이라고 보는 시각에 근거해서 프로그래밍하는 패러다임

# 프로그램을 보다 유연하게 작성할 수 있고, 프로그램 코드의 재사용을 높일 수 있으며
# 대규모 소프트웨어 개발시 유지보수가 용이해짐

# 프로그램의 각 구성 요소를 실제 세계의 객체와 유사하게 디자인해서 클래스로 정의하는 것에 중점

# ex) 성적 처리 프로그램 I
# 성적 데이터 입력
# name = input('이름은? ')
# kor = int(input('국어는? '))
# eng = int(input('영어는? '))
# mat = int(input('수학은? '))
#
# # 성적 처리
# tot = kor + eng + mat
# mean = tot / 3
# grd = '가'
# if mean >= 90: grd = '수'
# elif mean >= 80: grd = '우'
# elif mean >= 70: grd = '미'
# elif mean >= 60: grd = '양'
#
# # 결과 출력
# print('입력 : %s %d %d %d' % (name, kor, eng, mat))
# print('결과 : %d %.1f %s' % (tot, mean, grd))

# # ex) 성적 처리 프로그램 II
# # 함수 기반 프로그래밍: 처리 코드들을 하나의 이름으로 묶음

# def SungJukProgram(): # 함수에 너무 많은 기능 부여
#     pass # 하나의 기능만 부여

def readSungJuk():
    name = input('이름은? ')
    kor = int(input('국어는? '))
    eng = int(input('영어는? '))
    mat = int(input('수학은? '))

    return name, kor, eng, mat

def computeSungJuk(kor, eng, mat):
    tot = kor + eng + mat
    mean = tot / 3
    grd = '가'
    if mean >= 90: grd = '수'
    elif mean >= 80: grd = '우'
    elif mean >= 70: grd = '미'
    elif mean >= 60: grd = '양'

    return tot, mean, grd

def printSungJuk(name, kor, eng, mat, tot, mean, grd):
    print('입력 : %s %d %d %d' % (name, kor, eng, mat))
    print('결과 : %d %.1f %s' % (tot, mean, grd))

# 성적 처리 프로그램 실행
name, kor, eng, mat = readSungJuk()
tot, mean, grd = computeSungJuk(kor, eng, mat)
printSungJuk(name, kor, eng, mat, tot, mean, grd)

# ex) 성적 처리 프로그램 III
# OOP 기반 프로그래밍: 함수들과 관련 변수를 하나로 묶음

class SungJukVO(): # 변수들로 구성된 클래스
    pass

class SungJukDAO(): # 처리 코드들로 구성된 클래스
    pass

# 객체지향에서의 클래스 특성
# 1. 값만을 저장하는 클래스: VO(value object),
#                             DTO(data transfer object)
# 2. 기능만을 모아둔 클래스: DAO(data access object)
#                             BO(business logic object)
# 프로그램이 제공하는 기능: CRUD (create, read, update, delete)
# 3. UI을 모아둔 클래스: UO(user interface object)

# 클래스 사용 이전
redCarSize = 100
redCarColor = 'red'
redCarWheels = 4
redCarDoors = 4
redCarisLoad = True

redCarSize = 100
redCarColor = 'red'
redCarWheels = 4
redCarDoors = 4
redCarisLoad = True

redCarSize = 100
redCarColor = 'red'
redCarWheels = 4
redCarDoors = 4
redCarisLoad = True

# 자동차 클래스 정의
# '차'라고 인지할만한 특성 정의
class Car:
    def __init__(self, size, color, wheels, doors, isLoad): # 생성자
        self.size = size
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.isLoad = isLoad

    def __str__(self):
        return '우우우웅~'

# 객체 생성
# 클래스를 통해 생성된 실제 결과물
# 여기에는 데이터와 기능을 포함되어 있음
# ex) 붕어빵 <- 붕어빵 틀에 밀가루 반죽과 팥을 넣어 만듦
# 변수명 = 클래스이름(초기값들)
redCar = Car(100, 'red', 4, 4, True)
greenCar = Car(50, 'green', 4, 4, True)
bluenCar = Car(10, 'blue', 4, 4, True)

# 객체의 속성에 접근하려면 .연산자를 이용
# 즉, '객체명.속성명' 형식을 사용해서 객체의 속성을 볼 수 있음
print(redCar.size, redCar.color, redCar.wheels, redCar.doors, redCar.isLoad)

# 객체명만 호출하면 클래스에 정의해둔 __str__가 호출되어 결과 출력
print(redCar)

# 성적 처리를 위한 성적 클래스를 정의하세요
# 이름, 국어, 영어, 수학, 총점, 평균, 학점으로 구성
class SungJuk:
    def __init__(self, name, kor, eng, mat, tot=0, avg=0, grd='가'):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = tot
        self.avg = avg
        self.grd = grd

    def __str__(self):
        result = f'{self.name} {self.kor} {self.eng} {self.mat} \n' \
                 f'{self.tot} {self.avg} {self.grd}'
        return result

sj1 = SungJuk('혜교', 86, 74, 46)

print(sj1)

# 사원 관리를 위한 사원 클래스를 정의
# 사원번호, 성, 이름, 이메일, 전화번호, 입사일, 직책, 급여, 수당, 상사, 부서번호로 구성
class Employee:
    def __init__(self, empno, fname, lname, email, phone, hdate, jobid, salary, mngid, deptid):
        self.empno = empno
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid = jobid
        self.salary = salary
        self.mngid = mngid
        self.deptid = deptid

    def __str__(self):
        result = f'{self.empno} {self.fname} {self.lname} {self.email} {self.phone} \n' \
                 f'{self.hdate} {self.jobid} {self.salary} {self.mngid} {self.deptid}'
        return result

emp = Employee(100, 'Steven', 'King', 'steven@gmail.com', '12345678',
               '2003-06-17', 'AD_PRES', 24000, '', 90)

print(emp)