-- Active: 1664259342598@@127.0.0.1@3306@stu

insert into class values 
(8,"Eva",17,'w',70.5);

insert into hobby values 
(1,"Joy","draw,sing","B",49800.58,"当代达芬奇"),
(2,"Emma","dance,sing","B",36800.58,"练舞奇才");

insert into hobby (name,hobby,level,price) 
values
("James","draw,dance","C",35000),
("Abby","dance","B",22000),
("Lucy","sing","B",25600);

insert into hobby (name,hobby,level,price) 
values
("Ben","draw","C",9980.45);


-- 基础查询

-- 查询一个表中所有数据
select * from class;

-- 选择字段
select name,score from class;

select * from class where age div 2 = 9;

-- 不支持连续的大于 小于的写法
select * from class where 70<score<80;

-- >=70  <=80
select * from class 
where score between 70 and 80;


-- 数据集合筛选
select * from class 
where name in ("Tom","Tonny","Timmy");

-- null判断必须使用is 不能用 = 
select * from class where sex is null;

select * from class 
where sex='m' and score>80;


-- 修改操作
update class set sex='m',score=91 
where name="Alex";

update class set score=60 
where id=5 or id=6;

update class set age=age+1;

-- 删除操作
delete from class where id=12;









