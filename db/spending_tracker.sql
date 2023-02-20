DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS categories;


CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    deactivated BOOLEAN
);

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    deactivated BOOLEAN
);

CREATE TABLE goals (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    savings_target DECIMAL(10,2), 
    savings_time_frame DATE,
    saved_so_far DECIMAL(10,2)
);

CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    take_home_pay DECIMAL(10,2)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    cost DECIMAL(10,2), 
    date DATE,
    category_id INT NOT NULL REFERENCES categories(id),
    vendor_id INT NOT NULL REFERENCES vendors(id),
    monthly_recurring BOOLEAN,
    notes VARCHAR(510)
);