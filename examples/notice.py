# 登陆获取通知例子
from whuapi import *

lgn = Login()
lgn.login('学号', '密码')  # 登陆
cookies = lgn.cookies  # cookies获取方法
person = Student(cookies=cookies)

print(person.notice())
lgn.logout()
