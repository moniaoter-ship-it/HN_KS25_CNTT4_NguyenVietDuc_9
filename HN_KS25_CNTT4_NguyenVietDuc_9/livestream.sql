CREATE DATABASE IF NOT EXISTS livestream_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE livestream_db;

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    category_id INT NOT NULL,
    CONSTRAINT fk_products_category
        FOREIGN KEY (category_id)
        REFERENCES categories(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT chk_price CHECK (price > 0),
    CONSTRAINT chk_stock CHECK (stock_quantity >= 0)
);

INSERT IGNORE INTO categories (name, description) VALUES
('Thời trang', 'Sản phẩm thời trang'),
('Giày dép', 'Giày dép thể thao và thời trang'),
('Phụ kiện', 'Phụ kiện thời trang');

INSERT IGNORE INTO products
(sku, name, price, stock_quantity, category_id)
SELECT 'SP001', 'Áo thun livestream', 250000, 50, id
FROM categories WHERE name = 'Thời trang';

INSERT IGNORE INTO products
(sku, name, price, stock_quantity, category_id)
SELECT 'SP002', 'Quần jean', 450000, 30, id
FROM categories WHERE name = 'Thời trang';

INSERT IGNORE INTO products
(sku, name, price, stock_quantity, category_id)
SELECT 'SP003', 'Giày thể thao', 1200000, 20, id
FROM categories WHERE name = 'Giày dép';

INSERT IGNORE INTO products
(sku, name, price, stock_quantity, category_id)
SELECT 'SP004', 'Váy công sở', 680000, 15, id
FROM categories WHERE name = 'Thời trang';

INSERT IGNORE INTO products
(sku, name, price, stock_quantity, category_id)
SELECT 'SP005', 'Kính mát', 350000, 45, id
FROM categories WHERE name = 'Phụ kiện';
