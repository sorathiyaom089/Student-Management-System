-- Additional Attendance Data for Better Widget Display
USE student_management_system;

-- Add more attendance records for student 1 (John Doe) for courses 3 and 4
INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
-- Course 3 (DBMS) - Good attendance (85%)
(1, 3, '2024-11-03', 'Present'),
(1, 3, '2024-11-04', 'Present'),
(1, 3, '2024-11-05', 'Present'),
(1, 3, '2024-11-06', 'Present'),
(1, 3, '2024-10-28', 'Present'),
(1, 3, '2024-10-29', 'Present'),
(1, 3, '2024-10-30', 'Present'),
(1, 3, '2024-10-31', 'Present'),
(1, 3, '2024-10-25', 'Present'),
(1, 3, '2024-10-24', 'Absent'),
(1, 3, '2024-10-23', 'Present'),
(1, 3, '2024-10-22', 'Present'),
(1, 3, '2024-10-21', 'Present'),
(1, 3, '2024-10-18', 'Present'),
(1, 3, '2024-10-17', 'Absent'),
(1, 3, '2024-10-16', 'Present'),
(1, 3, '2024-10-15', 'Present'),
(1, 3, '2024-10-14', 'Present'),

-- Course 4 (Operating Systems) - Warning level (65%)
(1, 4, '2024-11-02', 'Absent'),
(1, 4, '2024-11-03', 'Present'),
(1, 4, '2024-11-04', 'Present'),
(1, 4, '2024-11-05', 'Absent'),
(1, 4, '2024-11-06', 'Present'),
(1, 4, '2024-10-28', 'Present'),
(1, 4, '2024-10-29', 'Absent'),
(1, 4, '2024-10-30', 'Present'),
(1, 4, '2024-10-31', 'Present'),
(1, 4, '2024-10-25', 'Present'),
(1, 4, '2024-10-24', 'Absent'),
(1, 4, '2024-10-23', 'Present'),
(1, 4, '2024-10-22', 'Absent'),
(1, 4, '2024-10-21', 'Present'),
(1, 4, '2024-10-18', 'Present'),
(1, 4, '2024-10-17', 'Absent'),
(1, 4, '2024-10-16', 'Present'),
(1, 4, '2024-10-15', 'Present');

-- Add attendance for other students too
-- Student 2 (Sarah) - Excellent attendance
INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
(2, 3, '2024-11-02', 'Present'),
(2, 3, '2024-11-03', 'Present'),
(2, 3, '2024-11-04', 'Present'),
(2, 3, '2024-11-05', 'Present'),
(2, 3, '2024-11-06', 'Present'),
(2, 4, '2024-11-02', 'Present'),
(2, 4, '2024-11-03', 'Present'),
(2, 4, '2024-11-04', 'Present'),
(2, 4, '2024-11-05', 'Present'),
(2, 4, '2024-11-06', 'Present');

-- Student 3 (Mike) - Average attendance
INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
(3, 1, '2024-11-02', 'Absent'),
(3, 1, '2024-11-03', 'Present'),
(3, 1, '2024-11-04', 'Present'),
(3, 1, '2024-11-05', 'Absent'),
(3, 1, '2024-11-06', 'Present'),
(3, 5, '2024-11-01', 'Present'),
(3, 5, '2024-11-02', 'Present'),
(3, 5, '2024-11-03', 'Absent'),
(3, 5, '2024-11-04', 'Present'),
(3, 5, '2024-11-05', 'Present');

-- Student 4 (Emma) - Good attendance
INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
(4, 3, '2024-11-02', 'Present'),
(4, 3, '2024-11-03', 'Present'),
(4, 3, '2024-11-04', 'Present'),
(4, 3, '2024-11-05', 'Absent'),
(4, 3, '2024-11-06', 'Present'),
(4, 4, '2024-11-01', 'Present'),
(4, 4, '2024-11-02', 'Present'),
(4, 4, '2024-11-03', 'Present'),
(4, 4, '2024-11-04', 'Present'),
(4, 4, '2024-11-05', 'Present');
