-- 创建一个数据库  exercise
create database exercise;
use exercise;

-- 创建一个数据表  books  类型和约束自己设计 ，
-- 字段 ： id  书名   作者   出版社  价格   备注
create table `books` (
    `id` int primary key AUTO_INCREMENT,
    `bname` varchar(30) not null,
    `author` varchar(30) default "佚名",
    `press` varchar(128),
    `price` decimal(5,2),
    `comment` text
);


-- 向其中插入数据若干  >= 6条
-- 参考 ： 老舍  沈从文  鲁迅  冰心  ....
-- 出版社 ： 中国文学  人民教育   机械工业
-- 价格 ：  30-120

insert into books
(bname,author,press,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into books
(bname,author,press,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("子夜","茅盾","人民教育出版社",47);









