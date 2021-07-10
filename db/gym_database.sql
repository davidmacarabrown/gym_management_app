DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS class;


CREATE TABLE member(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
)

CREATE TABLE class (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255)
)

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    class_id REFERENCES class(id),
    member_id REFERENCES member(id)
)