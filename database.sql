CREATE DATABASE option_pricer_db;
USE option_pricer_db;
CREATE TABLE calculation_input(
    calculationInputId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    stock_price DECIMAL(18,6) NOT NULL,
    strike_price DECIMAL(18,6) NOT NULL,
    time_to_maturity DECIMAL(10,6) NOT NULL,
    risk_free_rate DECIMAL(18,9) NOT NULL,
    dividend_yield DECIMAL(18,9) DEFAULT 0.0,
    option_type ENUM('Call','Put') NOT NULL,
    is_american BOOLEAN DEFAULT FALSE,
    steps INT DEFAULT 500,
    purchase_price DECIMAL(18,6) DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE calculation_output (
    calculationOutputId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    calcuationInputId INT NOT NULL,
    volatility_shock DECIMAL(18,9),
    stock_price_shock DECIMAL(18,6),
    option_price DECIMAL(18,9),
    PNL_VALUE DECIMAL(18,9),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (calculationInputId) REFERENCES calculation_input(calculationInputId)
)