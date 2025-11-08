# Student Management System - Relational Schema

## Complete Database Schema Documentation

---

## 📐 Formal Relational Schema Notation

### **1. Users**
```
Users(user_id, username, password, role, email, created_at)
  PK: user_id
  UK: username, email
  Constraints:
    - role ∈ {'admin', 'student', 'faculty'}
    - username NOT NULL
    - password NOT NULL
    - email NOT NULL
```

---

### **2. Students**
```
Students(student_id, user_id, first_name, last_name, date_of_birth, 
         gender, phone, address, enrollment_date, program, semester, status)
  PK: student_id
  FK: user_id → Users(user_id) [CASCADE DELETE]
  UK: user_id
  Constraints:
    - gender ∈ {'Male', 'Female', 'Other'}
    - status ∈ {'Active', 'Inactive', 'Graduated'} DEFAULT 'Active'
    - first_name NOT NULL
    - last_name NOT NULL
    - enrollment_date NOT NULL
```

**Functional Dependencies:**
- student_id → {user_id, first_name, last_name, date_of_birth, gender, phone, address, enrollment_date, program, semester, status}
- user_id → {student_id, first_name, last_name, ...}

---

### **3. Faculty**
```
Faculty(faculty_id, user_id, first_name, last_name, department, 
        phone, email, qualification, hire_date)
  PK: faculty_id
  FK: user_id → Users(user_id) [CASCADE DELETE]
  UK: user_id
  Constraints:
    - first_name NOT NULL
    - last_name NOT NULL
```

**Functional Dependencies:**
- faculty_id → {user_id, first_name, last_name, department, phone, email, qualification, hire_date}
- user_id → {faculty_id, first_name, last_name, ...}

---

### **4. Courses**
```
Courses(course_id, course_code, course_name, credits, department, semester, description)
  PK: course_id
  UK: course_code
  Constraints:
    - course_code NOT NULL
    - course_name NOT NULL
    - credits NOT NULL
```

**Functional Dependencies:**
- course_id → {course_code, course_name, credits, department, semester, description}
- course_code → {course_id, course_name, credits, ...}

---

### **5. Course_Assignment**
```
Course_Assignment(assignment_id, course_id, faculty_id, academic_year, semester)
  PK: assignment_id
  FK: course_id → Courses(course_id) [CASCADE DELETE]
  FK: faculty_id → Faculty(faculty_id) [SET NULL]
```

**Functional Dependencies:**
- assignment_id → {course_id, faculty_id, academic_year, semester}

**Business Rule:**
- A faculty member can teach multiple courses
- A course can be taught by multiple faculty members (different semesters/years)

---

### **6. Enrollment**
```
Enrollment(enrollment_id, student_id, course_id, enrollment_date, 
           academic_year, status)
  PK: enrollment_id
  FK: student_id → Students(student_id) [CASCADE DELETE]
  FK: course_id → Courses(course_id) [CASCADE DELETE]
  UK: (student_id, course_id, academic_year)
  Constraints:
    - enrollment_date NOT NULL
    - status ∈ {'Enrolled', 'Dropped', 'Completed'} DEFAULT 'Enrolled'
```

**Functional Dependencies:**
- enrollment_id → {student_id, course_id, enrollment_date, academic_year, status}
- (student_id, course_id, academic_year) → {enrollment_id, enrollment_date, status}

**Business Rule:**
- A student cannot enroll in the same course twice in the same academic year

---

### **7. Attendance**
```
Attendance(attendance_id, student_id, course_id, attendance_date, status, remarks)
  PK: attendance_id
  FK: student_id → Students(student_id) [CASCADE DELETE]
  FK: course_id → Courses(course_id) [CASCADE DELETE]
  Constraints:
    - attendance_date NOT NULL
    - status ∈ {'Present', 'Absent', 'Late'} NOT NULL
```

**Functional Dependencies:**
- attendance_id → {student_id, course_id, attendance_date, status, remarks}

**Business Rule:**
- Tracks daily attendance for each student in each course

---

### **8. Grades**
```
Grades(grade_id, student_id, course_id, assessment_type, marks_obtained, 
       max_marks, grade_letter, academic_year)
  PK: grade_id
  FK: student_id → Students(student_id) [CASCADE DELETE]
  FK: course_id → Courses(course_id) [CASCADE DELETE]
  Constraints:
    - assessment_type ∈ {'Assignment', 'Midterm', 'Final', 'Quiz', 'Project'} NOT NULL
```

