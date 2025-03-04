--------------------------------------------------------------------------------------------------------
------------------------------------------TASK DAY 4----------------------------------------------------
--------------------------------------------------------------------------------------------------------

create table salesman (
	salesman_id int primary key,
	name varchar(20) not null,
	city varchar(20),
	comission float 
)

create table customer (
	customer_id int primary key,
	customer_name varchar(20) not null,
	city varchar(20),
	grade int,
	salesman_id int
)

create table orders (
	order_no int primary key,
	purchase_amt float,
	order_date date,
	customer_id int not null,
	salesman_id int 
)

insert into salesman(salesman_id, name, city, comission)
values
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen',null,0.12),
(5007, 'Paul Adam', 'Rome', 0.13)

insert into customer(customer_id, customer_name, city, grade, salesman_id)
values
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Eusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', null, null),
(3004, 'Fabien Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, null),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200,5007)

insert into orders(order_no, purchase_amt, order_date, customer_id , salesman_id)
values 
(70001, 150.5,'2016-10-05', 3005, 5002)
(70009, 270.65, '2016-09-10', 3001, null),
(70002, 65.26, '2016-10-05', 3002, 5001),
(70004, 110.5, '2016-08-17', 3009, null),
(70007, 948.5, '2016-09-10', 3005, 5002),
(70005, 2400.6, '2016-07-27', 3007, 5001),
(70008, 5760, '2016-09-10', 3002, 5001),
(70010, 1983.43, '2016-10-10', 3004, 5006),
(70003, 2480.4, '2016-10-10', 3009, null),
(70012, 250.45, '2016-06-27', 3008, 5002),
(70011, 75.29, '2016-08-17', 3003, 5007);


--1. find the name and city of those customers who live in the same city
select c1.customer_name, c1.city
from customer c1
join customer c2
on c1.city = c2.city
and c1.customer_id <> c2.customer_id
order by c1.city, c1.customer_name

--2. find the nemes of all customer along with the salesman who works for them
select c.customer_name, s.name
from customer c
left join salesman s
on c.salesman_id = s.salesman_id
order by c.customer_name

--3. display all those orders by the customers not located in the same cities where their salesman live 
select o.order_no, o.purchase_amt,o.order_date,c.customer_name, c.city as customer_city, s.name as salesman_name, s.city as salesman_city
from orders o
join customer c 
on o.customer_id = c.customer_id 
join salesman s 
on o.salesman_id = s.salesman_id 
where c.city <> s.city
or s.city is null
order by o.order_no

--4. Display all the orders issued by the salesman 'Paul Adam' from the orders table
select o.order_no, o.purchase_amt, o.order_date, s.salesman_id, s.name
from orders o
left join salesman s
on o.salesman_id = s.salesman_id
where s.name = 'Paul Adam'

--5. Display all the orders which values are greater than the average order value for 10th october 2016
select order_no, purchase_amt, order_date
from orders  
where purchase_amt > (
	select avg(purchase_amt)
	from orders
	where order_date = '2016-10-10'
)

--6. find all the orders attributed to salesman in paris
select o.order_no, o.order_no, o.order_date, s."name", s.city
from orders o
join salesman s
on o.salesman_id = s.salesman_id
where s.city = 'Paris'

--7. extract the data from the orders table for the salesman who earned the maximum commission
select s.salesman_id , s.name, max(s.comission) as maximum_commission
from salesman s
join orders o
on s.salesman_id = o.salesman_id
group by s.salesman_id

-----------------------------------------------------------------------------------------------------------------------
--------------------------------------------------- Task Day 5 --------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------

-- insert into salesman(salesman_id, name, city, comission)
-- insert into customer(customer_id, customer_name, city, grade, salesman_id)
-- insert into orders(order_no, purchase_amt, order_date, customer_id , salesman_id)

-- 1. Rank salesmen based on their total sales amount in descending order. Include salesman_id, name , total sales, and rank
select s.salesman_id, s."name", 
	sum(o.purchase_amt) as total_sales,
	rank() over (order by sum(o.purchase_amt) desc) as rank
from salesman s
join orders o 
on o.salesman_id = s.salesman_id
group by s.salesman_id

-- 2. Find the customer with the highest purchase amount and their rank within their respective city.
select c.customer_id, c.customer_name, c.city, o.purchase_amt,
	rank() over (partition by c.city order by o.purchase_amt desc) as "rank"
from customer c
join orders o
on o.customer_id = c.customer_id

-- 3. create a view that lists the total purchase amount per customer along with customer details.
create view total_purchase_customer as 
select c.customer_id, c.customer_name, c.city , sum(o.purchase_amt) as total_purchase_amount
from customer c
join orders
on o.customer_id = c.customer_id
group by c.customer_id;

select * from total_purchase_customer;

-- 4. create a view to show each salesman's customers and their total purchase amounts.
create view salesman_with_customer as
select c.customer_id, c.customer_name, s.salesman_id,s."name" as salesman_name , sum(o.purchase_amt) as total_purchase_amt
from customer c
join salesman s
on s.salesman_id = c.salesman_id
join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name, s.salesman_id, s."name";
order by total_purchase_amt desc

select * from salesman_with_customer;
drop view salesman_with_customer;

-- 5. write a stored procedure to insert a new customer into the customer table.
create or replace procedure insert_new_customer(
	p_customer_id int,
	p_customer_name varchar(20),
	p_city varchar(20),
	p_grade int,
	p_salesman_id int
) 
language plpgsql
as $$
begin
	insert into customer(customer_id, customer_name, city, grade, salesman_id)
	values (p_customer_id, p_customer_name, p_city, p_grade, p_salesman_id);
end $$;

call insert_new_customer(3011, 'Jane Doe', 'New York', 350, 5003);

select * from customer;

-- 6. write a stored procedure to get all orders of a given customer by their customr_id.

-- 7. find the top 3 customers by purchase amount in each city.
SELECT customer_id, customer_name, city, total_amount
FROM (
    SELECT c.customer_id, c.customer_name, c.city, 
           SUM(o.purchase_amt) AS total_amount,
           RANK() OVER (PARTITION BY c.city ORDER BY SUM(o.purchase_amt) DESC) AS rnk
    FROM customer c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name, c.city
) ranked_customers
WHERE rnk <= 3;

-- 8. calculate the average purchase amount per city and list customers who exceed this average.
select ct.customer_id, ct.customer_name, ct.city, ct.total_amount, ca.avg_amount
from (
    -- calculate total purchase amount per customer
    select c.customer_id, c.customer_name, c.city, sum(o.purchase_amt) as total_amount
    from customer c
    join orders o on c.customer_id = o.customer_id
    group by c.customer_id, c.customer_name, c.city
) ct
join (
    -- calculate average purchase amount per city
    select city, avg(total_city_amount) as avg_amount
    from (
        select c.city, sum(o.purchase_amt) as total_city_amount
        from customer c
        join orders o on c.customer_id = o.customer_id
        group by c.city, c.customer_id
    ) city_totals
    group by city
) ca 
on ct.city = ca.city
where ct.total_amount > ca.avg_amount;


-- 9. find all salesmen who have more than one customers.
select distinct salesman_id, name
from (
    select s.salesman_id, s.name, count(c.customer_id) over (partition by s.salesman_id) as customer_count
    from salesman s
    left join customer c on s.salesman_id = c.salesman_id
) sales_data
where customer_count > 1;

-- 10. Find the customers who have placed orders worth more than average order amount.
select c.customer_id, c.customer_name, sum(o.purchase_amt) as total_purchase
from customer c
join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having sum(o.purchase_amt) > (select avg(purchase_amt) from orders);

-- 11. Rank salesman by their total commission earned from orders, including the commission percentage from salesman table.
SELECT 
    s.salesman_id, 
    s.name, 
    SUM(o.purchase_amt * s.comission) AS total_commission,
    RANK() OVER (ORDER BY SUM(o.purchase_amt * s.comission) DESC) AS rank
FROM salesman s
JOIN orders o 
    ON s.salesman_id = o.salesman_id
GROUP BY s.salesman_id, s.name;

-- 12. create a view that lists each city's total sales and number of salesmen operating in that city.
CREATE VIEW city_sales_summary AS
SELECT 
    s.city,
    SUM(o.purchase_amt) AS total_sales,
    COUNT(DISTINCT s.salesman_id) AS number_of_salesmen
FROM salesman s
JOIN orders o 
    ON s.salesman_id = o.salesman_id
GROUP BY s.city;

SELECT * FROM city_sales_summary;

-- 13. write a stored procedure to update a customer's grade based on their total purchase amount. For example, if the total purchases exceed 1000, update the grade to 300.
CREATE OR REPLACE PROCEDURE UpdateCustomerGrade()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE customer
    SET grade = 300
    WHERE customer_id IN (
        SELECT customer_id 
        FROM orders 
        GROUP BY customer_id 
        HAVING SUM(purchase_amt) > 1000
    );
END $$;


CALL UpdateCustomerGrade();

-- 14. Use a recursive CTE to list all salesman and their total sales, including sales from customers managed by salesman they supervise
WITH RECURSIVE SalesHierarchy AS (
    -- Base case: Select all salesmen and their direct sales
    SELECT s.salesman_id, s.name, SUM(sa.saleAmount) AS total_sales
    FROM salesman s
    LEFT JOIN sales sa
    ON s.salesman_id = sa.salesPerson
    GROUP BY s.salesman_id, s.name

    UNION ALL

    -- Recursive case: Select salesmen under the supervision of another salesman and add their sales
    SELECT s.salesman_id, s.name, SUM(sa.saleAmount) + sh.total_sales AS total_sales
    FROM salesman s
    JOIN SalesHierarchy sh
    ON s.supervisor_id = sh.salesman_id  -- assuming the field is `supervisor_id`
    LEFT JOIN sales sa
    ON s.salesman_id = sa.salesPerson
    GROUP BY s.salesman_id, s.name, sh.total_sales
)

-- Select the final result
SELECT salesman_id, name, total_sales
FROM SalesHierarchy
ORDER BY total_sales DESC;



-- 15. Write a subquery to find the salesman with the highest numbers of orders and display their details. 

SELECT s.salesman_id, s.name, COUNT(o.order_no) AS order_count
FROM salesman s
JOIN orders o ON s.salesman_id = o.salesman_id
GROUP BY s.salesman_id, s.name
HAVING COUNT(o.order_no) = (
    SELECT MAX(order_count)
    FROM (
        SELECT COUNT(order_no) AS order_count
        FROM orders
        GROUP BY salesman_id
    ) AS subquery
)



-----------------------------------------------------------------------------------------------------------------------
--------------------------------------------------- Task Day 6 --------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------

create table sales(
	saleID SERIAL primary key not null,
	salesPerson varchar(20) not null,
	saleDate date, 
	saleAmount float 
)

insert into sales(salesPerson, saleDate, saleAmount)
values 
('Alice', '2023-01-01', 300),
('Bob', '2023-01-02', 450),
('Alice', '2023-01-03', 650),
('Charlie','2023-01-04', 900),
('Bob', '2023-01-05', 1200),
('Alice', '2023-05-06', 1300),
('Charlie', '2023-05-07', 1650),
('Alice', '2023-01-08', 2100),
('Bob', '2023-01-09', 2300),
('Charlie', '2023-01-10', 2700),
('Alice', '2023-01-11', 2850),
('Bob', '2023-01-12', 3100),
('Charlie','2023-01-13', 3400),
('Alice', '2023-01-14', 3750),
('Bob', '2023-01-15', 3850)

-- 1. calculate the running total SaleAmount for each row ordered by SaleDate.
select saleID, salesPerson, saleDate, saleAmount,
	sum(saleAmount) over (order by saleDate) as running_total
from sales;

-- 2. calculate the cumulative sales amount for each salesperson over time.
select saleID, salesPerson, saleDate, saleAmount,
	sum(saleAmount) over (partition by salesPerson order by saleDate) as cumulative_sales
from sales;

-- 3. rank each sale based on the SaleAmount in descending order.
select saleID, salesPerson, saleDate, saleAmount, 
       rank() over (order by saleAmount desc) as rank
from sales;

-- 4. calculate a moving average of SaleAmount
select saleID, salesPerson, saleDate, saleAmount, 
       avg(saleAmount) over (order by saleDate rows between 2 preceding and current row) as moving_avg
from sales;

-- 5. Rank sales by saleAmount (Highest sale first)
select saleID, salesPerson, saleDate, saleAmount,
	dense_rank() over (order by saleAmount desc) as rank
from sales;	

-- 6. Rank Sales within each salesperson by saleAmount (Highest sale first)
select saleID, salesPerson, saleDate, saleAmount,
	rank() over (partition by salesPerson order by  saleAmount desc) as rank
from sales;

-- 7. Assign a unique row number to each sale ordered by Sale Date
select saleID, salesPerson , saleDate, saleAmount,
	row_number() over (order by saleDate) as row_num
from sales;

-- 8. Assign a unique row number to each sale within each salesperson, ordered by sale date
select saleID, salesPerson, saleDate, saleAmount,
	row_number() over (partition by salesPerson order by saleDate) as row_num
from sales;

-- 9. divide sales into 4 quartiles by sale amount
select saleID, salesPerson, saleDate, saleAmount,
	ntile(4) over (order by saleAmount desc) as quartile
from sales;

-- 10. divide sales into 3 tiers by sale date
select saleID, salesPerson, saleDate, saleAmount,
	ntile(3) over (order by saleDate) as tier
from sales;


-----------------------------------------------------------------------------------------------------------------------
--------------------------------------------------- Task Day 7 --------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------

--1. Get the First Sale Amount for Each Salesperson Based on Sale Date
WITH RankedSales AS (
    SELECT 
        saleID,
        salesPerson,
        saleDate,
        saleAmount,
        ROW_NUMBER() OVER (PARTITION BY salesPerson ORDER BY saleDate) AS rn
    FROM sales
)
SELECT 
    salesPerson,
    saleAmount AS first_sale_amount
FROM RankedSales
WHERE rn = 1;

--2. Get the Last Sale Amount for Each Salesperson Based on Sale Date
WITH RankedSales AS (
    SELECT 
        saleID,
        salesPerson,
        saleDate,
        saleAmount,
        ROW_NUMBER() OVER (PARTITION BY salesPerson ORDER BY saleDate DESC) AS rn
    FROM sales
)
SELECT 
    salesPerson,
    saleAmount AS last_sale_amount
FROM RankedSales
WHERE rn = 1;

--3. Get the Next Sale Amount for Each Sale
SELECT 
    saleID,
    salesPerson,
    saleDate,
    saleAmount,
    LEAD(saleAmount) OVER (PARTITION BY salesPerson ORDER BY saleDate) AS next_sale_amount
FROM sales;

--4. Get the Previous Sale Amount for Each Sale
SELECT 
    saleID,
    salesPerson,
    saleDate,
    saleAmount,
    LAG(saleAmount) OVER (PARTITION BY salesPerson ORDER BY saleDate) AS previous_sale_amount
FROM sales;

--5. from our previous table of employees and departments write the query to find the nth highest salary for a given department(say 3rd). you can insert your own data.
WITH RankedSalaries AS (
    SELECT 
        e_name,
        dept_id,
        salary,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM Employee
)
SELECT 
    e_name,
    dept_id,
    salary
FROM RankedSalaries
WHERE rnk = 3; 

--6. Find the 3rd highest sale amount for each salesperson. If a salesperson has fewer than 3 sales, return NULL for that salesperson.
WITH SaleRank AS (
    SELECT
        salesPerson,
        saleAmount,
        RANK() OVER (PARTITION BY salesPerson ORDER BY saleDate) AS sale_rank
    FROM sales
)
SELECT salesPerson,
       CASE WHEN sale_rank = 3 THEN saleAmount ELSE NULL END AS third_highest_sale
FROM SaleRank
WHERE sale_rank = 3
ORDER BY salesPerson;

--7.Find the top salesperson (the one with the highest total sales amount) for each month in 2023. If there are ties within a month, return all tied salespeople.
WITH MonthlySales AS (
    SELECT
        salesPerson,
        EXTRACT(MONTH FROM saleDate) AS sale_month,
        EXTRACT(YEAR FROM saleDate) AS sale_year,
        SUM(saleAmount) AS total_sales
    FROM sales
    WHERE saleDate BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY salesPerson, sale_month, sale_year
),
RankedSales AS (
    SELECT
        salesPerson,
        sale_month,
        sale_year,
        total_sales,
        RANK() OVER (PARTITION BY sale_month, sale_year ORDER BY total_sales DESC) AS rank
    FROM MonthlySales
)
SELECT
    salesPerson,
    sale_month,
    sale_year,
    total_sales
FROM RankedSales
WHERE rank = 1
ORDER BY sale_year, sale_month;














