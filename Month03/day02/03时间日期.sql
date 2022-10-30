-- Active: 1664259342598@@127.0.0.1@3306@stu

create table marathon (
id int primary key auto_increment,
athlete varchar(32),
birthday date,
r_time datetime comment "报名时间",
performance time
);

-- 数据书写
insert into marathon values 
(1,"尼古拉斯","1998-6-4","2022-9-25 19:38:22","2:38:56"),
(2,"托尼","2000-6-6","2022-9-26 15:8:22","2:25:6");

-- 时间类型比较大小
select * from marathon where birthday >= "2000-01-01";
select * from marathon where performance < "2:30:00";

-- 时间函数
select DATE("2022-9-15 19:10:10");

select DATEDIFF("2022-9-28 10:10:10","2019-11-20");

select now();

-- 字段默认时间填充当前时间
alter table marathon modify r_time datetime default now();

insert into marathon (athlete,birthday) values 
("曹操","1989-10-14");