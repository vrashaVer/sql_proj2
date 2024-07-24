import sqlite3


def open_connection():
    connection = sqlite3.connect('data.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection,cursor):
    cursor.close()
    connection.close()


def add_products(cursor):
    cursor.execute("""
    INSERT INTO products (product_id, name, category, price) VALUES
    (1, 'iPhone 13', 'smartphones', 999.99),
    (2, 'Samsung Galaxy S21', 'smartphones', 799.99),
    (3, 'MacBook Pro', 'laptops', 1299.99),
    (4, 'Dell XPS 13', 'laptops', 999.99),
    (5, 'iPad Air', 'tablets', 599.99),
    (6, 'Samsung Galaxy Tab', 'tablets', 499.99),
    (7, 'Sony WH-1000XM4', 'headphones', 349.99),
    (8, 'Apple Watch Series 6', 'wearables', 399.99),
    (9, 'GoPro HERO9', 'action cameras', 299.99),
    (10, 'Amazon Echo', 'smart speakers', 99.99);
    """)
    result = cursor.execute("""
    SELECT product_id, name, category, price
    FROM products;
    """).fetchall()
    return result



def add_custumers(cursor):
    cursor.execute("""
    INSERT INTO customers (customer_id, first_name, last_name, email) VALUES
    (1, 'John', 'Doe', 'john.doe@example.com'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com'),
    (3, 'Emily', 'Johnson', 'emily.johnson@example.com'),
    (4, 'Michael', 'Williams', 'michael.williams@example.com'),
    (5, 'Sarah', 'Brown', 'sarah.brown@example.com'),
    (6, 'David', 'Jones', 'david.jones@example.com');
    """)
    result = cursor.execute("""
    SELECT customer_id, first_name, last_name, email
    FROM customers;
    """).fetchall()
    return result
   

def add_orders(cursor):
    cursor.execute(""" 
    INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES
    (1, 1, 1, 2, '2024-07-01'),
    (2, 1, 3, 1, '2024-07-02'),
    (3, 2, 2, 3, '2024-07-01'),
    (4, 2, 5, 1, '2024-07-03'),
    (5, 3, 6, 2, '2024-07-02'),
    (6, 4, 7, 1, '2024-07-01'),
    (7, 5, 8, 1, '2024-07-04'),
    (8, 6, 9, 1, '2024-07-02'),
    (9, 6, 10, 2, '2024-07-03');
    """)
    result = cursor.execute("""
    SELECT order_id, customer_id, product_id, quantity, order_date
    FROM orders;
    """).fetchall()
    return result

def get_total_sales(cursor):
    result = cursor.execute("""
    SELECT SUM(products.price * orders.quantity)
    FROM orders
    JOIN products ON orders.product_id = products.product_id;
    """).fetchone()
    return result

def get_count_of_orders(cursor):
    result = cursor.execute("""
    SELECT customers.first_name, customers.last_name, COUNT(orders.order_id) AS order_count
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_id;
    """).fetchall()
    return result

def get_average_order_value(cursor):
    result = cursor.execute("""
    SELECT AVG(order_totals.total)
    FROM (
        SELECT SUM(products.price * orders.quantity) AS total
        FROM orders
        JOIN products ON orders.product_id = products.product_id
        GROUP BY orders.order_id
    ) AS order_totals;  
    """).fetchone()   
    return result[0] if result[0] is not None else 0             

def get_the_most_popular_category(cursor):
    result = cursor.execute("""
    SELECT products.category
    FROM orders
    JOIN products ON orders.product_id = products.product_id
    GROUP BY products.category
    ORDER BY COUNT(orders.order_id)DESC
    LIMIT 1;
    """).fetchone()
    return result

def get_product_count_per_category(cursor):
    result = cursor.execute("""
    SELECT category, COUNT(product_id) 
    FROM products
    GROUP BY category;
    """).fetchall()
    return result

def update_smartphone_prices(cursor):
    cursor.execute("""
    UPDATE products
    SET price = price * 1.10
    WHERE category = 'smartphones';
    """)
    result = cursor.execute("""
    SELECT product_id, name, price
    FROM products
    WHERE category = 'smartphones';
    """).fetchall()
    return result
                            

