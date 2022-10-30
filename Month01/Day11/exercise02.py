"""
    创建员工管理器：
        1. 记录所有员工
        2. 计算总薪资
    岗位：
        1. 程序员:   底薪 + 项目分红
        2. 测试员：底薪 + Bug数 * 5
        ...
    要求：
        增加新员工,管理器代码不变.

分析:
    员工管理器类
        属性: list_employee
        方法: add_employee/calculate_salary

    员工类: staff
        属性: basic_salary
        方法: complate_salary

    程序员类
        属性: basic_salary/project_money
        方法: complate_salary

    测试员类
        属性: basic_salary/bug_number
        方法: complate_salary

    封装: 根据需求将问题分解为员工管理类/程序员类/测试员类
    继承: 抽象了一个父类员工类,隔离员工管理器计算薪资的方法与程序员对象/测试员对象的变化
    多态: 遍历对象,父类中计算薪资的方法,在程序员类/测试员类被重写,计算各自不同的薪资
"""


class EmployeeManager:
    def __init__(self):
        self.list_employee = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):  # 判断当前传入的对象是员工类中的一种 ('约束')
            self.list_employee.append(employee)

    def calculate_salary(self):
        total_salary = 0
        for employee in self.list_employee:
            total_salary += employee.complate_salary()
        return total_salary


class Employee:
    def __init__(self, basic_salary=0):
        self.basic_salary = basic_salary

    def complate_salary(self):
        pass


class Programmer(Employee):
    def __init__(self, basic_salary=0, money=0):
        super().__init__(basic_salary)
        self.project_money = money

    def complate_salary(self):
        return self.basic_salary + self.project_money


class Tester(Employee):
    def __init__(self, basic_salary=0, count=0):
        super().__init__(basic_salary)
        self.bug_count = count

    def complate_salary(self):
        return self.basic_salary + self.bug_count * 5


em = EmployeeManager()
p01 = Programmer(12000, 20000)
t01 = Tester(8000, 20)

em.add_employee(p01)
em.add_employee(t01)
print(em.calculate_salary())
