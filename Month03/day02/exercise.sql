-- Active: 1664259342598@@127.0.0.1@3306@exercise


-- 查询练习 使用books表

-- 1. 查找30多元的图书
select * from books 
where price >= 30 and price < 40;

-- ２．查找人民教育出版社出版的图书　
select * from books 
where press="人民教育出版社";

-- ３．查找老舍写的，中国文学出版社出版的图书　
select * from books 
where author="老舍" and press="中国文学出版社";

-- ４．查找备注不为空的图书
select * from books 
where comment is not null; 

-- ５．查找价格超过60元的图书，只看书名和价格
select bname,price from books 
where price > 60;

-- ６．查找鲁迅写的或者茅盾写的图书
select * from books 
where author="鲁迅" or author="茅盾";


select * from books 
where author in ("鲁迅","茅盾");


-- 练习 使用books表
-- 1. 将呐喊的价格修改为45元
update books set price=45 where bname="呐喊";

-- 2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table books add publish_time date after price;

-- 3. 修改所有老舍的作品出版时间为 2018-10-1
update books set publish_time="2018-10-1" 
where author="老舍";

-- 4. 修改所有中国文学出版社出版的但是不是老舍的作品出版时间为 2020-1-1
update books set publish_time="2020-1-1" 
where press="中国文学出版社" and author!="老舍";

-- 5. 修改所有出版时间为Null的图书出版时间
-- 为 2019-10-1
update books set publish_time="2019-10-1" where publish_time is null;

-- 6. 所有鲁迅的图书价格增加5元
update books set price=price+5 where author="鲁迅";

-- 7. 删除所有价格超过70元或者不到40元的图书
delete from books where price not between 40 and 70;


use stu;
-- 查找练习
-- 1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country="蜀" order by attack desc;

-- 2. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack=300 where country="吴" and attack>300 limit 2;

-- 3. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name as  姓名,attack as 攻击力 from sanguo where country="魏" and attack>200;


-- 4. 所有英雄按照攻击力降序排序，如果相同则按照防御升序排序
select * from sanguo order by attack desc,defense;

-- 5. 查找名字为3字的
select * from sanguo where name like "___";


-- 6. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country="魏" 
order by defense desc limit 2 offset 1;

-- 7. 查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender="女" and attack >180 
union 
select * from sanguo where gender="男" and attack < 250;


-- 8. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo where country="蜀" and attack > (select attack from sanguo where country="魏" order by attack desc limit 1);

