DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    cost DECIMAL(10,2), 
    date DATE,
    monthly_recurring BOOLEAN,
    notes VARCHAR(510)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    transaction INT NOT NULL REFERENCES transactions(id),
    deactivated BOOLEAN
);

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    transaction INT NOT NULL REFERENCES transactions(id),
    deactivated BOOLEAN
);

CREATE TABLE goals (
    id SERIAL PRIMARY KEY, 
    monthly_take_home_pay DECIMAL(10,2), 
    savings_target DECIMAL(10,2), 
    savings_time_frame DATE
);
