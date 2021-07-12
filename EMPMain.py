from EMP import EMP
from EMPService import EMPService

emp = EMP(100, 'Steven', 'King', 'steven@gmail.com', '12345678',
               '2003-06-17', 'AD_PRES', 24000, '', '', 90)

print(emp)

# empsrv = EMPService() # 객체 생성
# emp = empsrv.readEmp() # 메서드 호출
# print(emp)

emp = EMPService.readEmp() # 객체 생성 없이 바로 메서드 호출
print(emp)

# from datetime import datetime
# now = datetime(2021, 7, 12)
# hire = datetime(2003, 6, 17)
# now - hire # 근무일수

EMPService.computeDuty(emp)
