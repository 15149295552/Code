-- Active: 1664259342598@@127.0.0.1@3306@exercise

-- books表，使用存储过程完成，将2020年以
-- 前出版的图书价格增加3元，参数传入一个作家
-- 的名字，将该作家的图书，在此基础上再涨2元，
-- 按照图书价格打印出图书信息，只要书名，
-- 作者和价格即可

delimiter  $$ 

create procedure change_price(IN aname varchar(30))
begin
    update books set price=price+3 where publish_time < "2020-1-1";
    update books set price=price+2 where author=aname;
    select bname,author,price from books order by price;
end $$

delimiter  ;