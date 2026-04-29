-- USERS TABLE
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    role TEXT NOT NULL,
    points INTEGER DEFAULT 0,
    steps INTEGER DEFAULT 0,
    mood INTEGER DEFAULT 0,
    completed INTEGER DEFAULT 0
);

-- SAMPLE DATA
INSERT INTO users (username, role, points, steps, mood, completed) VALUES
('Sam', 'Admin', 120, 8000, 7, 1),
('Alex', 'User', 90, 6500, 6, 1),
('Jordan', 'User', 40, 3000, 4, 0),
('Taylor', 'User', 75, 5000, 8, 1),
('Riley', 'User', 55, 4200, 5, 0);