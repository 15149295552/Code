-- Active: 1664259342598@@127.0.0.1@3306@exercise

-- 聚合练习： 基于books表
-- 1. 统计每位作家出版图书的平均价格
select author,avg(price) from books 
group by author;

-- 2. 统计每个出版社出版图书数量
select press,count(*) from books 
group by press;

-- 3. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price) 
from books group by publish_time;

-- 4. 筛选出那些出版过超过50元图书的出版社，
-- 并按照其出版图书的平均价格降序排序

select press,avg(price) from books  
group by press 
having max(price) > 50 
order by avg(price) desc;

select press,avg(price) from books 
where press in (select distinct press from books 
where price>50) 
group by press 
order by avg(price) desc;