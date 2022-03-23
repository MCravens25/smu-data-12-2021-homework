-- 1) List the following details of each employee: employee number, last name, first name, sex, and salary.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees e
	join salaries s on e.emp_no = s.emp_no;
	
	
-- 2) List first name, last name, and hire date for employees who were hired in 1986.	
select
	e.first_name,
	e.last_name,
	e.hire_date
from
	employees e
where
	e.hire_date >= '1986-01-01'
	AND e.hire_date <= '1986-12-31';
	
-- 3)List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
from
 	departments as d
 	Join dept_manager as dm ON dm.dept_no= d.dept_no
	Join employees as e on e.emp_no = dm.emp_no;

-- 4)List the department of each employee with the following information: employee number, last name, first name, and department name.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from
 	employees as e
 	Join dept_employee as de ON de.emp_no= e.emp_no
	Join departments as d on d.dept_no = de.dept_no;

--5)List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select
	e.first_name,
	e.last_name,
	e.sex
from
	employees e
where
	e.first_name = 'Hercules'
	and e.last_name like 'B%';
	
--6)List all employees in the Sales department, including their employee number, last name, first name, and department name.
select
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
from
 	employees as e
 	Join dept_employee as de ON de.emp_no= e.emp_no
	Join departments as d on d.dept_no = de.dept_no
Where
	d.dept_name = 'Sales';
	
--7)List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
from
 	employees as e
 	Join dept_employee as de ON de.emp_no= e.emp_no
	Join departments as d on d.dept_no = de.dept_no
Where
	d.dept_name = 'Sales'
	OR d.dept_name = 'Development';

--8)In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select
	e.last_name,
	count(emp_no) as num_employees
from
	employees e
group by
	e.last_name
order by
	num_employees desc;



-- epilogue
select
*
from
employees