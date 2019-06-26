-- DROP TABLE IF EXISTS Departments;
-- DROP TABLE IF EXISTS Dept_Employees;


Create Table Departments ( 
-- 	IDNumber serial ,		  
	Dept_No Varchar (25) NOT NULL, 
	Dept_Name Varchar(25) NOT NULL,
	Primary Key (Dept_No)
	);

Create Table Dept_Employees ( 
-- 	IDNumber serial ,		  
	emp_no integer NOT NULL ,
	Dept_No Varchar (25) NOT NULL,
	from_date Date NOT NULL,
	to_date Date NOT NULL,
	Foreign Key (dept_no) References Departments (dept_No)
	);
	
Create Table Dept_Mgr ( 
-- 	IDNumber serial ,		  
	Dept_No Varchar (25) NOT NULL,
	emp_no integer NOT NULL ,
	from_date Date NOT NULL,
	to_date Date NOT NULL
--	Foreign Key (dept_no) References Departments (dept_No)
-- 	Foreign Key (emp_no) References Departments (Employee)
	);
	
Create Table Employees ( 
-- 	IDNumber serial ,		  
	emp_no integer NOT NULL ,
	birth_date date NOT NULL,
	first_name varchar (25),
	last_name varchar (25),
	gender varchar (1),
	hire_date date
);

Create Table Salaries ( 
-- 	IDNumber serial ,		  
	emp_no integer NOT NULL ,
	salary int NOT NULL,
	from_date Date NOT NULL,
	to_date Date NOT NULL
);

Create Table Titles ( 
-- 	IDNumber serial ,		  
	emp_no integer NOT NULL ,
	title varchar (50) NOT NULL,
	from_date Date NOT NULL,
	to_date Date NOT NULL
);

