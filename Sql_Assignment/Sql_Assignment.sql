-- Creating a new database named MarketCo
create database MarketCo;

-- Using the created database
use MarketCo;

-- Creating Company table to store company details
create table Company
(
CompanyID int primary key,             -- Unique ID for each company
CompanyName varchar(45),              -- Name of the company
Street varchar(45),                   -- Street address
City varchar(45),                     -- City name
State varchar(2),                     -- State abbreviation (like GJ)
Zip varchar(10)                       -- ZIP code
);

-- Creating Contact table to store contacts of companies
create table Contact
(
ContactID int primary key,            -- Unique ID for each contact
CompanyID int,                        -- Foreign key to Company table
FirstName varchar(45),               -- Contact's first name
LastName varchar(45),                -- Contact's last name
Street varchar(45),                  -- Address street
City varchar(45),                    -- City name
State varchar(2),                    -- State abbreviation
Zip varchar(10),                     -- ZIP code
IsMain boolean,                      -- Is this the main contact?
Email varchar(45),                   -- Email address
Phone varchar(12)                    -- Phone number
);

-- Adding a foreign key to link Contact with Company
alter table Contact add foreign key(CompanyID) references Company(CompanyID);

-- Creating table to store employee interactions with contacts
create table ContactEmployee
(
    ContactEmployeeID int primary key,   -- Unique ID for each interaction
    ContactID int,                       -- Foreign key to Contact table
    EmployeeID int,                      -- Foreign key to Employee table
    ContactDate date,                    -- Date of contact
    Description varchar(100)            -- Description of the interaction
);

-- Linking ContactEmployee with Contact table
alter table ContactEmployee add foreign key(ContactID) references Contact(ContactID);

-- Linking ContactEmployee with Employee table
alter table ContactEmployee add foreign key(EmployeeID) references Employee(EmployeeID);

-- Creating Employee table to store employee details
create table Employee
(
    EmployeeID int primary key,         -- Unique ID for each employee
    FirstName varchar(45),              -- First name
    LastName varchar(45),               -- Last name
    Salary decimal(10,2),               -- Salary amount
    HireDate date,                      -- Date of hiring
    JobTitle varchar(25),               -- Job title
    Email varchar(45),                  -- Email address
    Phone varchar(12)                   -- Phone number
);


-- Inserting data into Company table
insert into Company values
(1, 'TechNova Solutions', '123 Maple St', 'Ahmedabad', 'GJ', '380015'),
(2, 'BrightPath Corp', '456 Pine Rd', 'Surat', 'GJ', '395007'),
(3, 'EcoWare Pvt Ltd', '789 Oak Ave', 'Vadodara', 'GJ', '390001'),
(4, 'Urban Outfitters, Inc', '666 Maple St', 'Ahmedabad', 'GJ', '380018');

-- Inserting data into Contact table
insert into Contact values
(1, 1, 'Riya', 'Shah', '123 Maple St', 'Ahmedabad', 'GJ', '380015', TRUE, 'riya@technova.com', '9876543210'),
(2, 2, 'Mehul', 'Patel', '456 Pine Rd', 'Surat', 'GJ', '395007', TRUE, 'mehul@brightpath.com', '9876512345'),
(3, 2, 'Sneha', 'Desai', '789 Oak Ave', 'Surat', 'GJ', '395007', FALSE, 'sneha@brightpath.com', '9876567890'),
(4, 3, 'Dianne', 'Connor', '789 Oak Ave', 'Vadodara', 'GJ', '390001', TRUE, 'aarav@ecoware.com', '9876534567');

-- Inserting data into Employee table
insert into Employee values
(101, 'Nidhi', 'Kapoor', 60000.00, '2021-04-12', 'Sales Manager', 'nidhi@marketco.com', '9087654321'),
(102, 'Jack', 'Lee', 45000.00, '2022-01-20', 'Marketing Executive', 'raj@marketco.com', '9012345678'),
(103, 'Anjali', 'Trivedi', 50000.00, '2020-10-01', 'Business Analyst', 'anjali@marketco.com', '9001234567'),
(104, 'Lesley', 'Bland', 55000.00, '2023-03-15', 'Project Manager', 'lesley@marketco.com', '666-555-0000');

