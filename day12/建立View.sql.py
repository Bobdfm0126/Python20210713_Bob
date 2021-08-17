CREATE VIEW emp_dept_view
AS
SELECT
	e.emp_id, e.dept_id, d.dept_name, e.emp_name, e.emp_salary, e.create_date
FROM
	employees e, departments d
WHERE
	e.dept_id = d.dept_id
SELECT * FROM emp_dept_view
