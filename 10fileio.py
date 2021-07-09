# 파일 다루기

# 입력한 성적 데이터를 파일에 저장
fname = '/Users/celeste/Documents/sungjuk.dat'

name = input('이름은? ')
kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))

f = open(fname, 'w') # 지정한 파일을 쓰기모드로 엶
# data = 'Hello, World!'
data = f'{name} {kor} {eng} {mat}' # 파일에 기록할 내용을 문자열로 작성
f.write(data)
f.close()

# 기록한 성적 데이터를 파일로부터 읽어오기
f = open(fname, 'r')
data = f.read()
print(data)
f.close()

# 일정 관리 메모를 입력하여 텍스트 파일에 저장
def saveMemo(memo):
    fname = '/Users/celeste/Documents/myMemo.txt'
    f = open(fname, 'a') # 추가 모드(append)로 파일을 초기화
    f.write(memo + "\n")
    f.close()

def memoMain():
    memo = input('메모를 입력하세요 ')
    saveMemo(memo)

memoMain()

# py3 방식으로 파일 다루기
# 기존 파일 입출력 코드에서 불편한 점은 파일 작업 후에는 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도 됨
with open(fname, 'w') as f:
    f.write('에에에에엥!')

# 파일에서 데이터 읽어오기
fname = '/Users/celeste/Downloads/연습문제/hr/EMPLOYEES_201808111534.csv'
with open(fname) as f:
    data = f.read() # 모든 데이터를 한 번에 다 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline() # 데이터를 한 줄 읽어옴
    print(data)

with open(fname) as f:
    data = f.readlines() # 모든 데이터를 줄 단위로 읽어옴
    print(data) # 읽어온 결과는 list형식

# employees.csv에서 사번, 이름, 입사일, 급여 출력
with open(fname) as f:
    f.readline() # 첫 줄은 읽기만 함 -> 처리 x
    while True:
        line = f.readline()
        if not line: break # 읽을 데이터가 없는 경우, 작업 중단
        data = line.split(',') # 문자열을 ,로 분리해서 리스트로 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

# 타이타닉 데이터셋을 이용해서 승객이름(name), 성별(sex), 나이(age), 승선위치(embarked), 사망여부(survived) 등을 추출해서 출력
# 단, survived가 0이면 '사망', 1이면 '생존'이라 출력
# embarked가 S이면 'southampton', 'C'이면 'cherbourg', 'Q'이면 'queenstown'이라 출력
fname = '/Users/celeste/Downloads/titanic3b.csv'
with open(fname) as f:
    f.readline()
    while True:
        row = f.readline()
        if not row: break

        data = row.split(',')
        # name = data[2]
        sex = data[2]
        age = data[3]
        embarked = data[9]
        survived = data[1]

        if embarked == 'S': embarked = 'southampton'
        elif embarked == 'Q': embarked = 'queenstown'
        elif embarked == 'C': embarked = 'cherbourg'

        if survived == '0': survived = '사망'
        elif survived == '1': survived = '생존'

        if age == '': age = '0'

        result = f'{sex} {age} {embarked} {survived}'
        print(result)