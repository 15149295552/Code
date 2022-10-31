[TOC]

# DJANGO-DAY01

## 一、介绍

### 1）第三阶段课程介绍

* 课程内容（<font color=red>19个工作日</font>）
  1. DJANGO框架（<font color=red>6个工作日左右</font>）
  2. Redis数据库（<font color=red>2个工作日左右</font>）
  3. Ajax（<font color=red>1个工作日左右</font>）
  4. 综合项目（<font color=red>10个工作日左右</font>）
* 目的
  1. 从事Python开发工程师岗位
  2. 其他岗位附加技能
  3. 提升编码能力，培养编程思维

* 特点

  抽象、知识点多、代码量大

### 2）自我介绍

* 姓名：王伟超
* 邮箱：wangweichao@tedu.cn

## 二、Python就业岗位

* Python开发工程师
* 人工智能工程师
* 数据分析工程师（**不好从事**）
* 爬虫工程师（**TTS赠送爬虫视频**）
* 自动化测试工程师（**补充相关测试内容**）
* 自动化运维工程师（**不好从事**）

## 三、DJANGO项目

### 1）项目流程

* 创建并启动项目

  `1.django-admin startproject 项目名`

  `2.cd 项目名`

  `3.python3 manage.py runserver`

* 全局配置settings.py

  `1.LANGUAGE_CODE = "zh-Hans"`

  `2.TIME_ZONE = "Asia/Shanghai"`

* 编写路由urls.py

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path("xxx/xxx", views.函数名),
  ]
  ```

* 完成视图views.py

  ```python
  from django.http import HttpResponse
  
  def xxx_view(request):
     	return HttpResponse("xxx")
  ```

* 浏览器测试

## 2）项目目录结构

django-admin startproject 项目名

```python
项目目录
  |--manage.py # 负责启动项目、创建应用、数据库...
  |--同名目录
      |--settings.py # 全局配置
      |--urls.py     # 路由
      |--views.py    # 视图:负责业务逻辑处理
      |--models.py   # 模型:负责和数据库交互
      |--wsgi.py     # 项目部署
      |--asgi.py     # 项目部署
```

### 3）settings.py中常见配置

1. BASE_DIR: `项目目录的绝对路径`
2. DEBUG: `开发模式DEBUG=True`
3. ALLOWED_HOSTS: `允许的请求头host值`
4. INSTALLED_APPS: `应用列表`
5. TEMPLATES: `模板文件,存放html`
6. DATABASES: `配置数据库`
7. LANGUAGE_CODE: `语言，zh-Hans` 
8. TIME_ZONE：`时区,Asia/Shanghai`

### 4）path转换器

* 作用

  将URL地址的数据按照关键字传参的方式传给视图函数。

* 语法格式

  `<类型:自定义变量名>`

* 示例

  * URL: `http://127.0.0.1:8000/user/liying`

  * urls.py

    `path("user/<str:username>", views.user_view)`

  * views.py

    ```python
    def user_view(request, username)
    	return HttpResponse("xxx")
    ```

* 常见的path转换器

  * str转换器：`<str:自定义变量名>`
  * int转换器：`<int:自定义变量名>`

### 5）常见服务端口号

* MySQL：3306
* http：80
* https：443
* django项目默认端口号：8000

## 四、HTTP请求和响应

### 1）请求内容

* 起始行：`请求方法、请求路由、使用协议`

* 请求头

  * Accept：浏览器希望获取什么类型数据
  * Content-Type：指明请求体数据类型，text/html、text/plain、application/json。

* 请求体

  前端需要交给服务器端数据，可以是Form表单形式提交，也可以是json形式提交。

### 2）请求方法

* GET：`在服务器端获取资源`
* POST：`在服务器端新增资源`
* PUT：`在服务器端更新资源`
* DELETE：`在服务器端删除资源`

<font color=red>**四种请求对应了对服务器端资源的增删改查四种操作，这只是一套指导规范，具体以入职以后的公司风格为准。**</font>

### 3）HttpRequest请求对象

* 说明

  视图函数的第一个参数是HttpRequest请求对象，服务器端收到请求后，会根据请求数据报文创建请求对象。

* 请求对象属性

  |  属性  |            作用            |  数据类型  |
  | :----: | :------------------------: | :--------: |
  | method |          请求方法          |   字符串   |
  |  GET   |         查询字符串         | QueryDict  |
  |  POST  | 请求体数据：以表单形式提交 | QueryDict  |
  |  body  | 请求体数据：以json形式提交 | 字节串:b"" |
  |  META  |         请求头数据         |  字典:{}   |

  注意：<font color=green>**request.META: Django会把所有请求头都大写，并加上HTTP_前缀，比如：HTTP_ACCEPT、HTTP_USER_AGENT等。也可以获取客户端的IP地址：REMOTE_ADDR**</font>







1. 启动项目
2. pycharm打开项目
3. 确认数据库数据表
4. 浏览器输入地址确认登录功能是否正常



1. 原来项目停止
2. 创建并启动新项目：mysite2
3. 全局配置：禁用csrf中间件、设置语言和时区

- 访问地址: <http://127.0.0.1:8000/birthday>
- 最终输出: 生日为: xxxx年xx月xx日
- 要求：
  - GET请求：以查询字符串方式传递：`http://127.0.0.1:8000/birthday?year=xxxx&month=xx&day=xx`
  - POST请求：在表单中传递（**birth.html**）



状态码：

* 404：路由匹配路由（**URL和urls.py**）
* 403：禁用csrf中间件
* 500：检查视图函数（**views.py**）
* 200：成功





templates



用户模块：登录、注册、第三方登录... ...

​      views.py   实现用户模块所有功能

​      templates目录：存放用户模块所有html文件

商品模块：首页、列表页、详情页... ...

​      views.py   实现商品模块所有功能

​      templates目录：存放商品模块所有html文件



浏览器：http://127.0.0.1:8000

​     index.html       这是我的首页！



* settings.py中指定目录，并创建目录
* 在目录中创建html文件
* 视图中将此html文件返回给浏览器





浏览器：http://127.0.0.1:8000/v1/nba/index

返回：NBA:也是我现在正服下的毒药

应用名：nba



项目名：teduproject

应用名：users

实现功能：注册功能

实现方式：POST请求（Form表单）

* 请求的路由

  http://127.0.0.1:8000/v1/users/register

* 请求的方法

  POST

* 请求体数据（**register.html**）

  请输入用户名（username）：

  请输入密码（password）：

  请再次输入密码（password_again）：

  请输入邮箱（email）：

  请输入手机号（mobile）：

* 返回响应

  用户名已被占用

  两次密码不一致

  恭喜你，xxx，注册成功

关于数据库及表：

库名：tedudb

表名：user_profile

表字段：

```mysql
id 整型 主键 自增
username varchar(20),
password char(32),
email varchar(100),
mobile char(11),
unique(username)
```

附赠：md5加密代码

```python
import hashlib

m = hashlib.md5()
m.update("123456".encode())
md5_pwd = m.hexdigest()
```





