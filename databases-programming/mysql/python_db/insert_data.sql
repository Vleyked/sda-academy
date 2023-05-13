-- Insert sample data into the "users" table
INSERT INTO users (name)
VALUES
    ('Alice'),
    ('Bob'),
    ('Charlie'),
    ('Dave'),
    ('Eve');

-- Insert sample data into the "orders" table
INSERT INTO orders (user_id, status)
VALUES
    (1, 'completed'),
    (1, 'completed'),
    (2, 'pending'),
    (2, 'completed'),
    (3, 'completed'),
    (3, 'completed'),
    (3, 'pending'),
    (4, 'completed'),
    (4, 'completed'),
    (5, 'completed'),
    (5, 'completed'),
    (5, 'completed'),
    (5, 'pending');

-- Insert sample data into the "products" table
INSERT INTO products (name, price)
VALUES
    ('Product 1', 10.99),
    ('Product 2', 19.99),
    ('Product 3', 29.99),
    ('Product 4', 39.99),
    ('Product 5', 49.99);

-- Insert sample data into the "customers" table
INSERT INTO customers (name, email)
VALUES
    ('Customer 1', 'customer1@example.com'),
    ('Customer 2', 'customer2@example.com'),
    ('Customer 3', 'customer3@example.com'),
    ('Customer 4', 'customer4@example.com'),
    ('Customer 5', 'customer5@example.com');

-- Insert sample data into the "reviews" table
INSERT INTO reviews (product_id, user_id, rating, comment)
VALUES
    (1, 1, 4, 'This product was great!'),
    (1, 2, 3, 'Not bad, but could be better.'),
    (2, 2, 5, 'This product exceeded my expectations.'),
    (2, 3, 2, 'Not worth the money.'),
    (3, 3, 4, 'I would recommend this product.'),
    (3, 4, 3, 'It was okay, but nothing special.'),
    (3, 5, 5, 'This product was amazing!'),
    (4, 1, 1, 'I was very disappointed in this product.'),
    (4, 2, 2, 'It was not what I expected.'),
    (4, 4, 3, 'It was an okay product.'),
    (5, 1, 5, 'This product was fantastic!'),
    (5, 2, 4, 'I would recommend this product to others.'),
    (5, 3, 3, 'It was not worth the price.'),
    (5, 4, 2, 'I would not buy this product again.'),
    (5, 5, 1, 'This product was a complete waste of money.');
