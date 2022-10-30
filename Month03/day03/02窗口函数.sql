-- Active: 1664259342598@@127.0.0.1@3306@stu

-- partition by 用于分组  order by在分组后进行排序 row_number()函数表达具体功能

select
    name,
    country,
    attack,
    row_number() over (
        partition by country
        order by
            attack desc
    ) as a
from sanguo;

-- 给窗口命名可以便于重复使用
select
    name,
    country,
    attack,
    row_number() over ca as a,
    rank() over ca as b,
    dense_rank() over ca as c
from
    sanguo 
    window ca as (
        partition by country
        order by attack desc
    );