**Functional Dependencies:**
- grade_id → {student_id, course_id, assessment_type, marks_obtained, max_marks, grade_letter, academic_year}

**Business Rule:**
- Multiple grades per student per course (different assessment types)

---

### **9. Fees**
```
Fees(fee_id, student_id, academic_year, semester, total_amount, 
     paid_amount, payment_date, status)
  PK: fee_id
  FK: student_id → Students(student_id) [CASCADE DELETE]
  Constraints:
    - total_amount NOT NULL
    - paid_amount DEFAULT 0
    - status ∈ {'Pending', 'Partial', 'Paid'} DEFAULT 'Pending'
```

**Functional Dependencies:**
- fee_id → {student_id, academic_year, semester, total_amount, paid_amount, payment_date, status}

**Business Rule:**
- Tracks fee payment status per semester

---

### **10. Announcements**
```
Announcements(announcement_id, title, content, posted_by, posted_date, target_audience)
  PK: announcement_id
  FK: posted_by → Users(user_id) [SET NULL]
  Constraints:
    - title NOT NULL
    - content NOT NULL
    - posted_date DEFAULT CURRENT_TIMESTAMP
    - target_audience ∈ {'All', 'Students', 'Faculty'} DEFAULT 'All'
```

**Functional Dependencies:**
- announcement_id → {title, content, posted_by, posted_date, target_audience}

---

### **11. Timetable**
```
Timetable(timetable_id, course_id, faculty_id, day_of_week, 
          start_time, end_time, room_number)
  PK: timetable_id
  FK: course_id → Courses(course_id) [CASCADE DELETE]
  FK: faculty_id → Faculty(faculty_id) [SET NULL]
  Constraints:
    - day_of_week ∈ {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'} NOT NULL
    - start_time NOT NULL
    - end_time NOT NULL
```

**Functional Dependencies:**
- timetable_id → {course_id, faculty_id, day_of_week, start_time, end_time, room_number}

---

## 🔑 Complete Schema with All Constraints

```sql
-- RELATIONAL SCHEMA DEFINITION

Users(user_id, username, password, role, email, created_at)
  PRIMARY KEY: user_id
  UNIQUE: username, email
  CHECK: role IN ('admin', 'student', 'faculty')

Students(student_id, user_id, first_name, last_name, date_of_birth, gender, 
         phone, address, enrollment_date, program, semester, status)
  PRIMARY KEY: student_id
  FOREIGN KEY: user_id REFERENCES Users(user_id) ON DELETE CASCADE
  UNIQUE: user_id
  CHECK: gender IN ('Male', 'Female', 'Other')
  CHECK: status IN ('Active', 'Inactive', 'Graduated')

Faculty(faculty_id, user_id, first_name, last_name, department, phone, 
        email, qualification, hire_date)
  PRIMARY KEY: faculty_id
  FOREIGN KEY: user_id REFERENCES Users(user_id) ON DELETE CASCADE
  UNIQUE: user_id

Courses(course_id, course_code, course_name, credits, department, semester, description)
  PRIMARY KEY: course_id
  UNIQUE: course_code

Course_Assignment(assignment_id, course_id, faculty_id, academic_year, semester)
  PRIMARY KEY: assignment_id
  FOREIGN KEY: course_id REFERENCES Courses(course_id) ON DELETE CASCADE
  FOREIGN KEY: faculty_id REFERENCES Faculty(faculty_id) ON DELETE SET NULL

Enrollment(enrollment_id, student_id, course_id, enrollment_date, academic_year, status)
  PRIMARY KEY: enrollment_id
  FOREIGN KEY: student_id REFERENCES Students(student_id) ON DELETE CASCADE
  FOREIGN KEY: course_id REFERENCES Courses(course_id) ON DELETE CASCADE
  UNIQUE: (student_id, course_id, academic_year)
  CHECK: status IN ('Enrolled', 'Dropped', 'Completed')

Attendance(attendance_id, student_id, course_id, attendance_date, status, remarks)
  PRIMARY KEY: attendance_id
  FOREIGN KEY: student_id REFERENCES Students(student_id) ON DELETE CASCADE
  FOREIGN KEY: course_id REFERENCES Courses(course_id) ON DELETE CASCADE
  CHECK: status IN ('Present', 'Absent', 'Late')

Grades(grade_id, student_id, course_id, assessment_type, marks_obtained, 
       max_marks, grade_letter, academic_year)
  PRIMARY KEY: grade_id
  FOREIGN KEY: student_id REFERENCES Students(student_id) ON DELETE CASCADE
  FOREIGN KEY: course_id REFERENCES Courses(course_id) ON DELETE CASCADE
  CHECK: assessment_type IN ('Assignment', 'Midterm', 'Final', 'Quiz', 'Project')

Fees(fee_id, student_id, academic_year, semester, total_amount, paid_amount, 
     payment_date, status)
  PRIMARY KEY: fee_id
  FOREIGN KEY: student_id REFERENCES Students(student_id) ON DELETE CASCADE
  CHECK: status IN ('Pending', 'Partial', 'Paid')

Announcements(announcement_id, title, content, posted_by, posted_date, target_audience)
  PRIMARY KEY: announcement_id
  FOREIGN KEY: posted_by REFERENCES Users(user_id) ON DELETE SET NULL
  CHECK: target_audience IN ('All', 'Students', 'Faculty')

Timetable(timetable_id, course_id, faculty_id, day_of_week, start_time, 
          end_time, room_number)
  PRIMARY KEY: timetable_id
  FOREIGN KEY: course_id REFERENCES Courses(course_id) ON DELETE CASCADE
  FOREIGN KEY: faculty_id REFERENCES Faculty(faculty_id) ON DELETE SET NULL
  CHECK: day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
```

