# 登陆获取分数例子
from whuapi import *

lgn = Login()
lgn.login('学号', '密码')  # 登陆
cookies = lgn.cookies  # cookies获取方法
person = Student(cookies=cookies)

grade = person.grade('2019', '0')  # 2019年、第1学期(0 or 1 or 2 or 3 此处0为全年)
print(grade)
lgn.logout()
