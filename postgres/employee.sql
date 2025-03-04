-----------------------------TASK DAY 1(sql)---------------------------------------
-- 1. creating an Employee and Department table and inserting values into it
create table Employee(
	e_id SERIAL primary key not null,
	e_name varchar(30) not null,
	dept_id varchar(30) not null,
	salary integer not null,
	active bool not null
);

create table Department(
	dept_id SERIAL primary key not null,
	dept_name varchar(30) not null
);

insert into Employee (e_name, dept_id, salary, active)
values
  ('john', 'IT', 2000, true),
  ('Sean', 'IT', 4000, true),
  ('Eric', 'Admin', 2000, true),
  ('Nancy', 'Admin', 2000, true),
  ('Lee', 'HR', 3000, true),
  ('Steven', 'Accounts', 2000, true),
  ('Matt', 'IT', 5000, true),
  ('Sarah', 'IT', 2000, false);
		
insert into Department (dept_name)
values 
	('IT'),
	('Admin'),
	('HR'),
	('Accounts'),
	('Health')
	
select * from employee e;
select * from department d ;

-- Getting the salary of 
select * from employee e
order by 
e.salary ASC

-- 3. select only the distinct salary from the employee table
select distinct salary from employee e

-- 4. write a code to find total number of active employees
select count(*) from employee e where active = true

--5. Update the department of nancy to HR
update employee e set dept_id = 'HR' where e_name = 'Nancy'

--6. a query to get the salary from employee table with highest and second highest salary
-- without using subquery
select distinct salary
from employee e order by salary desc 
limit 2 offset 1

--with using subquery creating separate column named highest and second highest salary
select
	(select max(salary) from employee e ) as highest_salary,
	(select max(salary) from employee e where salary < (select max(salary) from employee e)) as second_highest_salary

--7. query to get the department name of each employee
select * from employee e 
join department d 
on e.dept_id = d.dept_name

--8. query to get the department name with maximum employee count
select e.dept_id , count(e.e_id)
from employee e
group by e.dept_id
order by count(e.e_id) desc
limit 1

--9. query to get the department where no employee is assigned
select d.dept_name
from department d
left join employee e on d.dept_name = e.dept_id
where e.dept_id is null;

--10. query to get the list of employee and salary with the same salary
select e.e_name, e.salary
from employee e
join (
    select salary
    from employee
    group by salary
    having COUNT(e_id) > 1
) duplicate_salaries on e.salary = duplicate_salaries.salary;

-------------------------------TASK DAY 2 (SQL)-----------------------------------------
-- 1. find the total salary expenditure for each department
select d.dept_name , coalesce(sum(e.salary),0)
from employee e
right join department d
on d.dept_name = e.dept_id
group by d.dept_name

--2. Query to find the average salary of employees in each department
select d.dept_name , coalesce(avg(e.salary), 0)
from employee e
right join department d
on d.dept_name = e.dept_id
group by d.dept_name

--3. Query to get the list of employees who are in same department as john
select distinct e.e_name, d.dept_name 
from employee e
join department d
on e.dept_id = d.dept_name
where e.dept_id  = (select dept_id from employee where e_name = 'john')

--4. Query to get the list of employees who do not belong to the it department
select e.e_name, e.dept_id
from employee e
join department d
on e.dept_id = d.dept_name
where d.dept_name <> 'IT'

--5 Query to find the department with highest salary expenditure
select d.dept_name , sum(e.salary) as highest_salary_expenditure
from employee e
join department d
on d.dept_name = e.dept_id
group by d.dept_name
order by highest_salary_expenditure desc
limit 1

--6 Query to get the names of employees who have the same salary as the maximum salary in the 'HR' department
select e.e_name , max(e.salary) as max_salary
from employee e
join department d
on d.dept_name = e.dept_id
where d.dept_name = 'HR'
group by e.e_name
order by max_salary desc
limit 1

--7. Query to list all employees and their departments, displaying 'No Department' for employees without
select distinct e.e_name, 
       coalesce(d.dept_name, 'No Department') as department_name
from employee e
right join department d 
on e.dept_id = d.dept_name
order by e.e_name

--8. Query to find departments that have employees with salaries above the average salary of all employees
SELECT d.dept_name
FROM department d
JOIN employee e ON d.dept_name = e.dept_id
WHERE e.salary > (SELECT AVG(salary) FROM employee)
GROUP BY d.dept_name

