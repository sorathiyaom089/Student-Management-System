DROP DATABASE IF EXISTS experiment_10;
CREATE DATABASE experiment_10;
USE experiment_10;

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    phone VARCHAR(15),
    city VARCHAR(30)
);

INSERT INTO Product (product_id, product_name, category, price, stock_quantity) VALUES
(1, 'Laptop', 'Electronics', 55000, 50),
(2, 'Mouse', 'Electronics', 500, 200),
(3, 'Keyboard', 'Electronics', 1500, 150),
(4, 'Monitor', 'Electronics', 12000, 75),
(5, 'Desk Chair', 'Furniture', 8000, 40),
(6, 'Desk', 'Furniture', 15000, 30),
(7, 'Headphones', 'Electronics', 2500, 100),
(8, 'Webcam', 'Electronics', 3500, 60);

INSERT INTO Customer (customer_id, customer_name, email, phone, city) VALUES
(1, 'Amit Shah', 'amit@email.com', '9876543210', 'Mumbai'),
(2, 'Priya Desai', 'priya@email.com', '9876543211', 'Delhi'),
(3, 'Rahul Joshi', 'rahul@email.com', '9876543212', 'Bangalore'),
(4, 'Sneha Patil', 'sneha@email.com', '9876543213', 'Pune'),
(5, 'Vijay Nair', 'vijay@email.com', '9876543214', 'Chennai');

INSERT INTO Sales (product_id, quantity_sold, sale_date, total_amount) VALUES
(1, 2, '2025-10-01', 110000),
(2, 10, '2025-10-02', 5000),
(3, 5, '2025-10-03', 7500),
(4, 3, '2025-10-05', 36000),
(5, 2, '2025-10-07', 16000),
(1, 1, '2025-10-10', 55000),
(7, 4, '2025-10-12', 10000),
(8, 2, '2025-10-15', 7000);

DELIMITER //
CREATE PROCEDURE GetAllProducts()
BEGIN
    SELECT * FROM Product;
END;//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetProductsByCategory(IN cat VARCHAR(30))
BEGIN
    SELECT * FROM Product WHERE category = cat;
END;//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateProductPrice(
    IN prod_id INT,
    IN new_price DECIMAL(10,2)
)
BEGIN
    UPDATE Product 
    SET price = new_price 
    WHERE product_id = prod_id;
END;//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AddNewProduct(
    IN p_id INT,
    IN p_name VARCHAR(50),
    IN p_category VARCHAR(30),
    IN p_price DECIMAL(10,2),
    IN p_stock INT
)
BEGIN
    INSERT INTO Product (product_id, product_name, category, price, stock_quantity)
    VALUES (p_id, p_name, p_category, p_price, p_stock);
END;//
DELIMITER ;

DELIMITER //
CREATE FUNCTION CalculateDiscount(original_price DECIMAL(10,2), discount_percent INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE discounted_price DECIMAL(10,2);
    SET discounted_price = original_price - (original_price * discount_percent / 100);
    RETURN discounted_price;
END;//
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetTotalStock()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT SUM(stock_quantity) INTO total FROM Product;
    RETURN total;
END;//
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetProductCount(cat VARCHAR(30))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE count INT;
    SELECT COUNT(*) INTO count FROM Product WHERE category = cat;
    RETURN count;
END;//
DELIMITER ;

CALL GetAllProducts();

CALL GetProductsByCategory('Electronics');

CALL UpdateProductPrice(2, 550);

SELECT * FROM Product WHERE product_id = 2;

CALL AddNewProduct(9, 'USB Cable', 'Electronics', 300, 500);

SELECT * FROM Product WHERE product_id = 9;

SELECT product_name, price, CalculateDiscount(price, 10) AS discounted_price
FROM Product;

SELECT product_name, price, CalculateDiscount(price, 20) AS discounted_price
FROM Product
WHERE category = 'Electronics';

SELECT GetTotalStock() AS total_stock;

SELECT GetProductCount('Electronics') AS electronics_count;

SELECT GetProductCount('Furniture') AS furniture_count;

DELIMITER //
CREATE PROCEDURE GetSalesReport()
BEGIN
    SELECT p.product_name, p.category, 
           SUM(s.quantity_sold) AS total_sold,
           SUM(s.total_amount) AS total_revenue
    FROM Product p
    LEFT JOIN Sales s ON p.product_id = s.product_id
    GROUP BY p.product_id, p.product_name, p.category
    ORDER BY total_revenue DESC;
END;//
DELIMITER ;

CALL GetSalesReport();

DELIMITER //
CREATE FUNCTION GetAveragePrice(cat VARCHAR(30))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE avg_price DECIMAL(10,2);
    SELECT AVG(price) INTO avg_price FROM Product WHERE category = cat;
    RETURN avg_price;
END;//
DELIMITER ;

SELECT GetAveragePrice('Electronics') AS avg_electronics_price;

SELECT GetAveragePrice('Furniture') AS avg_furniture_price;