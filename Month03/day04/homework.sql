-- Active: 1664259342598@@127.0.0.1@3306@exercise

-- 表关系设计练习：
-- 根据所学 用户朋友圈表内容表，使其合理，假设现有如下内容需要存储：
-- 姓名 密码 电话  图片 内容  地点 时间 点赞  评论

-- 哪个用户发了什么朋友圈，被谁点赞评论了

-- 用户表
CREATE TABLE user (
    uid int PRIMARY KEY AUTO_INCREMENT,
    user char(32) not null,
    password char(32) not null,
    tel char(16)
);

-- 朋友圈
CREATE TABLE friends (
    fid int PRIMARY KEY AUTO_INCREMENT,
    image varchar(50),
    content VARCHAR(1024),
    site VARCHAR(50),
    time DATETIME,
    user_id int,
    Foreign Key (user_id) REFERENCES user(uid)
);

-- 点赞评论表
CREATE TABLE `mylike`(
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `like` bit default 0,
    `comment` text,
    `user_id` int,
    `friends_id` int,
    Foreign Key (user_id) REFERENCES user(uid),
    Foreign Key (friends_id) REFERENCES friends(fid)
);


-- 表关系设计练习：
-- 将book表拆分为三张表（图书   作家    出版社）,自行设计表之间的关系，通过E-R图分析表关系和属性，然后写出创建语句

create table press(
    pid int PRIMARY KEY AUTO_INCREMENT,
    pname varchar(50),
    tel char(16),
    site varchar(128)
);

create table author(
    aid int PRIMARY KEY AUTO_INCREMENT,
    aname varchar(50),
    age tinyint,
    remark text
);

create Table book(
    bid int PRIMARY KEY AUTO_INCREMENT,
    bname VARCHAR(30),
    price float,
    press_id int,
    author_id int,
    foreign key(press_id) references press(pid),
    foreign key(author_id) references author(aid)
);

create Table author_press(
    id int PRIMARY KEY AUTO_INCREMENT,
    press_id int,
    author_id int,
    foreign key(press_id) references press(pid),
    foreign key(author_id) references author(aid)
);