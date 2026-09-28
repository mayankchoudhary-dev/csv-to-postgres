-- Basic metrics

SELECT COUNT(*) AS total_orders
FROM sales;

SELECT SUM(total_amount) AS total_revenue
FROM sales;

SELECT SUM(quantity) AS total_quantity_sold
FROM sales;

SELECT AVG(total_amount) AS average_order_value
FROM sales;


-- Sales by city

SELECT
    city,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC;


-- Sales by product

SELECT
    product_id,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_sales
FROM sales
GROUP BY product_id
ORDER BY total_sales DESC;


-- Sales by date

SELECT
    order_date,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM sales
GROUP BY order_date
ORDER BY order_date;