CREATE TABLE IF NOT EXISTS ntw_salt (
    id SERIAL PRIMARY KEY, 
    salt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ntw_users (
    id SERIAL PRIMARY KEY,
    user_name TEXT UNIQUE NOT NULL,
    passw TEXT UNIQUE NOT NULL,
    salt_id INT REFERENCES ntw_salt(id)
);

CREATE INDEX user_index ON ntw_users(id);