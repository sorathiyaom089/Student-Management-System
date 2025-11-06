import sys
sys.path.append('C:/Coding/Student_Management_System/backend')
from database import DatabaseConnection

db = DatabaseConnection()

# Add more attendance records for student 1 (John Doe)
attendance_data = [
    # Course 3 (DBMS) - Good attendance (85%)
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
    
    # Course 4 (Operating Systems) - Warning level (65%)
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
    (1, 4, '2024-10-15', 'Present'),
    
    # Student 2 (Sarah) - Excellent attendance
    (2, 3, '2024-11-02', 'Present'),
    (2, 3, '2024-11-03', 'Present'),
    (2, 3, '2024-11-04', 'Present'),
    (2, 3, '2024-11-05', 'Present'),
    (2, 3, '2024-11-06', 'Present'),
    (2, 4, '2024-11-02', 'Present'),
    (2, 4, '2024-11-03', 'Present'),
    (2, 4, '2024-11-04', 'Present'),
    (2, 4, '2024-11-05', 'Present'),
    (2, 4, '2024-11-06', 'Present'),
    
    # Student 3 (Mike) - Average attendance
    (3, 1, '2024-11-02', 'Absent'),
    (3, 1, '2024-11-03', 'Present'),
    (3, 1, '2024-11-04', 'Present'),
    (3, 1, '2024-11-05', 'Absent'),
    (3, 1, '2024-11-06', 'Present'),
    (3, 5, '2024-11-01', 'Present'),
    (3, 5, '2024-11-02', 'Present'),
    (3, 5, '2024-11-03', 'Absent'),
    (3, 5, '2024-11-04', 'Present'),
    (3, 5, '2024-11-05', 'Present'),
    
    # Student 4 (Emma) - Good attendance
    (4, 3, '2024-11-02', 'Present'),
    (4, 3, '2024-11-03', 'Present'),
    (4, 3, '2024-11-04', 'Present'),
    (4, 3, '2024-11-05', 'Absent'),
    (4, 3, '2024-11-06', 'Present'),
    (4, 4, '2024-11-01', 'Present'),
    (4, 4, '2024-11-02', 'Present'),
    (4, 4, '2024-11-03', 'Present'),
    (4, 4, '2024-11-04', 'Present'),
    (4, 4, '2024-11-05', 'Present'),
]

try:
    count = 0
    for record in attendance_data:
        # Check if record already exists
        check_query = """
        SELECT * FROM Attendance 
        WHERE student_id = %s AND course_id = %s AND attendance_date = %s
        """
        existing = db.execute_query(check_query, (record[0], record[1], record[2]))
        
        if not existing:
            insert_query = """
            INSERT INTO Attendance (student_id, course_id, attendance_date, status)
            VALUES (%s, %s, %s, %s)
            """
            db.execute_query(insert_query, record)
            count += 1
            print(f"Added: Student {record[0]}, Course {record[1]}, Date {record[2]}, Status {record[3]}")
        else:
            print(f"Skipped (exists): Student {record[0]}, Course {record[1]}, Date {record[2]}")
    
    print(f"\n✅ Added {count} new attendance records successfully!")
    print("Now refresh your browser to see the updated attendance summary.")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
