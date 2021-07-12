# 근무 시간에 필요한 컴퓨터 수량
# 컴퓨터 수 * 근무 시간
# 3 * 8 = computer * time
# computer = 3 * 8 / time
time = int(input('근무 시간을 입력하세요 '))

computer = 3 * 8 // time
addCom = 1 if (3 * 8 % time) > 0 else 0
print(f'필요한 컴퓨터: {computer + addCom}')