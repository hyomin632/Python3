# 반복문
# 1 ~ 10까지 정수 출력
for i in range(1, 10 + 1):
    print(i)

# 2 ~ 10 사이 짝수 출력
for i in range(2, 10 + 1, 2):
    # print(i)
    print(i, end=' ')

for i in range(1, 10 + 1):
    if i % 2 == 0: print(i)

# 사용자가 입력한 횟수만큼 문자열 출력
times = input('메일 발송 횟수를 입력하세요 ')
for i in range(1, 3 + 1):
    print('메일 발송!!')

# 1 ~ 10 사이 정수 출력, 3의 배수이면 '3의 배수!' 출력
for i in range(i, 10 + 1):
    if i % 3 == 0:
        print('3의 배수!')
    else:
        print(f'num = {i}')

# 구구단 5단 출력하기
dan = int(input('단을 하나 입력하세요 (1~9) '))
for i in range(1, 9 + 1):
    print(f'{dan} x {i} = {dan * i}')

# 1 ~ 10까지 정수의 합 출력하기
sum = 0
for i in range(1, 10 + 1):
    sum += i
print(sum)

# 1 ~ 100까지 정수 중에서 3과 7의 공배수와 최소공배수 출력
for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

min = 100
print('3과 7의 공배수', end=' ')
for i in range(100, 1, -1):
    if i % 3 == 0 and i % 7 == 0:
        if min >= i: min = i
        print(i, end=', ')
print(f'\n최소공배수 {min}')

for i in range(-10, 1, 1):
    print(i)

# 1 ~ 10까지 출력
for i in range(10):
    print(i + 1)

# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end=', ')
print()

# 50보다 작은 7의 배수 출력 프로그램
for i in range(50):
    if i % 7 == 0: print(i, end=', ')
print()

# 1 ~ 10까지 출력
num = 1
while num < 10 + 1:
    print(num)
    num += 1

# 1 ~ 30까지의 정수 중 홀수/짝수 구분하여 출력
i = 1
while i < 30 + 1:
    if i % 2 == 0: print(f'짝수: {i}')
    else: print(f'홀수: {i}')
    i += 1

# 구구단 3단 출력하기
i = 1
dan = 19
while i < 9 + 1:
    print(f'{dan} x {i} = {dan * i}')
    i += 1

# 0 ~ 100까지의 정수 중 3과 8의 공배수, 최소공배수
num = 1
min = 999
while num < 100 + 1:
    if num % 3 == 0 and num % 8 == 0:
        print(f'공배수: {num}')
        if min > num: min = num
    num += 1
print(f'최소공배수: {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1: 진행, 2: 종료'))
    if code == 1: print('게임 진행')
    else:
        flag = False
        print('게임 종료')

# 1 ~ 50까지 정수 중 3의 배수를 더하기
sum = 0
for i in range(1, 50 + 1):
    if i % 3 == 0:
        sum += i
print(sum)

sum = 0
for i in range(1, 50 + 1):
    if i % 3 != 0: continue
    sum += i
print(sum)

# 1 ~ 100까지 모든 정수 더하기
# 단, 정수의 총합이 500이 넘었을 때의 정수는 무엇인가
sum = 0
for i in range(1, 100 + 1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# 1 ~ 10까지 정수의 총합을 구하고, 반복이 끝나는 경우 완료 메세지 출력
sum = 0
for i in range(11):
    sum += (i + 1)
else:
    print(f'총합 계산 끝!: {sum}')

# 가로, 세로 길이에 다른 삼각형 너비 구하기
# 단, 너비가 150을 넘으면 프로그램을 종료하고, 이때의 가로/세로 길이 출력
width = 2
height = 3
area = 0
while area <= 150:
    area = (width * height) / 2
    print(area, width, height)
    width += 2
    height += 3

# 1 ~ 100까지 정수 중 5 또는 7의 배수를 제외하고 출력
for i in range(1, 100):
    if i % 5 == 0 or i % 7 == 0: continue
    print(i, end=', ')
print()

# 구구단 출력
for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        print(f'{j:2d} x {i:2d} = {i * j:2d} \t', end=' ')
    print()
print()

# 별 트리 출력하기
print('     *')
print('    ***')
print('   *****')
print('  *******')
print(' *********')
print('***********')


