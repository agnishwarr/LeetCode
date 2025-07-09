# Write your MySQL query statement below
WITH OrderedBuys AS (
  SELECT stock_name, price,
         ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS rn
  FROM Stocks
  WHERE operation = 'Buy'
),
OrderedSells AS (
  SELECT stock_name, price,
         ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS rn
  FROM Stocks
  WHERE operation = 'Sell'
),
Paired AS (
  SELECT b.stock_name, s.price - b.price AS gain_loss
  FROM OrderedBuys b
  JOIN OrderedSells s
    ON b.stock_name = s.stock_name AND b.rn = s.rn
)
SELECT stock_name, SUM(gain_loss) AS capital_gain_loss
FROM Paired
GROUP BY stock_name;
