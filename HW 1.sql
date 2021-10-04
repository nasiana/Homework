use parts;
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
where (sy.S_ID = 'S2' or sy.S_ID = 'S3' or sy.S_ID = 'S5');

