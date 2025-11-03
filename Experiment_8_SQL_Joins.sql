DROP DATABASE IF EXISTS experiment_8;
CREATE DATABASE experiment_8;
USE experiment_8;

CREATE TABLE Student (
    sid VARCHAR(10) PRIMARY KEY,
    sname VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE `Match` (
    mid VARCHAR(10) PRIMARY KEY,
    mname VARCHAR(50) NOT NULL,
    venue VARCHAR(50) NOT NULL
);

CREATE TABLE Play (
    sid VARCHAR(10),
    mid VARCHAR(10),
    day DATE,
    PRIMARY KEY (sid, mid, day),
    FOREIGN KEY (sid) REFERENCES Student(sid),
    FOREIGN KEY (mid) REFERENCES `Match`(mid)
);

INSERT INTO Student (sid, sname, age) VALUES
('S001', 'Amit', 20),
('S002', 'Rahul', 22),
('S003', 'Priya', 21),
('S004', 'Neha', 19),
('S005', 'Vijay', 23),
('S006', 'Sneha', 20),
('S007', 'Karan', 22),
('S008', 'Pooja', 21);

INSERT INTO `Match` (mid, mname, venue) VALUES
('B10', 'Cricket Championship', 'Delhi'),
('B11', 'Football League', 'Mumbai'),
('B12', 'Basketball Tournament', 'Delhi'),
('B13', 'Volleyball Cup', 'Bangalore'),
('B14', 'Tennis Open', 'Mumbai'),
('B15', 'Hockey Championship', 'Delhi');

INSERT INTO Play (sid, mid, day) VALUES
('S001', 'B10', '2025-10-15'),
('S001', 'B11', '2025-10-16'),
('S002', 'B10', '2025-10-15'),
('S002', 'B12', '2025-10-15'),
('S003', 'B12', '2025-10-17'),
('S004', 'B13', '2025-10-18'),
('S005', 'B14', '2025-10-19'),
('S005', 'B15', '2025-10-19'),
('S006', 'B11', '2025-10-16'),
('S007', 'B15', '2025-10-20');

SELECT DISTINCT s.*
FROM Student s
INNER JOIN Play p ON s.sid = p.sid
WHERE p.mid = 'B10';

SELECT DISTINCT m.mname
FROM `Match` m
INNER JOIN Play p ON m.mid = p.mid
INNER JOIN Student s ON p.sid = s.sid
WHERE s.sname = 'Amit';

SELECT DISTINCT s.sname
FROM Student s
INNER JOIN Play p ON s.sid = p.sid
INNER JOIN `Match` m ON p.mid = m.mid
WHERE m.venue = 'Delhi';

SELECT DISTINCT s.sname
FROM Student s
INNER JOIN Play p ON s.sid = p.sid;

SELECT s.sid, s.sname
FROM Student s
INNER JOIN Play p ON s.sid = p.sid
GROUP BY s.sid, s.sname, p.day
HAVING COUNT(DISTINCT p.mid) >= 2;

SELECT DISTINCT s.sid
FROM Student s
INNER JOIN Play p ON s.sid = p.sid
INNER JOIN `Match` m ON p.mid = m.mid
WHERE m.venue IN ('Delhi', 'Mumbai');

SELECT AVG(age) AS average_age
FROM Student;

SELECT s.sid, s.sname, COUNT(p.mid) AS matches_played
FROM Student s
INNER JOIN Play p ON s.sid = p.sid
GROUP BY s.sid, s.sname
HAVING COUNT(p.mid) > 1;

SELECT m.venue, COUNT(DISTINCT m.mid) AS match_count
FROM `Match` m
GROUP BY m.venue
HAVING COUNT(DISTINCT m.mid) > 2;

SELECT m.mid, m.mname, COUNT(DISTINCT p.sid) AS player_count
FROM `Match` m
INNER JOIN Play p ON m.mid = p.mid
GROUP BY m.mid, m.mname
HAVING COUNT(DISTINCT p.sid) > 1;
