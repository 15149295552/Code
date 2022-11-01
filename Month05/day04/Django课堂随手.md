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

# DJANGO-DAY03

## 一、DJANGO配置MySQL

* 创建数据库

  `create database 库名 default charset utf8;`

* 配置数据库（<font color=red>**settings.py**</font>）

  <font color=red>**指定数据库引擎、主机地址、用户名、密码、端口号、具体库**</font>

  示例

  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.mysql",
          "HOST": "MySQL数据库服务器的IP地址",
          "USER": "用户名",
          "PASSWORD": "密码",
          "NAME": "库名",
          "PORT": "3306",
      }
  }
  ```

  * 常见的数据库引擎

    ```python
    django.db.backends.mysql
    django.db.backends.sqlite3
    django.db.backends.oracle
    ... ...
    ```

## 二、ORM框架

### 1）定义

​	ORM，对象关系映射，避免使用SQL操作数据库，而是使用类和对象对数据库进行操作。

## 2）ORM特点

#### 2.1 优点

* 只需要面向对象编程，无须面向数据库编程。
* 实现数据模型和数据库的解耦，不用关心公司使用的数据库（**MySQL、Oracle等**）的细节，通过简单的配置就能实现更换项目数据库，无须修改大量代码。

#### 2.2 缺点

* 需要将对应的操作语句转为SQL命令再执行，映射的过程中会有一定程度的性能丢失。
* 对于复杂的业务使用成本较高。

### 3）ORM对应关系

|    ORM     |   数据库   |
| :--------: | :--------: |
|   一个类   |   一张表   |
| 一个类属性 | 一个表字段 |
|  一个对象  | 一条表记录 |

得到对象：

1. user = UserProfile.objects.create(username="xxx", ........)

2. user_query = UserProfile.objects.filter(username="xxx")

   user = user_query[0]

### 4）ORM使用流程

1. 创建库

2. 配置数据库

3. 创建应用

   `python3 manage.py startapp 应用名`

4. 创建模型类

   ```python
   from django.db import models
   
   class Xxx(models.Model):
       username = models.CharField(...)
   ```

5. 迁移同步

   python3 manage.py makemigrations

   python3 manage.py migrate

### 5）迁移文件混乱的处理方法

1. 删除库：`drop database 库名;`

2. 建库：`create database 库名 default charset utf8;`

3. 删除迁移文件：`删除所有应用下的migrations中的 000_xxx... 的文件`

4. 迁移同步

   `python3 manage.py makemigrations`

   `python3 manage.py migrate`

### 6）字段类型

* 类型

  |    models.py    |     mysql数据库     |    示例     |
  | :-------------: | :-----------------: | :---------: |
  | BooleanField()  |     tinyint(1)      | 是否会员... |
  |   CharField()   |     varchar(20)     |             |
  | DateTimeField() | datetime、timestamp | 注册时间... |
  | DecimalField()  |    decimal(M,D)     |   单价...   |
  |  EmailField()   |      varchar()      |    邮箱     |
  | IntegerField()  |         int         |   销量...   |

* 字段类型需要注意

  1. 字符类型必须指定宽度：**CharField(max_length=宽度)**

  2. 浮点型必须指定总位数和小数位位数：**DecimalField(max_digits=10, decimal_places=2)**

  3. 日期时间类型设置自动创建或者更新时间：

     **auto_now_add=True: 插入数据时自动创建时间**

     **auto_now=True: 增删改时会自动更新时间**

  4. 存储邮箱：**EmailField()**

* 字段选项注意

  1. 主键：primary_key

     <font color=red>模型类未指定主键，则Django会自动创建id字段并设置为主键；如果模型类指定主键，则Django不会创建id字段。</font>

  2. 索引：db_index

     <font color=red>在经常用来查询的字段上建立索引，也是数据库优化的一种方式。</font>

  3. 唯一：unique

     <font color=red>字段的值不允许重复。</font>

### 7）内部类Meta

​	使用Meta内部类，可以对模型类赋予属性，比如指定表名、指定admin后台数据格式显示等等。



# DJANGO-DAY04

## 一、ORM增删改查

<font color=blue>**统统使用管理器对象objects，每个继承models.Model的模型类都会同样继承objects。**</font>

### 1）增-create

* 方法：`模型类.objects.create(属性=值,属性=值, ...)`

### 2）查-filter

* 方法：`模型类.objects.filter(条件1,条件2,...)`





#### 登录功能

* 请求路由：**http://127.0.0.1:8000/v1/users/login**
* 请求方法：
  * GET请求：获取登录页面
  * POST请求：请求登录
* 请求体数据
  * 用户名
  * 密码
* 返回响应
  * 登录成功
  * 用户名或密码错误





1. **编写models.py**

2. **终端迁移同步**

3. **shell中插入数据**

   ```python
   from django.db import models
   
   
   class Book(models.Model):
       title = models.CharField("书名", max_length=20, null=False, unique=True)
       pub = models.CharField("出版社", max_length=50, null=False)
       price = models.DecimalField("价格", max_digits=6, decimal_places=2)
       market_price = models.DecimalField("零售价", max_digits=6, decimal_places=2)
   
   
   class Author(models.Model):
       name = models.CharField("姓名", max_length=20, null=False)
       age = models.IntegerField("年龄", null=False, default=1)
       email = models.EmailField("邮箱", null=True)
   
   ```

   

   ```python
   Book.objects.create(title="Python", price=20.00, market_price=25.00, pub="清华大学出版社")
   Book.objects.create(title="Django", price=70.00, market_price=75.00, pub="清华大学出版社")
   Book.objects.create(title="JQuery", price=90.00, market_price=85.00, pub="机械工业出版社")
   Book.objects.create(title="Linux", price=80.00, market_price=65.00, pub="机械出版社")
   Book.objects.create(title="HTML5", price=90.00, market_price=105.00, pub="清华大学出版社")
   
   Author.objects.create(name="王老师", age=28, email="wangweichao@tedu.cn")
   Author.objects.create(name="吕老师", age=31, email="lvze@tedu.cn")
   Author.objects.create(name="祁老师", age=30, email="qitx@tedu.cn")
   ```

   

- 练习:

  1. 查询Book表中price大于等于50的信息

     `books = Book.objects.filter(price__gte=50)`

  2. 查询Author表中姓王的人的信息

     `authors = Author.objects.filter(name__startswith="王")`

  3. 查询Author表中Email中包含"w "的人的信息

     `authors = Author.objects.filter(email__contains="w")`

  4. 将Book表中的数据按照零售价格(market_price)降价排序

     `books = Book.objects.order_by("-market_price")`

  5. 查询用户表UserProfile中的所有数据

     `users = UserProfile.objects.all()`

  6. 查询用户表中id为5，并且用户名为zhaoliying的数据

     `user = UserProfile.objects.get(id=5,username="zhaoliying")`

  7. 查询Book表中价格>=30，并且是清华大学出版社出版的图书

     `books = Book.objects.filter(price__gte=30,pub="清华大学出版社")`

  8. 查询author表中，年龄<30的数据

     `authors = Author.objects.filter(age__lt=30)`

  9. 将Author表中吕老师的邮箱调整为：309435365@qq.com

     `author = Author.objects.get(name="吕老师")`

     `author.email = "309435365@qq.com"`

     `author.save()`

  10. 将Book表中HTML5这本书的出版社改为：人民教育出版社

      `book = Book.objects.get(title="HTML5")`

      `book.pub = "人民教育出版社"`

      `book.save()`

<font color=red>**一查二改三保存**</font>

##### select * from bookstore_book;

##### select * from bookstore_author;

###### 

#### 修改密码

* 路由：http://127.0.0.1:8000/v1/users/update_password

* 请求方法

  GET请求：获取页面

  POST请求：更新密码

* 请求体数据

  用户名、密码、新密码

* 响应

  更新成功、更新失败



#### 注销用户

* 路由：http://127.0.0.1:8000/v1/users/delete_user?username=dilireba&password=123456

* 请求方法：GET

* 查询字符串

  用户名username、密码password

* 响应

  注销成功 | 失败



```mysql
select avg(price) from bookstore_book;

select pub, avg(price) from bookstore_book group by pub;
```



```mysql
Book表中，所有书的零售价market_price统一上调10元！

update bookstore_book set market_price=market_price+10;

想找出定价低于20元 或 清华大学出版社的全部书
Book.objects.filter(price__lt=20)
Book.objects.filter(pub="清华大学出版社")

Book.objects.filter(Q(price__lt=20) | Q(pub="清华大学出版社"))
```

```mysql
查找不是机械工业出版社的书 且 价格低于50的书
Book.objects.filter(~Q(pub="机械工业出版社") & Q(price__lt=50))
```



#### select * from bookstore_book where id=%s

#### 正常用户：select * from bookstore_book where id=666

#### 黑客：select * from bookstore_book where id=1 or 1



**模型类.objects.raw('sql', ['1 or 1'])**









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













**终端1：启动项目 python3 manage.py runserver**

**终端2：进入数据库 mysql  -uroot -p123456          use  mysite3db;**

**终端3：常规打开**

**pycharm单独打开mysite3项目**

**打开Firefox火狐浏览器**

**打开django笔记**











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





