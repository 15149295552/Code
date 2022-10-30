-- Active: 1664259342598@@127.0.0.1@3306@exercise

create table
    class(
        cid int primary key auto_increment,
        caption char(4) not null
    );

create table
    teacher(
        tid int primary key auto_increment,
        tname varchar(32) not null
    );

create table
    student(
        sid int primary key auto_increment,
        sname varchar(32) not null,
        gender enum('male', 'female', 'others') not null default 'male',
        class_id int,
        foreign key(class_id) references class(cid) on update cascade on delete cascade
    );

create table
    course(
        cid int primary key auto_increment,
        cname varchar(16) not null,
        teacher_id int,
        foreign key(teacher_id) references teacher(tid) on update cascade on delete cascade
    );

create table
    score(
        sid int primary key auto_increment,
        student_id int,
        course_id int,
        number int(3) not null,
        foreign key(student_id) references student(sid) on update cascade on delete cascade,
        foreign key(course_id) references course(cid) on update cascade on delete cascade
    );

insert into class(caption) values ('三年一班'), ('三年二班'), ('三年三班');

insert into teacher (tname) values('魏老师'),('祁老师'),('小泽老师');

insert into
    student(sname, gender, class_id)
values ('钢蛋', 'female', 1), ('铁锤', 'female', 1), ('山炮', 'male', 2), ('彪哥', 'male', 3), ('虎子', 'male', 3), ('妞妞', 'female', 2), ('建国', 'male', 2);

insert into
    course(cname, teacher_id)
values ('生物', 1), ('体育', 1), ('物理', 2);

insert into
    score(student_id, course_id, number)
values (1, 1, 60), (1, 2, 59), (2, 2, 100), (3, 2, 78), (4, 3, 66), (2, 3, 78), (5, 2, 77), (6, 1, 84), (7, 1, 79), (5, 3, 80), (3, 1, 59);

-- 1. 查询每位老师教授的课程数量
select tname,count(cname) 
from teacher left join course 
on teacher.tid = course.teacher_id 
group by tname;

-- 2. 查询各科成绩最高和最低的分数,形式 : 课程ID  课程名称 最高分  最低分
select cid,cname,max(number),min(number)  
from course left join score 
on course.cid = score.course_id 
group by cid;


-- 3. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,sname,avg(number) 
from student left join score 
on student.sid = score.student_id 
group by student.sid 
having avg(number) > 85;


-- 4. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid,sname   
from student left join score 
on student.sid = score.student_id 
where course_id = 2 and number>80;


-- 5. 查询各个课程及相应的选修人数
select  cname,count(*) 
from course inner join score 
on course.cid = score.course_id  
group  by cname;


-- 6. 查询每位学生的姓名，所在班级和各科平均成绩
select sname,caption,avg(number)  
from student inner join class 
on student.class_id = class.cid 
inner join score 
on student.sid = score.student_id 
group by sname,caption;


-- 函数练习：
-- 使用books表，请编写一个函数，参数传入2本书的名字
-- 返回两本书的价格之差

create function price_mul(b1 varchar(30),b2 varchar(30)) returns float 
begin
    declare p1,p2 float;
    set p1 = (select price from books where bname=b1);
    set p2 = (select price from books where bname=b2);
    return p1-p2;
end $$