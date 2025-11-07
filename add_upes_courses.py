import sys
sys.path.append('C:/Coding/Student_Management_System/backend')
from database import DatabaseConnection

db = DatabaseConnection()

# New courses to add based on UPES portal
new_courses = [
    # Code, Name, Credits, Department, Semester, Description
    ('CSEG2006_3', 'Discrete Mathematical Structures', 3, 'Computer Science', 3, 'Mathematical foundations for computer science'),
    ('CSEG2060_3', 'Operating Systems', 3, 'Computer Science', 3, 'Operating system concepts and design'),
    ('SOB20B001_3', 'Introduction to Management', 3, 'School of Business', 3, 'Fundamentals of management principles'),
    ('SLLS2001_0', 'Social Internship', 0, 'Liberal Studies', 3, 'Social internship program'),
    ('SOB20B002_3', 'Marketing Fundamentals', 3, 'School of Business', 3, 'Basic marketing concepts and strategies'),
    ('SFLS0003_2', 'Leading Conversations', 2, 'Liberal Studies', 3, 'Communication and leadership skills'),
    ('CSAI2018_3', 'Elements of AIML', 3, 'Computer Science', 3, 'Introduction to AI and Machine Learning'),
    ('CSEG2072_5', 'Database Management Systems', 5, 'Computer Science', 3, 'Database design and SQL'),
    ('CSEG3053_4', 'Design and Analysis of Algorithms', 4, 'Computer Science', 3, 'Algorithm design and complexity analysis'),
]

# Enroll student 1 (john.student) in all these courses
student_id = 1
academic_year = '2024-25'
enrollment_date = '2024-08-01'

try:
    # First, add courses that don't exist
    added_courses = 0
    for course_code, course_name, credits, department, semester, description in new_courses:
        # Check if course exists
        check_query = "SELECT course_id FROM Courses WHERE course_code = %s"
        existing = db.execute_query(check_query, (course_code,))
        
        if not existing:
            # Add new course
            insert_course = """
                INSERT INTO Courses (course_code, course_name, credits, department, semester, description)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            course_id = db.execute_query(insert_course, (course_code, course_name, credits, department, semester, description))
            print(f"✅ Added course: {course_code} - {course_name} (ID: {course_id})")
            added_courses += 1
        else:
            course_id = existing[0]['course_id']
            print(f"⏭️  Course exists: {course_code} - {course_name} (ID: {course_id})")
        
        # Enroll student in this course
        check_enrollment = """
            SELECT * FROM Enrollment 
            WHERE student_id = %s AND course_id = %s
        """
        enrolled = db.execute_query(check_enrollment, (student_id, course_id))
        
        if not enrolled:
            insert_enrollment = """
                INSERT INTO Enrollment (student_id, course_id, enrollment_date, academic_year, status)
                VALUES (%s, %s, %s, %s, 'Enrolled')
            """
            db.execute_query(insert_enrollment, (student_id, course_id, enrollment_date, academic_year))
            print(f"   📝 Enrolled student in {course_code}")
        else:
            print(f"   ⏭️  Already enrolled in {course_code}")
    
    # Assign faculty to courses (assign Dr. Lisa Johnson - faculty_id 2 to all)
    faculty_id = 2
    for course_code, _, _, _, _, _ in new_courses:
        course = db.execute_query("SELECT course_id FROM Courses WHERE course_code = %s", (course_code,))
        if course:
            course_id = course[0]['course_id']
            
            # Check if assignment exists
            check_assignment = """
                SELECT * FROM Course_Assignment 
                WHERE course_id = %s AND faculty_id = %s AND academic_year = %s
            """
            assigned = db.execute_query(check_assignment, (course_id, faculty_id, academic_year))
            
            if not assigned:
                insert_assignment = """
                    INSERT INTO Course_Assignment (course_id, faculty_id, academic_year, semester)
                    VALUES (%s, %s, %s, 3)
                """
                db.execute_query(insert_assignment, (course_id, faculty_id, academic_year))
                print(f"   👨‍🏫 Assigned faculty to {course_code}")
    
    print(f"\n✅ Success!")
    print(f"📚 Added {added_courses} new courses")
    print(f"📝 Student enrolled in {len(new_courses)} courses")
    print(f"💳 Total credits: {sum(c[2] for c in new_courses)}")
    print(f"\n🔄 Refresh the browser to see updated courses!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
