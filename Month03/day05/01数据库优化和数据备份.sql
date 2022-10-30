-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 查看引擎
show engines;

-- 更换引擎
alter table hobby engine=myisam;


-- explain工具
explain select * from class;


-- 表数据复制
create table student1 select * from class where score>=80;

-- 不是sql语句 在终端命令行执行
mysqldump -u root -p stu > stu.sql

-- 恢复数据库 先创建出数据库，再导入数据库文件内容
mysql -u root -p student < stu.sql