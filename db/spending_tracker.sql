DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cost FLOAT, 
    date DATE,
);