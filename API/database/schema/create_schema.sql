CREATE SCHEMA main;

CREATE TABLE IF NOT EXISTS ntw_salt (
    salt TEXT NOT NULL
);

INSERT INTO ntw_salt (salt) VALUES ('N3NosfLjZ8hPTIC3');

CREATE TABLE IF NOT EXISTS main.ntw_users (
    id SERIAL PRIMARY KEY,
    user_name TEXT UNIQUE NOT NULL,
    passw TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS main.share (
    from_user TEXT NOT NULL,
    to_user TEXT NOT NULL,
    directory TEXT NOT NULL,
    file_name TEXT
);

CREATE INDEX user_index ON main.ntw_users(user_name);

CREATE USER manager;

GRANT USAGE ON SCHEMA main TO manager;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA main TO manager;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA main TO manager;

GRANT SELECT ON ntw_salt TO manager;