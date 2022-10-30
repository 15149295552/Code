-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 部门表 与 员工表是主从关系
CREATE TABLE dept (
    id int PRIMARY KEY auto_increment,
    dname VARCHAR(50) not null
);

insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');

CREATE TABLE person (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  age tinyint unsigned,
  salary decimal(8,2),
  dept_id int
) ;

insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);


insert into person values
(7,"Tonny",26,15000,8);


-- 增加外键 constraint外键名 foreign key外键字段 references 关联的主表主键
alter table person add  
constraint dept_fk 
foreign key (dept_id) 
references dept(id);

-- 查看外键
show create table person;

-- 删除外键
alter table person drop foreign key dept_fk;

-- 主表改，从表跟着改
alter table person add  
constraint dept_fk 
foreign key (dept_id) 
references dept(id) 
on delete cascade on update cascade;

-- 主表改，从变为null
alter table person add  
constraint dept_fk 
foreign key (dept_id) 
references dept(id) 
on delete set null on update set null;


-- 多对多关系
CREATE TABLE athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  country varchar(30) NOT NULL
);

CREATE TABLE sports (
  id int primary key AUTO_INCREMENT,
  sport varchar(30) NOT NULL
);

-- 关系表
CREATE TABLE athlete_sports (
   id int primary key auto_increment,
   aid int NOT NULL,
   sid int NOT NULL,
   FOREIGN KEY (aid) REFERENCES athlete (id),
   FOREIGN KEY (sid) REFERENCES sports (id)
);

-- 由关系衍生的数据适合放在关系表中
alter table athlete_sports add ranking int;