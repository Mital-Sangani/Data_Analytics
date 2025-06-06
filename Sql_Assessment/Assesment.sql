create database assessment;

use Assessment;


-- ==============================  QUESTION-1  ======================================================================================


create table worker (
	worker_id int primary key,
	first_name varchar(20),
	last_name varchar(20),
	salary decimal(10,2),
    joining_date datetime,
    department varchar(30)
);

insert into worker values
(1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
(2, 'Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
(3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
(4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'),
(5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
(6, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
(7, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
(8, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');

# 1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.

select * from worker order by first_name asc, department desc;	

# 2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” from the Worker table. 

# select * from worker where worker_id in(6,7);

select * from worker where first_name in("Vipul", "Satish");

# 3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets. 

select * from worker where first_name like '_____h';

# 4. Write an SQL query to print details of the Workers whose SALARY lies between 1. 

select * from worker where salary between 1000 and 100000;

# 5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. 

SELECT first_name, COUNT(*) AS dup_count
FROM worker
GROUP BY first_name
HAVING COUNT(*) > 1;

-- 6. Write an SQL query to show the top 6 records of a table.

SELECT * FROM worker ORDER BY salary DESC LIMIT 6;

-- 7. Write an SQL query to fetch the departments that have less than five people in them. 

SELECT department, COUNT(*) AS total_workers
FROM worker
GROUP BY department
HAVING COUNT(*) < 5;

-- 8. Write an SQL query to show all departments along with the number of people in there. 

SELECT department, COUNT(*) AS total_people
FROM worker
GROUP BY department;

-- 9. Write an SQL query to print the name of employees having the highest salary in each department. 

select first_name, last_name, department, salary from worker
where salary in(select max(salary) from worker group by department);


-- ==============================  QUESTION-2  ======================================================================================

CREATE TABLE student (
    StdID INT PRIMARY KEY,
    StdName VARCHAR(50),
    Sex VARCHAR(10),
    Percentage INT,
    Class VARCHAR(10),
    Sec VARCHAR(5),
    Stream VARCHAR(20),
    DOB DATE
);

INSERT INTO student (StdID, StdName, Sex, Percentage, Class, Sec, Stream, DOB) VALUES
(1001, 'Sureka Joshi', 'Female', 82, '12', 'A', 'Science', STR_TO_DATE('3/8/1998', '%d/%m/%Y')),
(1002, 'MAAHI AGARWAL', 'Female', 56, '11', 'C', 'Commerce', STR_TO_DATE('11/23/2008', '%m/%d/%Y')),
(1003, 'Sanam Verma', 'Male', 59, '11', 'C', 'Commerce', STR_TO_DATE('6/29/2006', '%m/%d/%Y')),
(1004, 'Ronit Kumar', 'Male', 63, '11', 'C', 'Commerce', STR_TO_DATE('11/5/1997', '%m/%d/%Y')),
(1005, 'Dipesh Pulkit', 'Male', 78, '11', 'B', 'Science', STR_TO_DATE('14/09/2003', '%d/%m/%Y')),
(1006, 'JAHANVI Puri', 'Female', 60, '11', 'B', 'Commerce', STR_TO_DATE('11/7/2008', '%m/%d/%Y')),
(1007, 'Sanam Kumar', 'Male', 72, '12', 'F', 'Commerce', STR_TO_DATE('3/8/1998', '%d/%m/%Y')),
(1008, 'SAHIL SARAS', 'Male', 56, '11', 'C', 'Commerce', STR_TO_DATE('11/7/2008', '%m/%d/%Y')),
(1009, 'AKSHRA AGARWAL', 'Female', 72, '12', 'B', 'Commerce', STR_TO_DATE('10/1/1996', '%m/%d/%Y')),
(1010, 'STUTI MISHRA', 'Female', 39, '11', 'F', 'Science', STR_TO_DATE('11/23/2008', '%m/%d/%Y')),
(1011, 'HARSH AGARWAL', 'Male', 60, '11', 'C', 'Science', STR_TO_DATE('3/8/1998', '%d/%m/%Y')),
(1012, 'NIKUNJ AGARWAL', 'Male', 49, '12', 'C', 'Commerce', STR_TO_DATE('28/06/1998', '%d/%m/%Y')),
(1013, 'AKRITI SAXENA', 'Female', 89, '12', 'A', 'Science', STR_TO_DATE('11/23/2008', '%m/%d/%Y')),
(1014, 'TANI RASTOGI', 'Female', 82, '12', 'A', 'Science', STR_TO_DATE('11/23/2008', '%m/%d/%Y'));


-- 1 To display all the records form STUDENT table. SELECT * FROM student ;  

 SELECT * FROM student ;  
 
 -- 2. To display any name and date of birth from the table STUDENT. 
 
 SELECT StdName, DOB FROM student ; 
 
 -- 3. To display all students record where percentage is greater of equal to 80 FROM student table. 
 
SELECT * FROM student WHERE percentage >= 80;  

-- 4. To display student name, stream and percentage where percentage of student is more than 80 

SELECT StdName, Stream, Percentage FROM student WHERE percentage > 80;  

-- 5. To display all records of science students whose percentage is more than 75 form student table. 

SELECT * From student WHERE stream = 'Science' AND percentage > 75;
 
 
 
 