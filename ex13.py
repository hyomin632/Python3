# 로그인 기능
for i in range(5):
    userid = input('아이디는? ')
    passwd = input('비밀번호는? ')

    if userid == 'admin' and passwd == 'hanbitac':
        print('로그인 성공!')
        break
    else:
        print('아이디 또는 비밀번호 불일치!')
else:
    print('로그인 실패! 횟수 초과!')

cnt = 1
while True:
    if cnt > 5:
        print('로그인 실패! 횟수 초과!')
        break

    userid = input('아이디는? ')
    passwd = input('비밀번호는? ')

    if userid == 'admin' and passwd == 'hanbitac':
        print('로그인 성공!')
        break
    else:
        print('아이디 또는 비밀번호 불일치!')
    cnt += 1
