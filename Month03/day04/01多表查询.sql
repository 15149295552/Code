-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 简单多表查询
-- 如果两张表没有外键关系，则需要我们找到两个表的关联性
select c.name,c.score,h.hobby,h.price 
from class as c,hobby as h 
where c.name = h.name;

-- 如果两张表有外键关系，那么多表查询时表关系表达就是主表主键=从表外键
select name,salary,dname from dept,person 
where dept.id=person.dept_id;


-- 问题1： where 进行表关系表达和条件筛选
-- 问题2： 有可能在某些要求下丢失数据
select name,salary,dname from dept,person 
where dept.id=person.dept_id and salary>18000;

-- 内连接查询
select name,salary,dname 
from dept inner join person 
on dept.id=person.dept_id
where salary>18000;

-- 左连接
select name,salary,dname 
from person left join dept 
on dept.id=person.dept_id 
where salary>18000;

-- 右连接 统计出每个部门人数

select dname,count(name) from person right join dept 
on person.dept_id = dept.id 
group by dname;
