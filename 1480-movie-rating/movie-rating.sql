WITH user_cnt AS (
  SELECT u.name,
         COUNT(*) AS c
  FROM MovieRating mr
  JOIN Users u ON u.user_id = mr.user_id
  GROUP BY u.name
),
/* CTE: avg rating per movie in Feb 2020 */
feb_avg AS (
  SELECT m.title,
         AVG(mr.rating) AS avg_r
  FROM MovieRating mr
  JOIN Movies m ON m.movie_id = mr.movie_id
  WHERE mr.created_at >= '2020-02-01'
    AND mr.created_at <  '2020-03-01'
  GROUP BY m.title
),
/* Top user, break ties by name */
top_user AS (
  SELECT name
  FROM user_cnt
  ORDER BY c DESC, name ASC
  LIMIT 1
),
/* Top movie in Feb 2020, break ties by title */
top_movie AS (
  SELECT title
  FROM feb_avg
  ORDER BY avg_r DESC, title ASC
  LIMIT 1
)
SELECT name AS results FROM top_user
UNION ALL
SELECT title AS results FROM top_movie;