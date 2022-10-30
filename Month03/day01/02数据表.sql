-- Active: 1664259342598@@127.0.0.1@3306@stu

use stu;

-- 创建基础数据表

CREATE TABLE
    student(
        name varchar(20),
        age tinyint,
        sex enum("男", "女"),
        height float
    );

-- 查看所有表

show tables;

-- 创建class表

CREATE TABLE
    `class`(
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(30) NOT NULL,
        `age` tinyint unsigned,
        `sex` enum("m", "w", "o"),
        `score` float DEFAULT 0
    );

CREATE TABLE
    `class` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(30) NOT NULL,
        `age` tinyint unsigned DEFAULT NULL,
        `sex` enum('m', 'w', 'o') DEFAULT NULL,
        `score` float DEFAULT '0',
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE
    `hobby`(
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(30) NOT NULL,
        `hobby` set("sing", "dance", "draw") NOT NULL,
        `level` char COMMENT "初始评级",
        `price` decimal(7, 2) CHECK(`price` > 8000),
        `remark` text
    );

-- 查看表字段信息

desc class;

-- 查看表信息

show create table class;

-- 删除数据表

drop table student;