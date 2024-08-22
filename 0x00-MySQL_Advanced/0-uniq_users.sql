-- creates a table called users, contains these attributes: id, email, name
-- if the table exists it should not fail, and should be executed on any database
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
