-- Active: 1664259342598@@127.0.0.1@3306@stu
-- 创建表的同时创建索引
create table index_test(
    id int AUTO_INCREMENT,
    name varchar(30),
    primary key (id),
    unique (name)
);
-- 主键索引和唯一索引也可以作为字段约束
create table index_test(
    id int primary key AUTO_INCREMENT,
    name varchar(30) unique
);

-- 为已有的表增加索引
create index name on class(name);

-- 查看索引
desc class;
show create table class;

-- 删除索引
drop index name on index_test;