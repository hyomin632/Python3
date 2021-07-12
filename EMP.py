class EMP:
    def __init__(self, empno, fname, lname, email, phone, hdate, jobid='', salary='', comm='', mngid='', deptid=''):
        self.__empno = empno
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__salary = salary
        self.__comm = comm
        self.__mngid = mngid
        self.__deptid = deptid

    def __str__(self):
        result = f'{self.__empno} {self.__fname} {self.__lname} {self.__email} {self.__phone} {self.__hdate} \n' \
                 f'{self.__jobid} {self.__salary} {self.__comm} {self.__mngid} {self.__deptid}'

        return result

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self, empno):
        self.__empno = empno

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def hdate(self):
        return self.__hdate

    @hdate.setter
    def hdate(self, hdate):
        self.__hdate = hdate

    @property
    def jobid(self):
        return self.jobid

    @jobid.setter
    def jobid(self, jobid):
        self.__jobid = jobid

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, comm):
        self.__comm = comm

    @property
    def mngid(self):
        return self.__mngid

    @mngid.setter
    def mngid(self, mngid):
        self.__mngid = mngid

    @property
    def deptid(self):
        return self.__deptid

    @deptid.setter
    def deptid(self, deptid):
        self.__deptid = deptid