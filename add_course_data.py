import sys
sys.path.append('C:/Coding/Student_Management_System/backend')
from database import DatabaseConnection

db = DatabaseConnection()

student_id = 1

# Course IDs and their target attendance percentages
courses_data = [
    (7, 'CSEG2006_3', 90),   # Discrete Mathematical Structures - 90%
    (8, 'CSEG2060_3', 75),   # Operating Systems - 75%
    (9, 'SOB20B001_3', 94.44),  # Introduction to Management - 94.44%
    (11, 'SOB20B002_3', 100),  # Marketing Fundamentals - 100%
    (12, 'SFLS0003_2', 100),  # Leading Conversations - 100%
    (13, 'CSAI2018_3', 90.48),  # Elements of AIML - 90.48%
    (14, 'CSEG2072_5', 85),   # Database Management Systems - 85%
    (15, 'CSEG3053_4', 88),   # Design and Analysis of Algorithms - 88%
]

# Grades for each course
grades_data = [
    (7, 85, 100),   # Discrete Mathematical Structures
    (8, 78, 100),   # Operating Systems
    (9, 92, 100),   # Introduction to Management
    (11, 88, 100),  # Marketing Fundamentals
    (12, 95, 100),  # Leading Conversations
    (13, 90, 100),  # Elements of AIML
    (14, 87, 100),  # Database Management Systems
    (15, 91, 100),  # Design and Analysis of Algorithms
]

try:
    attendance_count = 0
    grades_count = 0
    
    # Add attendance records
    for course_id, course_code, target_pct in courses_data:
        if course_id == 10:  # Skip Social Internship (0 credits)
            continue
            
        # Calculate how many classes needed
        total_classes = 20
        present_classes = int((target_pct / 100) * total_classes)
        absent_classes = total_classes - present_classes
        
        # Add attendance records
        import datetime
        base_date = datetime.date(2024, 10, 1)
        
        for i in range(total_classes):
            date = base_date + datetime.timedelta(days=i*2)  # Every 2 days
            status = 'Present' if i < present_classes else 'Absent'
            
            # Check if exists
            check = db.execute_query(
                "SELECT * FROM Attendance WHERE student_id = %s AND course_id = %s AND attendance_date = %s",
                (student_id, course_id, date)
            )
            
            if not check:
                db.execute_query(
                    "INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES (%s, %s, %s, %s)",
                    (student_id, course_id, date, status)
                )
                attendance_count += 1
        
        print(f"✅ Added attendance for {course_code}: {present_classes}/{total_classes} = {target_pct:.2f}%")
    
    # Add grades
    for course_id, marks_obtained, max_marks in grades_data:
        # Check if grade exists
        check = db.execute_query(
            "SELECT * FROM Grades WHERE student_id = %s AND course_id = %s",
            (student_id, course_id)
        )
        
        if not check:
            percentage = (marks_obtained / max_marks) * 100
            grade_letter = 'A+' if percentage >= 90 else 'A' if percentage >= 80 else 'B+' if percentage >= 75 else 'B'
            
            db.execute_query(
                """INSERT INTO Grades (student_id, course_id, assessment_type, marks_obtained, max_marks, grade_letter, academic_year)
                   VALUES (%s, %s, 'Midterm', %s, %s, %s, '2024-25')""",
                (student_id, course_id, marks_obtained, max_marks, grade_letter)
            )
            grades_count += 1
            print(f"✅ Added grade for course {course_id}: {marks_obtained}/{max_marks} = {percentage:.1f}% ({grade_letter})")
    
    print(f"\n✅ Success!")
    print(f"📊 Added {attendance_count} attendance records")
    print(f"📝 Added {grades_count} grade records")
    print(f"\n🔄 Refresh the dashboard to see updated data!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
