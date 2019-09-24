--1. Employee detail
	Select a.emp_no, last_name, first_name, gender, salary from employees a
		left join Salaries b
			on a.emp_no = b.emp_no;
--2. Hired in 1986
	select * from employees
	where Extract(year from hire_date)=1986;
	
--3. Mgr by Dept
select a.dept_no, b.dept_name, a.emp_no,c.last_name, c.first_name, from_date, to_date
	from dept_mgr a
	
	left join Departments b
		on a.dept_no = b.dept_no

	left join employees c
		on a.emp_no = c.emp_no;

--4 Employee by Dept
select a.emp_no, a.last_name, a.first_name, b.dept_name
	from Employees a
	left join 
		(select distinct emp_no, b.dept_no, dept_name 
		 	from dept_employees a
				left join departments B
				on a.dept_no = b.dept_no) b
			on a.emp_no = b.emp_no	;
			
--5. Names w\ Hercules B.
select * from Employees 
where first_name = 'Hercules' and left(last_name,1)='B';

--6. Sales dept employees

select a.emp_no, a.last_name, a.first_name, b.dept_name
	from Employees a
	left join 
		(select distinct emp_no, b.dept_no, dept_name 
		 	from dept_employees a
				left join departments B
				on a.dept_no = b.dept_no) b
			on a.emp_no = b.emp_no
	where dept_name ='Sales';

--7. Sales and Development dept employees

select a.emp_no, a.last_name, a.first_name, b.dept_name
	from Employees a
	left join 
		(select distinct emp_no, b.dept_no, dept_name 
		 	from dept_employees a
				left join departments B
				on a.dept_no = b.dept_no) b
			on a.emp_no = b.emp_no
	where dept_name in ('Sales','Development');

--8. Common last_names by frequency
select last_name, count(*)
from Employees
	group by last_name
order by 2 desc;
