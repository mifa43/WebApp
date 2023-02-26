CREATE TABLE IF NOT EXISTS registration (
    id SERIAL PRIMARY KEY,
    name varchar(45) NOT NULL,
    lastName varchar(45) NOT NULL,
    mail varchar(45) NOT NULL,
    phoneNumber varchar(15) NOT NULL,
    password varchar(15) NOT NULL
);