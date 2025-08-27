# Write your MySQL query statement below
WITH first_order AS (
  SELECT
    customer_id,
    order_date,
    customer_pref_delivery_date,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY order_date, delivery_id
    ) AS rn
  FROM Delivery
)
-- Compute percent of first orders that were immediate, rounded to 2 decimals
SELECT
  ROUND(AVG(IF(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM first_order
WHERE rn = 1;