CREATE TABLE IF NOT EXISTS ntw_users (
    userName TEXT NOT NULL,
    passw TEXT NOT NULL
);

CREATE INDEX user_index ON ntw_users(userName);