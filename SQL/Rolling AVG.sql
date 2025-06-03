--where we include rolling 3-month average revenue per product

WITH RevenuePerMonth AS (
  SELECT 
    ProductID,
    DATE_FORMAT(SaleDate, '%Y-%m') AS YearMonth,
    EXTRACT(YEAR_MONTH FROM SaleDate) AS ym_val,
    SUM(PricePerUnit * Quantity) AS Revenue
  FROM Sales
  GROUP BY ProductID, YearMonth, ym_val
),
RollingRevenue AS (
  SELECT 
    ProductID,
    YearMonth,
    Revenue,
    ROUND(
      AVG(Revenue) OVER (
        PARTITION BY ProductID 
        ORDER BY ym_val 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
      ), 2
    ) AS Rolling_3_Month_Avg
  FROM RevenuePerMonth
)
SELECT * 
FROM RollingRevenue;