DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;


CREATE TABLE members(

    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id SERIAL PRIMARY KEY

);

CREATE TABLE classes (

    class_name VARCHAR(255),
    class_description TEXT,
    id SERIAL PRIMARY KEY

);

CREATE TABLE bookings (

    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
    
);