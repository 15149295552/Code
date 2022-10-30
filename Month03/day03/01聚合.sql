-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 配合聚合函数使用，如果写普通字段要求该字段的值统一
-- 可以同时使用更多个聚合函数，聚合函数可以起名字
select country,avg(attack) as 平均攻击力,
max(attack) as 最大攻击力 
from sanguo 
where country="蜀";


-- count 统计不会统计 null值
select count(*) from sanguo 
where attack>200;

-- 分组
-- 按照什么字段分组，select 后就查询什么字段
select country from sanguo 
group by country;

-- 配合聚合函数使用
select country,avg(attack) from sanguo 
group by country;

-- 多字段分组
select country,gender,max(attack) from sanguo 
group by country,gender;


-- HAVING利用聚合函数对组进行筛选
select country,count(*) from sanguo 
group by country 
having count(*) > 4;

-- 男性英雄平均攻击力超过250的国家，按照其平均攻击力降序排序
select country,avg(attack) from sanguo 
where gender="男" 
group by country 
having avg(attack) > 250 
order by avg(attack) desc;

-- 对查询结果去除重复的内容
select distinct country from sanguo;
select count( distinct country) from sanguo;