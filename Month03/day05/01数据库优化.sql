-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 查看引擎
show engines;

-- 更换引擎
alter table hobby engine=myisam;


-- explain工具
explain select * from class;
