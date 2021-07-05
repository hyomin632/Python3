# 차량 2부제 프로그램
carnum = int(input('차량 번호 4자리를 입력하세요 '))
# day = int(input('오늘 날짜를 입력하세요 '))
from datetime import datetime as dt
day = dt.now().day
day = dt.today().day

evenOrodd = '짝수'
if day % 2 != 0: evenOrodd = '홀수'
print(f'오늘 입차: 번호가 {evenOrodd}인 차량')

passOrNot = '입차 불가'
# if carnum % 2 == 0 and day % 2 != 0: # 검사 2번 시행
if carnum % 2 == 0 and evenOrodd == '짝수':
    passOrNot = '입차 가능'

print(f'귀하의 차량은 {passOrNot}합니다')