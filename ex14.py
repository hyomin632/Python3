# 출석부 관리 시스템
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']

# 1. 가나다순 정렬
students.sort()
print(students)

# 2. 박찬호 전학
students.remove('박찬호')
print(students)
print(len(students))

# 3. 앞에서 학생 3명 선발
print(students[:3])

# 4. 새로운 학생 이병규 전학
students.append('이병규')
print(students)

# 5. 학생 순서를 역순으로
students.reverse()
print(students)

# 6. 학생 이름 변경: 정우람 -> 정잘남
students[2] = '정잘남'
print(students)