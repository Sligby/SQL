DROP DATABASE IF EXISTS craigslist;

CREATE DATABASE craigslist;

CREATE TABLE user(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    region_id INTEGER REFERENCES region
);

CREATE TABLE region(
    id SERIAL PRIMARY KEY,
    region_name TEXT
);

CREATE TABLE category(
    id SERIAL PRIMARY KEY,
    category_name TEXT,    
    region_id INTEGER REFERENCES region

);

CREATE TABLE post(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user,
    category_id INTEGER REFERENCES category,
    post_location TEXT,
    title VARCHAR,
    contents VARCHAR,
    post_date INTEGER
);