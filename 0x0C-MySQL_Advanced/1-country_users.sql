-- create new user
CREATE TABLE IF NOT EXISTS users (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL 
    );
