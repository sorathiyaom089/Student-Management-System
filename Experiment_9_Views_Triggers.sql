DROP DATABASE IF EXISTS experiment_9;
CREATE DATABASE experiment_9;
USE experiment_9;

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

CREATE TABLE Salary_Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

INSERT INTO Department (dept_id, dept_name, location) VALUES
(1, 'IT', 'Mumbai'),
(2, 'HR', 'Delhi'),
(3, 'Finance', 'Bangalore'),
(4, 'Marketing', 'Pune'),
(5, 'Operations', 'Chennai');

INSERT INTO Employee (emp_id, emp_name, department, salary, hire_date) VALUES
(101, 'Amit Sharma', 'IT', 65000, '2023-01-15'),
(102, 'Priya Singh', 'HR', 55000, '2023-03-20'),
(103, 'Rahul Kumar', 'Finance', 70000, '2022-11-10'),
(104, 'Sneha Patel', 'IT', 60000, '2023-05-05'),
(105, 'Vijay Verma', 'Marketing', 58000, '2023-02-28'),
(106, 'Neha Gupta', 'IT', 72000, '2022-08-15'),
(107, 'Karan Mehta', 'Finance', 68000, '2023-04-12'),
(108, 'Pooja Reddy', 'HR', 52000, '2023-06-18');

CREATE VIEW High_Salary_Employees AS
SELECT emp_id, emp_name, department, salary
FROM Employee
WHERE salary > 60000;

CREATE VIEW IT_Department_View AS
SELECT emp_id, emp_name, salary, hire_date
FROM Employee
WHERE department = 'IT';

CREATE VIEW Employee_Count_By_Dept AS
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department;

DELIMITER //
CREATE TRIGGER before_salary_update
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
    IF NEW.salary <> OLD.salary THEN
        INSERT INTO Salary_Log (emp_id, old_salary, new_salary)
        VALUES (OLD.emp_id, OLD.salary, NEW.salary);
    END IF;
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER prevent_low_salary
BEFORE INSERT ON Employee
FOR EACH ROW
BEGIN
    IF NEW.salary < 30000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Salary cannot be less than 30000';
    END IF;
END;//
DELIMITER ;

SELECT * FROM High_Salary_Employees;

SELECT * FROM IT_Department_View;

SELECT * FROM Employee_Count_By_Dept;

UPDATE Employee SET salary = 75000 WHERE emp_id = 101;

UPDATE Employee SET salary = 62000 WHERE emp_id = 104;

SELECT * FROM Salary_Log;

SELECT * FROM High_Salary_Employees WHERE emp_id = 101;

DROP VIEW IF EXISTS Employee_Summary;
CREATE VIEW Employee_Summary AS
SELECT e.emp_id, e.emp_name, e.department, e.salary, 
       CASE 
           WHEN salary >= 70000 THEN 'High'
           WHEN salary >= 55000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_grade
FROM Employee e;

SELECT * FROM Employee_Summary;

SELECT department, salary_grade, COUNT(*) AS count
FROM Employee_Summary
GROUP BY department, salary_grade
ORDER BY department, salary_grade;