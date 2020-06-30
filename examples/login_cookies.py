# 登陆获取cookies例子
from whuapi import *

lgn = Login()
lgn.login('学号', '密码')  # 登陆

cookiejar = lgn.cookies  # cookiejar类的cookies
cookie_str = lgn.cookies_str  # 字符串形式的的cookies
print(cookiejar)
print(cookie_str)
lgn.logout()