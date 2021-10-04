

-- TASK 1
-- USE PARTS DB TO WRITE THE FOLLOWING QUERIES

use PARTS;

select * from parts.part; 
select * from parts.project; 
select * from parts.supplier; 
select * from parts.supply; 

-- Q1
-- find the name and weight from each red part
-- i know that it is not necessary to add 'p.colour' in the select statetment but i do it 
-- so i can visibly see all the colours are indeed red.
select p.pname as 'Part_Name', p.weight as 'Part_Weight', p.colour
from part p
where p.colour = 'red';

-- Q2
-- find all unique supplier(s) name from London
-- i know that it is not necessary to add 's.city' in the select statetment but i do it 
-- so i can visibly see all the cities are indeed London.
select distinct s.sname as 'Supplier_Name', s.city 
from supplier s
where s.city = 'London';

-- TASK 2
-- USE SHOP SALES DB TO WRITE THE FOLLOWING QUERIES

use shop;
select * from shop.sales1; 

-- Q1
select * from shop.sales1; 
-- Find out how many sales were recorded each week on different days of the week
SELECT s.Day, s.Week, count(*) as 'Frequency_of_Sales'
from sales1 s
group by s.Week, s.Day
order by s.Week; 

-- Q2
-- We need to change salesperson's name Inga to Annette
use shop;

SET SQL_SAFE_UPDATES = 0;
UPDATE sales1
SET 
    SalesPerson = 'Annette'
WHERE 
    SalesPerson = 'Inga';
SET SQL_SAFE_UPDATES = 1;

-- For this question I had to temporary disable the safe update option of MySQL as the 'sales1' table for the shop database
-- doesn't have a corresponding primary key for 'SalesPerson' where we would have a unique ID for 'SalesPerson'
-- that I would be able to use in the where clause in the 'UPDATE' function

-- Q3
select * from shop.sales1; 
-- Find out how many sales did Annette do
select s.SalesPerson, count(*) as 'Total_Sales'
from sales1 s
where s.SalesPerson = 'Annette';
	
-- Q4
SELECT * from shop.sales1;
-- Find the total sales amount by each person by day
SELECT sum(s.SalesAmount), s.SalesPerson, s.Day
from sales1 s
group by s.SalesPerson, s.Day;

-- Q5
use shop;
SELECT * from shop.sales1;
-- How much (sum) each person sold for the given period
select sum(s.SalesAmount), s.SalesPerson
from sales1 s
group by s.SalesPerson;

-- Q6
select * from shop.sales1;
-- How much (sum) each person sold for the given period, including the 
-- number of sales per person, their average, lowest and highest sale amounts
select sum(s.SalesAmount), s.SalesPerson, count(*) as 'Number_of_Sales', 
avg(s.SalesAmount), min(s.SalesAmount), max(s.SalesAmount)
from sales1 s
group by s.SalesPerson;

-- Q7
select * from shop.sales1;
-- Find the total monetary sales amount achieved by each store
select sum(s.SalesAmount), s.Store
from sales1 s
group by s.Store;

-- Q8 
select * from shop.sales1;
-- Find the number of sales by each person if they did less than 3 sales for 
-- the past period
SELECT count(*) as 'Number_Of_Sales', s.SalesPerson
from sales1 s
group by s.SalesPerson
having count(*) < 3;

-- Q9
select * from shop.sales1;
-- Find the total amount of sales by month where combined total is less than £100
SELECT sum(s.SalesAmount) as 'Total_Sales', s.Month 
from sales1 s
group by s.Month
having Total_Sales < 100;