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





网站前端：html、css、js、vue...    Web前端工程师

网站后端：Django... ...   后端开发工程师



#### http://127.0.0.1:8000/tmooc/xiaoze_video

#### http://127.0.0.1:8000/login



#### http://127.0.0.1:8000/v1/login?uname=liying&pwd=123456



#### path("v1/login", views.xxx_view),





1. 创建项目
2. cd到项目目录
3. 启动项目
4. pycharm中打开mysite1项目
5. urls.py，匹配路由
6. 新建views.py完成视图
7. 浏览器中输入地址测试





https://bj.lianjia.com/ershoufang/pg1/

https://bj.lianjia.com/ershoufang/pg2/

https://bj.lianjia.com/ershoufang/pg3/

... ...

https://bj.lianjia.com/ershoufang/pg100/





#### http://www.abc.com/zhaoliying/address

#### http://www.abc.com/dilireba/address

`path("<str:username>/address", views.xxx_view)`

<font color=red>使用path转换器</font>

<http://127.0.0.1:8000/>整数/操作字符串/整数

变量名：x    opeation    y

操作：add    sub   mul    div

浏览器：100/add/200   返回结果：300





登录功能

路由：v1/users/login

视图：login_view

任务：匹配路由，把视图结构写出来！



前端给后端传递数据的方式

* 方式1：路由传递

  `http://127.0.0.1:8000/<str:username>/<str:password>`

  后端接收：def xxx_view(request, username, password)

* 方式2：查询字符串

  `http://127.0.0.1:8000/v1/users/login?username=zhaoliying&password=123456`

  后端接收：request.GET







项目名：aidproject

1. 把原来的项目mysite1停止（Ctrl+C）

2. 创建新项目并启动新项目 aidproject

3. pycharm打开新的项目aidproject

4. MySQL中创建用户表user_tab并插入数据

   ```mysql
   mysql -uroot -p123456
   
   create database aiddb default charset utf8;
   use aiddb;
   create table user_tab(
   id int primary key auto_increment,
   username varchar(20),
   password char(32)
   );
   insert into user_tab(username,password) values("zhaoliying", "123456"),("reba","123456");
   ```

路由：v1/users/login

视图：login_view

实现方式：

* GET请求：用户名和密码以查询字符串方式传递
* POST请求：用户名和密码以表单形式传递



















https:  443

http:    80



## Python就业岗位

* Python开发工程师
* 人工智能工程师
* 数据分析工程师（**不好从事**）
* 爬虫工程师（**TTS赠送爬虫视频**）
* 自动化测试工程师（**补充相关测试内容**）
* 自动化运维工程师（**不好从事**）

