---

## 📊 Referential Integrity Constraints

### **CASCADE DELETE:**
When parent is deleted, all child records are automatically deleted:

1. **Users → Students** (Delete user → Delete student profile)
2. **Users → Faculty** (Delete user → Delete faculty profile)
3. **Students → Enrollment** (Delete student → Delete enrollments)
4. **Students → Attendance** (Delete student → Delete attendance records)
5. **Students → Grades** (Delete student → Delete grade records)
6. **Students → Fees** (Delete student → Delete fee records)
7. **Courses → Enrollment** (Delete course → Delete enrollments)
8. **Courses → Course_Assignment** (Delete course → Delete assignments)
9. **Courses → Attendance** (Delete course → Delete attendance)
10. **Courses → Grades** (Delete course → Delete grades)
11. **Courses → Timetable** (Delete course → Delete timetable entries)

### **SET NULL:**
When parent is deleted, foreign key is set to NULL:

1. **Faculty → Course_Assignment** (faculty_id)
2. **Faculty → Timetable** (faculty_id)
3. **Users → Announcements** (posted_by)

---

## 🎯 Normalization Analysis

### **First Normal Form (1NF):** ✅
- All tables have atomic values
- No repeating groups
- Each column contains single values

### **Second Normal Form (2NF):** ✅
- All tables are in 1NF
- All non-key attributes fully dependent on primary key
- No partial dependencies

### **Third Normal Form (3NF):** ✅
- All tables are in 2NF
- No transitive dependencies
- All non-key attributes depend only on primary key

### **Boyce-Codd Normal Form (BCNF):** ✅
- All tables are in 3NF
- Every determinant is a candidate key

**Conclusion:** Database is fully normalized to BCNF

---

## 🔗 Dependency Diagram

```
                    ┌─────────────┐
                    │    Users    │
                    │   (PARENT)  │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
       ┌───────────┐ ┌──────────┐ ┌──────────────┐
       │ Students  │ │ Faculty  │ │Announcements │
       │  (CHILD)  │ │ (CHILD)  │ │   (CHILD)    │
       └─────┬─────┘ └────┬─────┘ └──────────────┘
             │            │
       ┌─────┼─────┐      │
       │     │     │      │
       ▼     ▼     ▼      ▼
    ┌────┐┌────┐┌────┐┌────────────────┐
    │Enr.││Att.││Grd.││Course_Assign   │
    │    ││    ││    ││                │
    └─┬──┘└─┬──┘└─┬──┘└───┬────────────┘
      │     │     │       │
      └─────┼─────┼───────┘
            │     │
            ▼     ▼
       ┌──────────────┐
       │   Courses    │
       │  (CENTRAL)   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │  Timetable   │
       └──────────────┘
```

---

## 📋 Complete Attribute List by Table

