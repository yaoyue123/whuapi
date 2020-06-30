# 新版武汉大学教务系统API

[![](https://img.shields.io/badge/主页-@yaoyue123-orange.svg)](https://github.com/yaoyue123) ![](https://img.shields.io/badge/Version-v0.0.1-blue.svg) ![](https://img.shields.io/badge/License-MIT-lightgrey.svg)
基于最新版(2020/06)武汉大学教务系统，而制作的Python第三方库，方便他人的二次开发。

## 目录

- [背景](#背景)
- [功能](#功能)
- [安装](#安装)
- [用法](#用法)
- [更新日志](#更新日志)
- [相关项目](#相关项目)
- [主要项目负责人](#主要项目负责人)
- [参与贡献方式](#参与贡献方式)
    - [贡献人员](#贡献人员)
- [开源协议](#开源协议)

## 背景

由于你武教务系统常年奔溃，遭人诟病。终于在本学期彻底改头换面，导致原有旧教务系统的api接口面临失效的风险。所以我根据[@NeroAsmarr](https://github.com/NeroAsmarr) 的[新版正方教务教务系统API](https://github.com/NeroAsmarr/zfnew)项目 进行了本地化的适配而创建了此项目。

## 功能
*  自动登陆、cookies获取
*  个人信息
*  学校通知
*  成绩
*  课程表

## 安装

1. 使用pip命令安装 `pip install whuapi`

2. 在克隆本项目进行安装
   ```bash
   git clone https://github.com/yaoyue123/whuapi.git
   cd whuapi
   python setup.py build
   python setup.py install
   ```

## 用法
**推荐直接结合调用例子：** [examples](https://github.com/yaoyue123/whuapi/tree/master/examples)

## 更新日志
### v 0.0.1
- 初始版本
- 对个人信息，成绩，课程表等进行了修改。
## 相关项目

[新版正方教务教务系统API项目](https://github.com/NeroAsmarr/zfnew) 

## 主要项目负责人

[@yaoyue123](https://github.com/yaoyue123)

## 参与贡献方式

[![](https://img.shields.io/badge/%E7%94%B3%E8%AF%B7-Pull%20Request-orange)](https://github.com/yaoyue123/whuapi/pulls)

提交 [PR](https://github.com/yaoyue123/whuapi/pulls) 申请，我会视情况通过。

### 贡献人员

感谢所有贡献的人。

[@yaoyue123](https://github.com/yaoyue123)

## 开源协议

[MIT](LICENSE) © yaoyue123