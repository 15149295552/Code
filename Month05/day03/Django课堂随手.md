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

### 4）关于响应

#### 4.1 响应对象HttpResponse

-  视图函数中

  return  HttpResponse(content="响应体", content_type="类型", status=自定义状态码)

  content_type示例：

  * html格式：`text/html;charset=utf-8`
  * 文本格式：`text/plain;charset=utf-8`
  * json格式：`application/json;charset=utf-8`

#### 4.2 目前遇到的响应状态码

* 404：Page Not find，检查路由和浏览器URL地址是否匹配。

* 403：403 Forbidden，csrf校验未通过，关闭csrf中间件。

  ​		  settings.py中MIDDLEWARE： csrf中间件注释掉。

* 500：服务器错误，检查视图函数。

# DJANGO-DAY02

## 一、设计模式

<font color=red>**所有设计模式的最终作用都是为了降低模块间的耦合度。**</font>

### 1）MVC

* M：模型层model，封装数据库层。
* V：视图层View，展示数据。
* C：控制器层Controller,<font color=red>**核心**</font>，处理用户请求、获取数据、返回结果。

### 2）MTV

* M：模型层model，封装数据库层。
* T：模板层Templates，展示数据。
* V：视图层View，<font color=red>**核心**</font>，处理用户请求、获取数据、返回结果。

## 二、模板层Template

### 1）定义

​	可以根据视图中传递的字典数据动态生成相应的HTML网页，并呈现给用户。

### 2）使用流程

* 项目目录或者应用目录下创建模板目录：templates

* settings.py中配置模板配置项（**TEMPLATES**）

  1. BACKEND：指定模板引擎（<font color=red>**默认**</font>）
  2. DIRS：指定模板的搜索目录（<font color=red>**[BASE_DIR / "templates"]**</font>）
  3. APP_DIRS：是否在应用的templates目录中搜索模板文件（<font color=red>**默认**</font>）
  4. OPTIONS：有关模板的选项（<font color=red>**默认**</font>）

* 创建模板html文件

* 视图函数中render()方法加载模板

  ```python
  from django.shortcuts import render
  
  def xxx_view(request):
      return render(request, "html文件名", 字典数据)
  ```

### 3）模板语言

#### 3.1 模板传参

​	`return render(request, "xxx.html", 字典数据)`

#### 3.2 模板变量

* 语法格式：`{{  }}`
* 分类
  1. 普通变量：{{ 变量名 }}
  2. 列表中指定索引元素：{{ 变量名.index }}
  3. 获取自定中指定的key：{{ 变量名.key }}
  4. 获取指定函数返回值：{{ 变量名.函数名 }}
  5. 获取对象数据：{{ 对象名.方法 }}

#### 3.3 模板标签

* 作用：将一些服务器端的功能嵌入到模板中。

* 标签语法

  ```python
  {% 标签 %}
  ... ...
  {% end标签 %}
  ```

* if标签

  ```python
  {% if 表达式 %}
  	...
  {% elif 表达式 %}
  	...
  {% else %}
  	...
  {% endif %}
  ```

* for标签

  ```python
  {% for 变量名 in 可迭代对象 %}
  	...
  {% empty %}
  	...
  {% endfor %}
  ```

* 加载静态文件

  ```python
  {% load static %}
  <img src="{% static 'liying.png' %}"
  ```

## 三、静态文件配置

* settings.py中配置请求路由和寻址路径

  ```python
  STATIC_URL = "/static/"
  STATICFILES_DIRS = (BASE_DIR / "static",)
  ```

* 项目目录下创建static目录，并存放图片

* 浏览器测试

  `http://127.0.0.1:8000/static/liying.png`

## 四、应用APP

### 1）定义

​	应用是在django项目中独立的一个业务模块，每个应用包含自己的路由、视图、模型、模板。

### 2）使用流程

1. 创建应用：python3 manage.py startapp 应用名

