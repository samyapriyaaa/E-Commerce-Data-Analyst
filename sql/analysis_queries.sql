SELECT SUM(Quantity * Price) AS TotalRevenue
FROM ecommerce_sales;

SELECT Category, SUM(Quantity * Price) AS Revenue
FROM ecommerce_sales
GROUP BY Category
ORDER BY Revenue DESC;

SELECT Product, SUM(Quantity * Price) AS Revenue
FROM ecommerce_sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

SELECT Customer, SUM(Quantity * Price) AS TotalSpent
FROM ecommerce_sales
GROUP BY Customer
ORDER BY TotalSpent DESC;
