DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;


CREATE TABLE members(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    class_description TEXT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE
);