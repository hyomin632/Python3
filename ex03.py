# 이름, 국어, 영어, 수학을 입력받아 총점, 평균, 학점을 출력하는 프로그램
name = str(input('이름은? '))
kor = int(input('국어 점수는? '))
eng = int(input('영어 점수는? '))
mat = int(input('수학 점수는? '))

tot = kor + eng + mat
avg = tot % 3
grd = '수' if (avg >= 90) else \
      '우' if (avg >= 80) else \
      '미' if (avg >= 70) else \
      '양' if (avg >= 60) else '가'

print(f'이름: {name}, 국어: {kor}, 영어: {eng}, 수학: {mat}' \
      f'총점: {tot}, 평균: {avg:.1f}, 학점: {grd}')