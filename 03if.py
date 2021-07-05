# if문
num = int(input('숫자를 하나 입력하세요 '))

if (num > 10):
    print('num은 10보다 크다')

# 속도 위반 경고하기
speed = int(input('자동차의 현재 속도를 입력하세요 '))
if (speed > 50):
    print('속도 위반!!')

if speed > 50: print('속도 위반!!')

# 합격/불합격 출력: if ~ else
score = int(input('점수를 입력하세요 '))

if (score > 80):
    print('합격입니다')
else:
    print('다음에 다시 도전해주세요')

# 실행문이 아직 정해지지 않은 경우, pass 키워드로 대체 작성 가능
# if (score >= 80):
#     pass
# else:
#     pass

# 기계 온도를 감지하여 팬을 자동으로 구동하는 프로그램
temp = int(input('기계 온도를 입력하세요 '))

if temp >= 40:
    print('팬(fan) 가동')
else:
    print('팬(fan) 중지')

# 입력받은 정수를 3으로 나눠 소수점 첫째자리가 0.5 이상인 경우 반올림해서 출력하고,
# 그렇지 않은 경우 그대로 출력하는 프로그램
num = int(input('정수를 하나 입력하세요 '))

result = num / 3
if (result - int(result) >= 0.5):
    result = int(result) + 1 # 소수점 이하자리를 버린 후 올림
else:
    result = int(result) # 소수점 이하자리만 버림

print(f'결과: {result}')

# 마일리지 사용
mileage = int(input('마일리지를 입력하세요 '))

if mileage >= 1000:
    print('마일리지 사용 가능')
else:
    print('마일리지 사용 불가')

# 성적 처리
jumsu = int(input('점수를 입력하세요 '))

if 60 <= jumsu < 70:
    print('양')
elif 70 <= jumsu < 80:
    print('미')
elif 80 <= jumsu < 90:
    print('우')
elif 90 <= jumsu <= 100:
    print('수')
else:
    print('가')

# 자동 주문 시스템
language = int(input('Good morning. Nice to meet you. \n'
                     'Where are you from?\n Please select a number \n'
                     '1. 대한민국   2. USA  3. 中國'))

if language == 1:
    print('주문하시겠어요?')
elif language == 2:
    print('Would you like to order?')
elif language == 3:
    print('중국어 중국어')
else:
    print('Would you like to order?')

# 국가재난지원금 수령액 조회
person = int(input('가구 인원 수를 입력하세요 '))

if person == 1:
    print('400,000원 지원')
elif person == 2:
    print('600,000원 지원')
elif person == 3:
    print('800,000원 지원')
else:
    print('1,000,000원 지원')

# BMI 지수 프로그램
bmi = int(input('BMI 지수를 입력하세요 '))

if bmi > 30:
    print('고도 비만')
elif bmi > 25:
    print('비만')
elif bmi > 23:
    print('과체중')
elif bmi > 18.5:
    print('정상 체중')
else:
    print('저체중')

# 버스 전용차로 단속 프로그램
msg = '1. 월~금, 2. 토요일, 3. 공휴일 \n' \ 
      '요일을 선택하세요(1~3) '
day = input(msg)

if day == '2':
    msg = '토요일 및 공휴일은 단속하지 않습니다'
else:
    msg = '버스 전용차로 단속 중입니다'
print(msg)

msg = '1. 버스, 2. 승용차 \n'\
      '차종을 선택하세요(1~2) '
car = input(msg)

if car == '1':
    msg = '버스입니다'
elif car == '2':
    if day == '1':
        msg = '버스 전용차로 위반!'
    else:
        msg = '승용차입니다'
print(msg)

# 출생연도에 따른 마스크 구매 요일 출력 프로그램
fbirth = int(input('출생연도 끝자리 입력: '))
age = int(input('만 나이 입력: '))

day = ''
if age < 65:
    if fbirth == 1 or fbirth == 6: day = '월'
    elif fbirth == 2 or fbirth == 7: day = '화'
    elif fbirth == 3 or fbirth == 8: day = '수'
    elif fbirth == 4 or fbirth == 9: day = '목'
    elif fbirth == 5 or fbirth == 0: day = '금'
    print(f'{day}요일에 구매 가능합니다')
else:
    print('언제든지 구매 가능합니다')
