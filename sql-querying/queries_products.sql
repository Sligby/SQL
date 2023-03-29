-- Comments in SQL Start with dash-dash --
-- To add a product to the table:
INSERT INTO products (name, price, can_be_returned)
VALUES ('chair', 44.00, false);

-- INSERT INTO products (name, price, can_be_returned)
VALUES ('stool', 25.99, true);

-- INSERT INTO products (name, price, can_be_returned)
VALUES ('table', 124.00, false);

-- To display all of the rows and columns in the table:
SELECT * FROM products;

-- To display all of the names of the products:
SELECT name FROM products;

-- To display all of the names and prices of the products:
SELECT name, price FROM products;

-- To add a new product:
INSERT INTO products (name, price, can_be_returned)
VALUES ('lamp', 59.99, true);

-- To display only the products that can_be_returned:
SELECT * FROM products WHERE can_be_returned = true;

-- To display only the products that have a price less than 44.00:
SELECT * FROM products WHERE price < 44.00;

-- To display only the products that have a price in between 22.50 and 99.99:
SELECT * FROM products WHERE price BETWEEN 22.50 AND 99.99;

-- To update the prices of all products by reducing $20:
UPDATE products SET price = price - 20;

-- To remove all products whose price is less than $25:
DELETE FROM products WHERE price < 25.00;

-- To increase the price of remaining products by $20:
UPDATE products SET price = price + 20;

-- To update the database so that everything is returnable:
UPDATE products SET can_be_returned = true;-- There is a new company policy: everything is returnable. Update the database accordingly.