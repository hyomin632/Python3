# 문자열은 문자들의 리스트와 유사
# 따라서, 리스트 슬라이싱을 통해 문자열 내 개별 문자를 추출할 수 있음

# '파이썬은완전재미있어요'에서 홀수 위치에 있는 문자를 '#'으로 출력하는 코드 작성

str = '파이썬은완전재미있어요'
print(str)

for i in range(len(str)):
    if i % 2 == 0: print(str[i], end='')
    else: print('#', end='')
print()

# 문자열 함수
# 대소문자 변환
str = 'Python is Easy. 그래서 programming이 재미있어요'
str.lower()
str.upper()
str.swapcase()
str.title()

# 문자열 찾기
str = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠 ㅎㅎ..'

str.count('공부') # 특정 문자열 포함 갯수

str.find('공부') # 특정 문자열 위치 찾기(왼쪽 기준)
str.find('공부', 5) # 특정 인덱스를 시작으로 문자열 위치 찾기(왼쪽 기준)
str.find('공부', str.find('공부') + 1)
str.find('없다') # 찾지 못하는 경우 -> -1
str.rfind('공부') # 특정 문자열 위치 찾기(오른쪽 기준)

str.index('공부')
str.index('공부', 5)
str.rindex('공부')
str.index('없다') # 찾지 못하는 경우 -> 오류 발생!

str.startswith('파이썬') # 특정 문자열로 시작하는지 여부
str.startswith('파이썬', 10) # 특정 인덱스 이후로 특정 문자열로 시작하는지 여부
str.startswith('물론', 15)
str.endswith('..') # 특정 문자열로 끝나는지 여부

# 문자열 내 공백 다루기
str = ' 파   이   썬 '
str.strip() # 앞뒤 공백 제거: 매개변수가 없음
str.rstrip() # 오른쪽 공백 제거
str.lstrip() # 왼쪽 공백 제거

str = '--파---이---썬--'
str.strip('-') # 지정 문자 제거: 매개변수로 제거할 문자 지정
str.rstrip('-') # 오른쪽 문자 제거
str.lstrip('-') # 왼쪽 문자 제거

str = '<<파 << 이 >> 썬>>'
str.strip('<>') # 지정 문자들 제거: 매개변수로 제거할 문자열 제거
str.rstrip('<>')
str.lstrip('<>')

str = '열심히 파이썬 공부중~'
str.replace('파이썬', 'Python') # 지정한 문자열을 새로운 문자열로 변경

str = ' 파   이   썬 '
str.replace(' ', '')

str = '--파---이---썬--'
str.replace('-', '')

str = '<<파 << 이 >> 썬>>'
str = str.replace('<', '')
str = str.replace('>', '')
str.replace(' ', '')

# 문자열 분리 결합
str = '혜교,98,75,64' # 구분 기호로 문자열을 분리하고 리스트로 저장
str.split(',')

str = '혜교|98|75|64'
str.split('|')

str = '혜교\r\n98\r\n75\r\n64'
str.split('\r\n') # 줄바꿈 기호 기준 문자열 분리
str.splitlines()

str = ['혜교', '98', '75', '64']
','.join(str) # 리스트의 각 항목을 구분 기호로 결합

result = '' # join을 사용하지 않은 경우
for s in str:
    result += s + ','

# 객체를 특정 함수에 일괄적으로 적용하기
# map(적용할 함수명, 대상 객체)
str = ['123', '456', '789'] # 문자열을 숫자로 변경

nums = [] # map을 사용하지 않는 경우
for s in str:
    nums.append(int(s))

nums = list(map(int, str))

# 문자열 정렬하기

# 특정 문자로 채우기

# 문자열 구성 파악하기

# 입력한 값이 한글/영어이면 '글자', 숫자면 '숫자', 혼합이면 '글자+숫자',
# 그 외 나머지 문자면 '모르겠습니다'라고 출력하는 프로그램
str = input('문자를 입력하세요')

result = ''
if str.isalpha(): result = '글자입니다'
elif str.isdigit(): result = '숫자입니다'
elif str.isalnum(): result = '글자 + 숫자입니다'
else: result = '모르겠습니다'

print(result)