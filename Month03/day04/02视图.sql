-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 创建视图 视图操作实际就是操作原表数据，
-- 但是只能操作视图范围内的部分，还需要复合原表约束
create view good_stu_view as 
select * from class where score >=80;

-- 查看数据库中所有表和类型
show full tables in stu;

-- 多表视图  基本上主要用于查询操作
create view dept_person_view as 
select name,dname,salary from person 
left join dept 
on dept.id = person.dept_id;

-- 修改视图
alter view good_stu_view as 
select * from class where score >=85;

-- 删除视图
drop view dept_person_view;