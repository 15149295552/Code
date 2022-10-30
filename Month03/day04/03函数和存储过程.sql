
-- 创建函数设置
set global log_bin_trust_function_creators=1;


-- 修改语句结尾符号
delimiter  $$


-- 定义一个简单的函数
-- 1.函数中够可以写增删改语句但是很少，这种情况更应该使用个存储过程完成
-- 2.函数中如果查询内容，必须将查询结果赋值给变量，函数执行过程不会进行任何数据打印

delimiter  $$

create function func01() returns float 
begin
    declare s float;
    set s =(select score from class where id=1);
    return s;
end $$

delimiter  ;


-- 带有形参的函数
delimiter  $$

create function func02(a int) returns float 
begin
    declare sc float; -- 定义局部变量
    -- set sc = (select score from class where id = a);
    select score from class where id = a into sc;
    return sc;
end $$

delimiter  ; 


-- 创建一个简单的存储过程
delimiter  $$

create procedure proc01()
begin
    update class set score=77 where id=1;
    delete from hobby where price < 9500;
    delete from class where sex is null;
    select * from class order by score desc;
end $$

delimiter  ;

-- 调用存储过程
call proc01();


-- 全局变量 更多用于数据库用户和系统的配置
set global log_bin=1;

-- 用户变量 放在函数外 类似Python中的全局变量
set @num=1;


-- 存储过程形参：
delimiter $$
create procedure proc_out(OUT a int)
begin
    select a;
    set a = 10000;
    select a;
end$$ 

delimiter  ;

set @n = 1;
call proc(@n);

-- 查看一个数据库下所有的函数/存储过程
show procedure status  where db="stu";
show function status  where db="stu";

-- 删除函数/ 存储过程
drop procedure proc;