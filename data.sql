CREATE DATABASE demosql;
USE demosql ;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    MDP VARCHAR(255) NOT NULL
);
