SELECT id, visit_date, people
FROM (
    SELECT id, visit_date, people,
           IF(people >= 100, 1, 0) AS is_valid
    FROM Stadium
) AS s1
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               is_valid,
               LAG(is_valid, 1) OVER (ORDER BY id) AS prev1,
               LAG(is_valid, 2) OVER (ORDER BY id) AS prev2,
               LEAD(is_valid, 1) OVER (ORDER BY id) AS next1,
               LEAD(is_valid, 2) OVER (ORDER BY id) AS next2
        FROM (
            SELECT id, IF(people >= 100, 1, 0) AS is_valid
            FROM Stadium
        ) AS temp
    ) AS windowed
    WHERE 
        (is_valid = 1 AND next1 = 1 AND next2 = 1)
        OR (prev1 = 1 AND is_valid = 1 AND next1 = 1)
        OR (prev2 = 1 AND prev1 = 1 AND is_valid = 1)
)
ORDER BY visit_date;
