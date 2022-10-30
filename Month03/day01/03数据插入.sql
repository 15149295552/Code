-- Active: 1664259342598@@127.0.0.1@3306@stu

-- class表中插入数据

insert into class values (1,"Lily",18,"w",87), (2,"Tom",17,"m",79);

-- 选择字段插入

insert into
    class (name, age, score)
values ("Tonny", 17, 69), ("Alex", 19, 83);

insert into
    class (name, age, sex)
values ("Jame", 17, 'm'), ("Joy", 18, 'm'), ("Emma", 17, 'w');

insert into
    class (name, age, sex, score)
values ("Abby", 19, 'w', 90), ("Baron", 18, 'm', 76);
