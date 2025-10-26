DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS scholarship;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE scholarship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    amount REAL,
    deadline DATE,
    status TEXT,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