2. 注册应用：settings.py 中 INSTALLED_APPS:  [应用名,]

3. 匹配主路由：<font color=red>**注意：include()方法**</font>

   ```python
   from django.urls import path, include
   
   path("主路由", include("应用名.urls"))
   ```

4. 匹配分布式路由：<font color=red>**单独创建urls.py**</font>

5. 完成视图

<font color=green>**注意：查找模板文件时，优先查找外层的templates目录下的模板文件，如果没有则按照settings.py中INSTALLED_APPS中应用注册的顺序依次逐个查找。**</font>







建表：

```mysql
mysql: create table xxx(id int ......);
oracle: 
sqlite3:
```

增删改查

```python
select * from xxx where xxx;
```





* 创建项目

* 建库

* 配置数据库

  ```python
  DATABASES = {
      "ENGINE": "django.db.backends.mysql",
      "NAME": "库名",
      "HOST": "127.0.0.1",
      "USER": "root",
      "PASSWORD": "123456",
      "PORT": "3306"
  }
  ```

* 模型层的基本操作

  ```python
  from django.db import models
  
  class Xxx(models.Model):
      xx = xx
      xx = xx
  ```

* 迁移同步

  ```python
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

  



1. models.py中创建模型类，指定类属性

   模型类继承models.Model

2. 终端迁移同步

   python3 manage.py makemigrations

   python3 manage.py migrate

3. 数据库中确认

**创建书籍模型类Book，字段书籍名称title，书籍出版社pub，迁移同步到数据库**



**现在时间：2022-10-31**

<font color=red>**insert into xxx(username) values("只手遮天")**</font>

<font color=blue>**现在：11月1日  update xxx set username="么么哒" where username="只手遮天";**</font>

##### username = models.CharField(max_length=20)                   # 么么哒

##### created_time = models.DateField(auto_now_add=True)    # 2022-10-31

##### updated_time = models.DateField(auto_now=True)            # 2022-11-1





**会员信息表：MemberInfo，创建完成后勿忘<font color=red>迁移同步</font>**  

1. 用户名username：长度最大为20，不能重复（unique），不能为空（null）
2. 是否为会员is_member：布尔值，默认为False
3. 账户余额balance：浮点型，总位数为20，小数位为2，默认0.00
4. 会员编号member_id：整型
5. 邮箱email：使用EmailField()
6. 创建时间created_time：只在新增数据时会插入时间（auto_now_add=True)
7. 更新时间updated_time：增删改时自动更新时间（auto_now=True）











#### 404：检查路由和URL地址

#### ORM：对象关系映射

#### 命令

##### 1. django-admin startproject 项目名

##### 2. python3 manage.py runserver

##### 3. python3 manage.py startapp 应用名

##### 4. python3 manage.py makemigrations # 生成迁移文件

##### 5. python3 manage.py migrate # 同步到数据库





### 项目开发流程

* 需求文档（产品经理）

* UI原型图设计

* 数据库设计（**共计几张表、每张表有哪些字段、每个字段什么数据类型、表之间的关系，出ER图**）

* 开会：前端工程师、后端工程师、测试工程师、产品经理

* 开发文档（开发工程师完成）

* 前后端并行开发

* 前后端联调

* 测试阶段（测试工程师）

  冒烟测试、内测、公测、正式版本的候选版本

* 上线运行维护





1. 删除数据库mysite3db，并重新创建

   drop database mysite3db;

   create database mysite3db default charset utf8;

2. 删除所有的迁移文件 users/migrations/000xxxxx    

3. 重新迁移同步

   python3 manage.py makemigrations

   python3 manage.py migrate



##### insert into 表名 values(),(),....;

##### select * from 表名 where 条件;



class UserProfile(models.Model):

​	username = xxx

​	password = xxx



**UserProfile.objects.create(username="xxx", password="xxx", email="xxx")**

**UserProfile.objects.filter(username="zhaoliying", id=3)**











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





