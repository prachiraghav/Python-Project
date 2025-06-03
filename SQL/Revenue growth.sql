--month on month Revenue growth of products
with R as (
    select ProductID,
    sum(PricePerUnit * Quantity) as Revenue,  
    date_format(SaleDate, '%Y-%m' ) as YearMonth
    Extract(year_month,SaleDate ) as yml
    from Sales
    group by yml, ProductID
), 
WithPrevious as(
    select 
    current.ProductID,
    current.YearMonth ,
    current.Revenue,
    pre.revenue as PreviousRevenue
    round(((current.Revenue/pre.revenue)-1),4) as MoM_Growth
    from R as current
    left join R as pre 
    on current.ProductID = pre.ProductID and
    current.yml = pre.yml+1
)
SELECT 
    ProductID,
    YearMonth,
    Revenue,
    PreviousRevenue,
    MoM_Growth
FROM WithPrevious
WHERE PreviousRevenue IS NOT NULL


-- rolling averages or YTD growth per product

avg(Revenue)