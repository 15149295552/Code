-- Active: 1664259342598@@127.0.0.1@3306@stu

-- %任意长度字符 _一个字符
select * from class where name like "T%";
select * from class where name like "___";

-- 集合类型筛选
select * from hobby 
where hobby like "%draw%";


-- 起别名 简化书写 意思表达更明确
select name as 姓名,score as 分数 
from class as 班级;

select name  姓名,score  分数 
from class  班级;

-- 排序
select * from class where sex='w' 
order by score desc;

-- 复合排序
select * from class 
order by age desc,score desc;


-- 限制操作数量
select * from class limit 2;

update class set score=65 
where score=60 limit 1;

-- 分页
select * from class 
limit 2 offset 4;

select * from class 
order by score desc limit 3;

-- 跳过两条记录取一个
select * from class 
order by score desc limit 1 offset 2;

select * from class 
order by score desc limit 2,1;

-- 联合查询
select * from class where sex='m' 
union all 
select * from class where score>80;

-- 所有查询语句字段数量一样即可
select name,sex,score from class where sex='m' 
union  
select name,age,score from class where score>80;


-- 子查询
-- 子查询语句作为一个表放在另外一个查询语句的from后面
select * from (select * from class where sex='w') as wm  
where score>80;

-- 子查询作为值出现
select * from class where score>(select score from class where name="Tom" );

select * from class where name in (select name from hobby);







