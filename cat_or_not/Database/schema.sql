DROP TABLE IF EXISTS analysis_history;
CREATE TABLE analysis_history(
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name VARCHAR (20),
    file_size INTEGER,
    analysis_status VARCHAR(20)
);