-- Inserting data into ContactEmployee table (employee meetings)
insert into ContactEmployee values
(1, 1, 101, '2024-05-01', 'Initial meeting with TechNova team'),
(2, 2, 102, '2024-05-02', 'Marketing discussion with BrightPath'),
(3, 3, 103, '2024-05-03', 'Follow-up call with Sneha'),
(4, 4, 102, '2024-05-04', 'EcoWare onboarding session');

-- Updating phone number for employee with ID 104
update Employee set Phone = "215-555-8800" where EmployeeID = 104;

-- Updating company name for company ID 4
update company set CompanyName = "Urban Outfitters" where companyID = 4;

-- Deleting a contact employee record with ID 4
delete from ContactEmployee where ContactEmployeeID = 4;

-- Selecting contact names from a specific company
SELECT Contact.FirstName, Contact.LastName FROM Contact JOIN Company ON Contact.CompanyID = Company.CompanyID
WHERE Company.CompanyName = 'Toll Brothers';   -- This will return nothing unless 'Toll Brothers' exists


-- ===============  What is the significance of “%” and “_” operators in the LIKE statement?   ======================================================================================
 

-- The % and _ operators in the LIKE statement are wildcards used for pattern matching in SQL.

-- LIKE Statement Syntax:
-- SELECT * FROM table_name WHERE column_name LIKE 'pattern';

-- % (Percentage Sign):

-- Meaning: Matches zero, one, or many characters.
-- Use Case: When you don’t know the exact characters in the middle or end.

-- Examples:
-- WHERE name LIKE 'A%'     -- names starting with 'A' (e.g., "Anjali", "Amit")
-- WHERE name LIKE '%a'     -- names ending with 'a' (e.g., "Nisha", "Deepa")
-- WHERE name LIKE '%it%'   -- names containing 'it' anywhere (e.g., "Mital", "Smit")


-- _ (Underscore):

-- Meaning: Matches exactly one character.
-- Use Case: When you want to match a fixed number of characters with unknown positions.

-- Examples:
-- WHERE name LIKE '_at'     -- any 3-letter name ending with 'at' (e.g., "Pat", "Kat")
-- WHERE name LIKE 'S__'     -- any 3-letter name starting with 'S' (e.g., "Sam", "Sid")

-- Combined Use:
-- WHERE name LIKE '_a%'     -- second letter must be 'a' (e.g., "Mahi", "Ravi", "Naman")


-- Summary:
-- Operator	    		Matches				  Example				 Matches Example
-- %				0 or more characters		'M%'				Mital, Meena, Mohit
-- _				Exactly 1 character			'M_t'				Mat, Mit, Mot


-- ===========================  Explain normalization in the context of databases. ==============================================================================================


-- Normalization is the process of organizing data in a database to eliminate redundancy (duplicate data) 
-- and ensure data integrity.

-- It divides large tables into smaller, related tables and links them using keys.

-- Example of Normalization:

-- => Before Normalization (Redundant Data):

-- Order Table:
-- OrderID | CustomerName | CustomerPhone | Product
-- -------------------------------------------------
-- 1       | Priya         | 9876543210     | Laptop
-- 2       | Priya         | 9876543210     | Mouse

-- Here, customer information is repeated in multiple rows, which leads to data redundancy.

-- => After Normalization:

-- Customer Table:
-- CustomerID | Name  | Phone
-- -------------------------------
-- 101        | Priya | 9876543210

-- Order Table:
-- OrderID | CustomerID | Product
-- ------------------------------
-- 1       | 101        | Laptop
-- 2       | 101        | Mouse

-- Benefit: Data duplication is eliminated, and updating or managing the data becomes easier and more efficient.

-- Forms of Normalization (Main 3):

-- 🔹 1NF – First Normal Form:
-- Remove repeating groups
-- Every column should have atomic (indivisible) values.

-- 🔹 2NF – Second Normal Form:
-- Should be in 1NF
-- Remove partial dependency (only part of primary key is determining other data)
-- Mostly used in tables with composite primary keys.

-- 🔹 3NF – Third Normal Form:
-- Should be in 2NF

-- Remove transitive dependency
-- Non-key → Non-key dependency not allowed

-- Example:
-- If Student_ID → Class_ID
-- and Class_ID → Class_Teacher
-- Then: Student_ID → Class_Teacher (This is transitive — break it!)


