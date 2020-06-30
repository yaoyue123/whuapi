#登陆获取课表的例子
from whuapi import *

lgn = Login()
lgn.login('学号', '密码')  # 登陆
cookies = lgn.cookies  # cookies获取方法
person = Student(cookies=cookies)
schedule = person.schedule('2019', '2')  # 2019年、第1学期(1 or 2 or 3)
print(schedule)