### **Table 1: Users** (6 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | user_id | INT | PK, AUTO_INCREMENT |
| 2 | username | VARCHAR(50) | UNIQUE, NOT NULL |
| 3 | password | VARCHAR(255) | NOT NULL |
| 4 | role | ENUM | NOT NULL |
| 5 | email | VARCHAR(100) | UNIQUE, NOT NULL |
| 6 | created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

---

### **Table 2: Students** (12 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | student_id | INT | PK, AUTO_INCREMENT |
| 2 | user_id | INT | FK, UNIQUE |
| 3 | first_name | VARCHAR(50) | NOT NULL |
| 4 | last_name | VARCHAR(50) | NOT NULL |
| 5 | date_of_birth | DATE | |
| 6 | gender | ENUM | |
| 7 | phone | VARCHAR(15) | |
| 8 | address | TEXT | |
| 9 | enrollment_date | DATE | NOT NULL |
| 10 | program | VARCHAR(100) | |
| 11 | semester | INT | |
| 12 | status | ENUM | DEFAULT 'Active' |

---

### **Table 3: Faculty** (9 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | faculty_id | INT | PK, AUTO_INCREMENT |
| 2 | user_id | INT | FK, UNIQUE |
| 3 | first_name | VARCHAR(50) | NOT NULL |
| 4 | last_name | VARCHAR(50) | NOT NULL |
| 5 | department | VARCHAR(100) | |
| 6 | phone | VARCHAR(15) | |
| 7 | email | VARCHAR(100) | |
| 8 | qualification | VARCHAR(100) | |
| 9 | hire_date | DATE | |

---

### **Table 4: Courses** (7 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | course_id | INT | PK, AUTO_INCREMENT |
| 2 | course_code | VARCHAR(20) | UNIQUE, NOT NULL |
| 3 | course_name | VARCHAR(100) | NOT NULL |
| 4 | credits | INT | NOT NULL |
| 5 | department | VARCHAR(100) | |
| 6 | semester | INT | |
| 7 | description | TEXT | |

---

### **Table 5: Course_Assignment** (5 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | assignment_id | INT | PK, AUTO_INCREMENT |
| 2 | course_id | INT | FK |
| 3 | faculty_id | INT | FK |
| 4 | academic_year | VARCHAR(20) | |
| 5 | semester | INT | |

---

### **Table 6: Enrollment** (6 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | enrollment_id | INT | PK, AUTO_INCREMENT |
| 2 | student_id | INT | FK |
| 3 | course_id | INT | FK |
| 4 | enrollment_date | DATE | NOT NULL |
| 5 | academic_year | VARCHAR(20) | |
| 6 | status | ENUM | DEFAULT 'Enrolled' |

---

### **Table 7: Attendance** (6 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | attendance_id | INT | PK, AUTO_INCREMENT |
| 2 | student_id | INT | FK |
| 3 | course_id | INT | FK |
| 4 | attendance_date | DATE | NOT NULL |
| 5 | status | ENUM | NOT NULL |
| 6 | remarks | TEXT | |

---

### **Table 8: Grades** (8 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | grade_id | INT | PK, AUTO_INCREMENT |
| 2 | student_id | INT | FK |
| 3 | course_id | INT | FK |
| 4 | assessment_type | ENUM | NOT NULL |
| 5 | marks_obtained | DECIMAL(5,2) | |
| 6 | max_marks | DECIMAL(5,2) | |
| 7 | grade_letter | VARCHAR(2) | |
| 8 | academic_year | VARCHAR(20) | |

---

### **Table 9: Fees** (8 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | fee_id | INT | PK, AUTO_INCREMENT |
| 2 | student_id | INT | FK |
| 3 | academic_year | VARCHAR(20) | |
| 4 | semester | INT | |
| 5 | total_amount | DECIMAL(10,2) | NOT NULL |
| 6 | paid_amount | DECIMAL(10,2) | DEFAULT 0 |
| 7 | payment_date | DATE | |
| 8 | status | ENUM | DEFAULT 'Pending' |

---

### **Table 10: Announcements** (6 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | announcement_id | INT | PK, AUTO_INCREMENT |
| 2 | title | VARCHAR(200) | NOT NULL |
| 3 | content | TEXT | NOT NULL |
| 4 | posted_by | INT | FK |
| 5 | posted_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| 6 | target_audience | ENUM | DEFAULT 'All' |