-- ==================  What does a join in MySQL mean?  ==================================================================================

-- *** What is a JOIN in MySQL?
-- A JOIN in MySQL is used to combine rows from two or more tables based on a related column between them.

-- *** Why use JOIN?
-- Because data is stored in multiple related tables (thanks to normalization), so we use JOIN to fetch complete 
-- information by connecting those tables.

-- *** Types of JOIN in MySQL:

-- 1. INNER JOIN
-- Returns only the matching rows from both tables.

-- query: SELECT * FROM A INNER JOIN B ON A.id = B.id;

-- 2. LEFT JOIN (or LEFT OUTER JOIN)
-- Returns all rows from the left table, and matching rows from the right table.
-- If no match, NULLs are returned from the right.

-- query: SELECT * FROM A LEFT JOIN B ON A.id = B.id;

-- 3. RIGHT JOIN (or RIGHT OUTER JOIN)
-- Returns all rows from the right table, and matching rows from the left table.
-- If no match, NULLs from the left.

-- query: SELECT * FROM A RIGHT JOIN B ON A.id = B.id;

-- 4. A CROSS JOIN returns the cartesian product of two tables —
-- i.e., it combines every row of the first table with every row of the second table.

-- Use When:
-- You want all possible combinations of rows from two table

-- query: SELECT * FROM A CROSS JOIN B ON A.id = B.id;


-- ===============  What do you understand about DDL, DCL, and DML in MySQL?  ================================================================


-- Type			Full Form				       	Purpose					Common Commands
-- DDL			Data Definition Language		Defines structure			CREATE, ALTER, DROP
-- DML			Data Manipulation Language		Works with data				SELECT, INSERT, UPDATE
-- DCL			Data Control Language			Controls permissions		GRANT, REVOKE


-- 1. DDL – Data Definition Language
-- Used to define or modify the structure of database objects like tables.

-- Commands:
-- CREATE
-- ALTER
-- DROP
-- TRUNCATE

-- Example:
-- CREATE TABLE Students (ID INT, Name VARCHAR(50));

-- 2. DML – Data Manipulation Language
-- Used to insert, update, or retrieve data from tables.

-- Commands:
-- SELECT
-- INSERT
-- UPDATE
-- DELETE

-- Example:
-- INSERT INTO Students VALUES (1, 'Priya');

-- 3. DCL – Data Control Language
-- Used to control access and permissions on the database.

-- Commands:
-- GRANT
-- REVOKE

-- Example:
-- GRANT SELECT ON Students TO 'user1';


-- =============  What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?  =============================


-- The JOIN clause in MySQL is used to combine rows from two or more tables based on a related column between them.
-- It helps retrieve meaningful data that is split across multiple tables due to normalization.

-- Why JOIN is important:
-- 1. Maintains data relationships
-- 2. Avoids duplicate data
-- 3. Makes reporting and analysis easier

-- types:

-- 1. INNER JOIN
-- Returns only matching rows from both tables.

-- SELECT customers.name, orders.product
-- FROM customers
-- INNER JOIN orders
-- ON customers.id = orders.customer_id;

-- 2. LEFT JOIN (Left Outer Join)
-- Returns all rows from the left table, and matched rows from the right table.
-- If no match, NULL is shown for right table columns.

-- SELECT customers.name, orders.product
-- FROM customers
-- LEFT JOIN orders
-- ON customers.id = orders.customer_id;

-- 3. RIGHT JOIN (Right Outer Join)
-- Returns all rows from the right table, and matched rows from the left table.

-- SELECT customers.name, orders.product
-- FROM customers
-- RIGHT JOIN orders
-- ON customers.id = orders.customer_id;

-- 4. FULL JOIN (Not directly supported in MySQL)
-- Returns all rows from both tables — matched or unmatched.
-- In MySQL, use UNION of LEFT and RIGHT JOIN.

-- SELECT customers.name, orders.product
-- FROM customers
-- LEFT JOIN orders ON customers.id = orders.customer_id

-- UNION

-- SELECT customers.name, orders.product
-- FROM customers
-- RIGHT JOIN orders ON customers.id = orders.customer_id;

-- 5. CROSS JOIN
-- Returns all possible combinations (cartesian product) of two tables.

-- SELECT customers.name, products.product_name
-- FROM customers
-- CROSS JOIN products









