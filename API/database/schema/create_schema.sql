CREATE EXTENSION "uuid-ossp";

CREATE SCHEMA main;

CREATE TABLE IF NOT EXISTS ntw_salt (
    salt TEXT NOT NULL
);

INSERT INTO ntw_salt (salt) VALUES ('N3NosfLjZ8hPTIC3');

CREATE TABLE IF NOT EXISTS main.ntw_users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4 (),
    user_name TEXT UNIQUE NOT NULL,
    passw TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS main.share (
    from_user_id uuid NOT NULL,
    to_user_id uuid NOT NULL,
    directory TEXT NOT NULL,
    file_name TEXT,
    FOREIGN KEY (from_user_id) REFERENCES main.ntw_users (id),
    FOREIGN KEY (to_user_id) REFERENCES main.ntw_users (id)
);

CREATE INDEX user_index ON main.ntw_users(user_name);

CREATE USER manager;

GRANT USAGE ON SCHEMA main TO manager;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA main TO manager;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA main TO manager;

GRANT SELECT ON ntw_salt TO manager;