--9. Query to find the departments that have more than one employee with the same salary.
SELECT e1.dept_id, e1.salary, COUNT(e1.e_id) AS employee_count
FROM employee e1
JOIN employee e2 
ON e1.dept_id = e2.dept_id 
AND e1.salary = e2.salary 
AND e1.e_id <> e2.e_id
GROUP BY e1.dept_id, e1.salary
HAVING COUNT(e1.e_id) > 1;

-----------------------------------------------------------------------------------------
---------------------------------------Task DAY 3----------------------------------------
-----------------------------------------------------------------------------------------

--1. query to find the employees who have the highest salary in their respective departments (USE INNER JOIN)
--using subquery
SELECT e.e_name, e.salary, e.dept_id
FROM employee e
INNER JOIN (
    SELECT dept_id, MAX(salary) AS max_salary
    FROM employee
    GROUP BY dept_id
) subquery ON e.dept_id = subquery.dept_id AND e.salary = subquery.max_salary;

-- using self-join
SELECT e1.e_name, e1.salary, e1.dept_id
FROM employee e1
INNER JOIN employee e2 
ON e1.dept_id = e2.dept_id
GROUP BY e1.e_name, e1.salary, e1.dept_id
HAVING e1.salary = MAX(e2.salary);

-- 2. Query to list all employees and their department names, but include employees who do not belong to any department additionally indicate the employees who are active or not
select distinct e.e_name, d.dept_name , e.active 
from employee e
left join department d
on e.dept_id = d.dept_name
order by d.dept_name

-- 3. Query to list all departments and the names of the employees who work on them. include department that do not have employees assigned
select distinct e.e_name, d.dept_name
from employee e 
right join department d
on d.dept_name = e.dept_id
order by e.e_name

-- 4. Query to list all employees and departments, including employees without departments and departments without employees. indicate if each record is an employee or department

SELECT DISTINCT
    e.e_name AS name, 
    d.dept_name AS department, 
    CASE 
        WHEN e.e_id IS NOT NULL THEN 'Employee' 
        WHEN d.dept_id IS NOT NULL THEN 'Department' 
    END AS record_type
FROM employee e
FULL OUTER JOIN department d ON e.dept_id = d.dept_name;

--5. a query to find the total salary expenditure and the average salary for each department including departments without employees

select d.dept_name,
	coalesce(avg(e.salary), 0) as average_salary,
	coalesce(sum(e.salary)/2, 0) as total_salary_expenditure
from department d
left join (
	select dept_id, salary
	from employee
) e
on d.dept_name = e.dept_id
group by d.dept_name

-- 6. query using CTE to list the employees who have a salary above the average salary of their department, include department names in the results

WITH avg_salary AS (
    SELECT e.dept_id, AVG(e.salary) AS average_salary
    FROM employee e
    GROUP BY e.dept_id
)
select distinct e.e_name, e.salary, d.dept_name
FROM employee e
JOIN avg_salary avg_dept_salary
ON e.dept_id = avg_dept_salary.dept_id
JOIN department d ON e.dept_id = d.dept_name
WHERE e.salary > avg_dept_salary.average_salary;

--7. query to find the names of employees who earn more than average salary of all employees in the company. Include their department names
with company_average_salary as (
	select avg(e.salary) as average_company_salary
	from employee e
)
select e.e_name, e.salary, d.dept_name
from employee e 
join department d
on d.dept_name = e.dept_id
where e.salary > (select average_company_salary from company_average_salary)

--8. write a query to list the names of employees who work in the same department as 'sean' but exclude 'sean' from the results using cte and inner join
with department_as_sean as (
	select distinct d.dept_name as department
	from employee e
	inner join department d
	on d.dept_name = e.dept_id
	where e.e_name = 'Sean'
)
select distinct e.e_name, d.dept_name
from employee e
join department d 
on e.dept_id = d.dept_name
where e.e_name != 'Sean' and e.dept_id in (select department from department_as_sean)

--9. A query to find the department names which have more than one employees earning above the average salary of their departments 
--use nested subqueries and groupby

select e.dept_id as department
from employee e
where e.salary > (
	select avg(e2.salary)
	from employee e2
	where e2.dept_id = e.dept_id
)
group by e.dept_id
having count(*) > 1

--10. query to find pairs of employees who work in the same department and have the same salary. list each pair only once
select e1.e_name as employee1, e2.e_name as employee2, e1.dept_id, e1.salary
from employee e1
join employee e2
on e1.dept_id = e2.dept_id
and e1.salary = e2.salary
and e1.e_id = e2.e_id













