DROP DATABASE IF EXISTS rsl;

CREATE DATABASE rsl;

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    team_name VARCHAR,
    team_rank INTEGER

);

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    player_name VARCHAR,
    team_id INTEGER REFERENCES teams
);

CREATE TABLE seasons(
    id SERIAL PRIMARY KEY,
    season_start INTEGER,
    season_end INTEGER,
    champion VARCHAR CHECK (highest)
);

CREATE TABLE games(
    id SERIAL PRIMARY KEY,
    t1_id INTEGER REFERENCES teams,
    t2_id INTEGER REFERENCES teams,
    game_date VARCHAR,
    referee VARCHAR,
    winner INTEGER REFERENCES teams
)

