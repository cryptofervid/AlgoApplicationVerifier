DROP TABLE IF EXISTS application;
DROP TABLE IF EXISTS revision;

CREATE TABLE application (
    id INTEGER PRIMARY KEY,
    status TEXT
);

CREATE TABLE revision (
    commit_id TEXT PRIMARY KEY,
    application INTEGER NOT NULL,
    status TEXT,
    validation_time DATETIME,
    approval_url TEXT,
    clear_state_url TEXT,
    additional_info TEXT
);