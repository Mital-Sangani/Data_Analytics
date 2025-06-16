create database project;

use project;

create table driver (
	driv_id int primary key auto_increment,
    driv_name varchar(30),
    age int,
    vehcl_type varchar(30),
    charge decimal(10,2),
    availability varchar(30)
);

create table passenger (
	start_point varchar(50),
    end_point varchar(50),
    price int,
    passgr_name varchar(30),
    driv_id int, 
    foreign key (driv_id) references driver(driv_id)
);

update passenger set passgr_name = 'Ronak Vora' where passgr_name = 'Sneha Dave';

-- List all available drivers with "Electric" vehicle type.
select * from driver 
where availability = 'available' and vehcl_type = 'auto';			-- 1


-- Find all passengers who paid more than ₹200.
select * from passenger 
where price > 200;													-- 2


-- Show all passengers along with their driver names.
select passenger.passgr_name, driver.driv_name, driver.vehcl_type
from passenger
join driver on passenger.driv_id = driver.driv_id;					-- 3


-- Find total earning (price) of each driver.
select driver.driv_id, sum(passenger.price) as total_earning
from passenger 
join driver on passenger.driv_id = driver.driv_id
group by driver.driv_id;											-- 4


-- List all drivers who have done at least 2 rides.
select driver.driv_name, count(*) as ride_count
from passenger 
join driver on passenger.driv_id = driver.driv_id
group by driver.driv_id
having count(*) >= 2;												-- 5


-- Find youngest driver who is currently available.
select * from driver 
where availability = 'available'
order by age
limit 1;															-- 6


-- Find all passengers who traveled with SUV drivers.
select passenger.passgr_name, driver.vehcl_type 
from passenger 
join driver on driver.driv_id = passenger.driv_id
where driver.vehcl_type = 'SUV';									-- 7


-- Show drivers who have not taken any passengers yet.
select driv_name, driv_id from driver
where driv_id not in (
	select distinct driv_id from passenger                 	-- first method 8(1)
);

select driver.driv_name, driver.driv_id
from driver 
left join passenger on driver.driv_id = passenger.driv_id
where passenger.driv_id is null;							-- second method 8(2)


-- List total number of rides by each vehicle type.
select vehcl_type, count(*) as total_rides
from driver
group by vehcl_type
having count(*) > 1;												-- 9


-- Show driver and passenger pairs where price > charge × 10
select driver.driv_name, passenger.passgr_name, driver.charge, passenger.price
from passenger
join driver on driver.driv_id = passenger.driv_id
where passenger.price > driver.charge * 10;							-- 10


-- Average fare paid to each vehicle type
select d.vehcl_type, AVG(p.price) as avg_fare
from passenger p
join driver d on d.driv_id = p.driv_id
group by d.vehcl_type;												-- 11


-- Find all drivers whose age is below 40 and drive a Sedan.
select * from driver
where age < 40 and vehcl_type = 'SEDAN';							-- 12


-- Find the total number of passengers for each driver.
select d.driv_name, count(*) as total_passengers
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.driv_name;												-- 13


-- Show passengers who started their ride from 'Sardar Chowk' and ended at 'Gokuldham'.
select * from passenger
where start_point = 'Sardar Chowk' and end_point = 'Gokuldham';		-- 14


-- Find vehicle type-wise maximum fare received.
select d.vehcl_type, max(p.price) as maximum_fare
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.vehcl_type;												-- 15


-- List all passengers who travelled with a driver charging more than ₹250.
select p.passgr_name, d.driv_name, d.charge
from driver d
left join passenger p on d.driv_id = p.driv_id
where d.charge > 200;												-- 16


-- Find passengers who paid fare more than the average fare.
select passgr_name, price from passenger
where price > (
	select avg(price) from passenger
);																	-- 17


-- Find most used vehicle type and how many times it was used.
select d.vehcl_type, count(*) as total_rides
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.vehcl_type
order by total_rides desc
limit 1;															-- 18


-- Which driver took the longest route (based on max price)?
select d.driv_name, p.price, p.start_point, p.end_point
from driver d
left join passenger p on d.driv_id = p.driv_id
order by p.price desc
limit 1;															-- 19


-- Find average fare paid per route (start_point to end_point).
select start_point, end_point, AVG(price) as avg_fare
from passenger
group by start_point, end_point;									-- 20



-- Driver availability status report (how many available/unavailable).
select availability, count(*) as total_availability 
from driver
group by availability ;												-- 21


--  List all drivers whose age is between 25 and 40.
select driv_name, age 
from driver
where age between 25 and 40;										-- 22


-- Average price by vehicle type, ordered descending:
select d.vehcl_type, AVG(p.price) as avg_price
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.vehcl_type
order by avg_price desc;											-- 23


-- Find names of all drivers who have driven passengers only once.
select d.driv_id, d.driv_name, count(passgr_name) as total_driven
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.driv_id
having total_driven = 1;											-- 24


-- Find drivers who have the highest total earnings (fare sum)
select d.driv_name, sum(p.price) as total_earnings
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.driv_id
order by total_earnings desc
limit 1;															-- 25


-- Show passengers who have travelled with more than one driver
select p.passgr_name, count(*) as pass_ride_count
from passenger p
join driver d on d.driv_id = p.driv_id
group by p.passgr_name
having pass_ride_count > 1; 									   -- 26(1)


select passgr_name
from passenger
group by passgr_name
having COUNT(DISTINCT driv_id) > 1;								   -- 26(2)


-- Find drivers whose vehicle type is unique (only one driver has that type)
select driv_name, vehcl_type
from driver
where vehcl_type in (
	select vehcl_type from driver group by vehcl_type having count(*) = 1
);																	-- 27


-- Find driver(s) whose charge is closest to the average charge
select * from driver
order by ABS(charge - (select AVG(charge) from driver))
limit 1;															 -- 28
 

 -- Show start and end points of the route that has the highest average fare
 select start_point, end_point, AVG(price) as avg_fare
 from passenger
 group by start_point, end_point
 order by avg_fare desc
 limit 1;															 -- 29
 

-- List the vehicle type that generated the lowest total earning
select d.vehcl_type, SUM(p.price) as lowest_earning
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.vehcl_type
order by lowest_earning
limit 1 offset 1;													 -- 30


-- Find passengers who always travel with the same driver
select passgr_name from passenger
group by passgr_name
having COUNT(DISTINCT driv_id) = 1;									 -- 31


-- Show each driver’s max and min fare they received
select d.driv_name, MAX(p.price) as max_fare, MIN(p.price) as min_fare
from driver d
join passenger p on d.driv_id = p.driv_id
group by d.driv_id;													 -- 32


-- List drivers who have completed rides but their vehicle is currently unavailable
select distinct d.driv_name
from driver d
join passenger p on d.driv_id = p.driv_id	
where d.availability != 'available';								 -- 33


-- Show fare difference between each passenger's fare and the average fare
select passgr_name, price, 
       ABS(price - (select AVG(price) from passenger)) as fare_difference
from passenger;														 -- 34


-- Find the number of passengers for each vehicle type
select d.vehcl_type, COUNT(p.passgr_name) as total_passengers
from driver d
left join passenger p on d.driv_id = p.driv_id
group by d.vehcl_type;												 -- 35