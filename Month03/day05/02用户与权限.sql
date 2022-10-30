-- Active: 1664259342598@@127.0.0.1@3306@stu

-- 创建用户 % 表示允许用户在任意地址的计算机中通过网路连接数据库
create user "aid"@"%" identified by "123";

drop user "aid"@"%";


-- 给用户增加权限，注意使用root执行
grant select,update on stu.class to "aid"@"%" with grant option;


-- 删除权限 注意，添加权限时库.表的写法需要与删除时一致
revoke update on stu.class from "aid"@"%";