---

### **Table 11: Timetable** (7 attributes)
| # | Attribute | Type | Constraints |
|---|-----------|------|-------------|
| 1 | timetable_id | INT | PK, AUTO_INCREMENT |
| 2 | course_id | INT | FK |
| 3 | faculty_id | INT | FK |
| 4 | day_of_week | ENUM | NOT NULL |
| 5 | start_time | TIME | NOT NULL |
| 6 | end_time | TIME | NOT NULL |
| 7 | room_number | VARCHAR(20) | |

---

## 📊 Schema Statistics

| Metric | Count |
|--------|-------|
| Total Tables | 11 |
| Total Attributes | 80 |
| Primary Keys | 11 |
| Foreign Keys | 17 |
| Unique Constraints | 6 |
| ENUM Constraints | 8 |
| NOT NULL Constraints | 20 |
| DEFAULT Values | 6 |
| CASCADE DELETE | 10 |
| SET NULL | 3 |

---

## 🔍 Query Patterns

### **Common Queries:**

**1. Get Student with Courses:**
```sql
SELECT s.*, c.course_name, e.status
FROM Students s
JOIN Enrollment e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE s.student_id = ?
```

**2. Get Faculty Teaching Load:**
```sql
SELECT f.*, COUNT(ca.course_id) as course_count
FROM Faculty f
JOIN Course_Assignment ca ON f.faculty_id = ca.faculty_id
GROUP BY f.faculty_id
```

**3. Calculate Student Attendance Percentage:**
```sql
SELECT 
  (SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) / COUNT(*)) * 100 as percentage
FROM Attendance
WHERE student_id = ? AND course_id = ?
```

**4. Get Student GPA:**
```sql
SELECT AVG(marks_obtained / max_marks * 100) as gpa
FROM Grades
WHERE student_id = ?
```

---

## 🎓 Database Design Principles Applied

✅ **Entity Integrity** - All tables have primary keys  
✅ **Referential Integrity** - All foreign keys properly defined  
✅ **Domain Integrity** - ENUM and CHECK constraints  
✅ **Normalization** - Tables in BCNF  
✅ **Data Consistency** - UNIQUE constraints prevent duplicates  
✅ **Cascade Operations** - Automatic cleanup on deletions  
✅ **Null Handling** - NOT NULL where appropriate  
✅ **Semantic Naming** - Clear, descriptive names  

---

## 📐 Relational Algebra Operations

### **Selection (σ):**
```
σ(status='Active')(Students) - Select only active students
σ(role='faculty')(Users) - Select faculty users
```

### **Projection (π):**
```
π(first_name, last_name, email)(Students) - Get student names and emails
π(course_name, credits)(Courses) - Get course names and credits
```

### **Join (⋈):**
```
Students ⋈ Enrollment ⋈ Courses - Student course details
Faculty ⋈ Course_Assignment ⋈ Courses - Faculty teaching assignments
```

### **Aggregation:**
```
γ(student_id, COUNT(course_id))(Enrollment) - Courses per student
γ(course_id, AVG(marks_obtained))(Grades) - Average marks per course
```

---

## 🔐 Security & Integrity Rules

1. **Authentication Rule:** Every Student/Faculty must have a Users record
2. **Enrollment Rule:** Student can only enroll once per course per academic year
3. **Cascade Rule:** Deleting a user deletes all associated data
4. **Role Rule:** Users can only be admin, student, or faculty
5. **Status Rule:** Students can only be Active, Inactive, or Graduated
6. **Attendance Rule:** Status must be Present, Absent, or Late
7. **Fee Rule:** paid_amount cannot exceed total_amount (application level)
8. **Grade Rule:** marks_obtained cannot exceed max_marks (application level)

---

## 📈 Schema Evolution & Maintenance

### **Version History:**
- **v1.0** - Initial schema with 10 tables
- **v2.0** - Enhanced with improved UI/UX (Current)

### **Future Enhancements (Possible):**
- Add `fee_payments` table for payment history
- Add `course_materials` table for LMS
- Add `exam_schedule` table
- Add `student_attendance_summary` view

---

## 🎓 Created By: Enhanced Student Management System v2.0

**Repository:** https://github.com/sorathiyaom089/Student-Management-System.git  
**Database:** MySQL 8.2.0  
**Created:** November 8, 2025  
**Status:** Production Ready ✅

