SELECT
  d.id,                                           -- one row per department
  SUM(CASE WHEN d.month = 'Jan' THEN d.revenue END) AS Jan_Revenue,  -- Jan revenue
  SUM(CASE WHEN d.month = 'Feb' THEN d.revenue END) AS Feb_Revenue,  -- Feb revenue
  SUM(CASE WHEN d.month = 'Mar' THEN d.revenue END) AS Mar_Revenue,  -- Mar revenue
  SUM(CASE WHEN d.month = 'Apr' THEN d.revenue END) AS Apr_Revenue,  -- Apr revenue
  SUM(CASE WHEN d.month = 'May' THEN d.revenue END) AS May_Revenue,  -- May revenue
  SUM(CASE WHEN d.month = 'Jun' THEN d.revenue END) AS Jun_Revenue,  -- Jun revenue
  SUM(CASE WHEN d.month = 'Jul' THEN d.revenue END) AS Jul_Revenue,  -- Jul revenue
  SUM(CASE WHEN d.month = 'Aug' THEN d.revenue END) AS Aug_Revenue,  -- Aug revenue
  SUM(CASE WHEN d.month = 'Sep' THEN d.revenue END) AS Sep_Revenue,  -- Sep revenue
  SUM(CASE WHEN d.month = 'Oct' THEN d.revenue END) AS Oct_Revenue,  -- Oct revenue
  SUM(CASE WHEN d.month = 'Nov' THEN d.revenue END) AS Nov_Revenue,  -- Nov revenue
  SUM(CASE WHEN d.month = 'Dec' THEN d.revenue END) AS Dec_Revenue   -- Dec revenue
FROM Department d                    -- source table with id, revenue, month
GROUP BY d.id;         