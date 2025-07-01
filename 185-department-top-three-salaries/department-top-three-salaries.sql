# Write your MySQL query statement below
SELECT
    D.name AS Department,
    E.name AS Employee,
    E.salary AS Salary
FROM (
    SELECT
        departmentId,
        name,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
) E
JOIN Department D ON E.departmentId = D.id
WHERE E.salary_rank <= 3;
