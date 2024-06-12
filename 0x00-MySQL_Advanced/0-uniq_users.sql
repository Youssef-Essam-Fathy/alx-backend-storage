--SQL script that creates a table users
CREATE TABLE users (
  id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
  );
