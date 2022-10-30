-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 增加一个新的字段
alter table hobby 
add phone char(10) after price;

-- 删除一个字段
alter table hobby drop level;


-- 修改数据类型
alter table hobby 
modify phone char(16);

-- 替换字段
alter table hobby 
change phone tel char(16);
