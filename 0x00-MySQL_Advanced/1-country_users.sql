-- creates a table and adds another attribute: country

DROP TABLE IF EXISTS users;
CREATE TABLE users (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
	country VARCHAR(2) NOT NULL ENUM('CO', 'TN', 'US') DEFAULT = US
);
