CREATE TABLE IF NOT EXISTS ntw_users (
    id          INT PRIMARY KEY,
    userName    TEXT UNIQUE NOT NULL,
    passw       TEXT UNIQUE NOT NULL
);

CREATE INDEX user_index ON ntw_users(id);