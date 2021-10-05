-- TASK 3
use parts;

-- Q1
-- Find the name and city of each project not supplied by a London-based supplier
select * from parts.part;
select * from parts.project;
select * from parts.supplier;
select * from parts.supply;

-- table showing project name, project city and J_ID
select pj.jname, pj.city, pj.j_id
from project pj;

-- What is the S_ID of the non-London based suppliers
select sp.S_ID
from supplier sp
where City != 'London';


-- table showing J_ID and S_ID for values corresponding to a non London based supplier for S_ID
select sy.J_ID, sy.S_ID
from supply sy
where sy.S_ID IN ('S2', 'S3', 'S5');


-- Find the name and city of each project not supplied by a London-based supplier
-- self-joining project and supply tables 
SELECT DISTINCT pj.jname as 'Name_of_Project', pj.city as 'City_of_Project'
from project pj
INNER JOIN supply sy ON pj.j_ID = sy.j_ID
where sy.S_ID IN (select sp.S_ID
from supplier sp
where City != 'London');
-- Projects have multiple suppliers
-- excludes project which have any supplier which is London based
SELECT DISTINCT pj.jname as 'Name_of_Project', pj.city as 'City_of_Project'
from project pj
INNER JOIN supply sy ON pj.j_ID = sy.j_ID
where (sy.S_ID IN (select sp.S_ID
from supplier sp
where City != 'London'))
and
(sy.S_ID NOT IN (select sp.S_ID
from supplier sp
where City = 'London'));

-- shows all the projects which have only London based supplier
SELECT DISTINCT pj.jname as 'Name_of_Project', pj.city as 'City_of_Project'
from project pj
INNER JOIN supply sy ON pj.j_ID = sy.j_ID
where 
sy.S_ID NOT IN (select sp.S_ID
from supplier sp
where City != 'London');

-- Q2
-- USE PARTS DB
select * from parts.part;
select * from parts.project;
select * from parts.supplier;
select * from parts.supply;
--
select sp.city, sp.s_ID from supplier sp;
select p.city, p.P_ID from part p;
select pj.city, pj.J_ID from project pj;


-- Find the supplier name, part name and project name for each case where a supplier supplies a project with a part, 
-- but also the supplier city, project city and part city are the same
select sp.sname as 'Supplier_Name', p.pname as 'Part_Name', pj.jname as 'Project_Name'
from supply sy 
LEFT JOIN supplier sp ON sy.S_ID = sp.s_ID
LEFT JOIN part p ON sy.P_ID = P.P_ID
LEFT JOIN project pj ON sy.J_ID = pj.J_ID;

-- but also the supplier city, project city and part city are the same
-- 
