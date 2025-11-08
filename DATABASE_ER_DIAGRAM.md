# Student Management System - ER Diagram

## Database Schema Overview

The Student Management System uses **10 interconnected tables** to manage students, faculty, courses, attendance, grades, fees, and more.

---

## 📊 ER Diagram (Mermaid Format)

```mermaid
erDiagram
    Users ||--o| Students : "has"
    Users ||--o| Faculty : "has"
    Users ||--o{ Announcements : "posts"
    
    Students ||--o{ Enrollment : "enrolls in"
    Students ||--o{ Attendance : "has"
    Students ||--o{ Grades : "receives"
    Students ||--o{ Fees : "pays"
    
    Courses ||--o{ Enrollment : "has"
    Courses ||--o{ Course_Assignment : "assigned to"
    Courses ||--o{ Attendance : "tracks"
    Courses ||--o{ Grades : "evaluates"
    Courses ||--o{ Timetable : "scheduled"
    
    Faculty ||--o{ Course_Assignment : "teaches"
    Faculty ||--o{ Timetable : "scheduled"
    
    Users {
        int user_id PK
        varchar username UK
        varchar password
        enum role
        varchar email UK
        timestamp created_at
    }
    
    Students {
        int student_id PK
        int user_id FK_UK
        varchar first_name
        varchar last_name
        date date_of_birth
        enum gender
        varchar phone
        text address
        date enrollment_date
        varchar program
        int semester
        enum status
    }
    
    Faculty {
        int faculty_id PK
        int user_id FK_UK
        varchar first_name
        varchar last_name
        varchar department
        varchar phone
        varchar email
        varchar qualification
        date hire_date
    }
    
    Courses {
        int course_id PK
        varchar course_code UK
        varchar course_name
        int credits
        varchar department
        int semester
        text description
    }
    
    Course_Assignment {
        int assignment_id PK
        int course_id FK
        int faculty_id FK
        varchar academic_year
        int semester
    }
    
    Enrollment {
        int enrollment_id PK
        int student_id FK
        int course_id FK
        date enrollment_date
        varchar academic_year
        enum status
    }
    
    Attendance {
        int attendance_id PK
        int student_id FK
        int course_id FK
        date attendance_date
        enum status
        text remarks
    }
    
    Grades {
        int grade_id PK
        int student_id FK
        int course_id FK
        enum assessment_type
        decimal marks_obtained
        decimal max_marks
        varchar grade_letter
        varchar academic_year
    }
    
    Fees {
        int fee_id PK
        int student_id FK
        varchar academic_year
        int semester
        decimal total_amount
        decimal paid_amount
        date payment_date
        enum status
    }
    
    Announcements {
        int announcement_id PK
        varchar title
        text content
        int posted_by FK
        timestamp posted_date
        enum target_audience
    }
    
    Timetable {
        int timetable_id PK
        int course_id FK
        int faculty_id FK
        enum day_of_week
        time start_time
        time end_time
        varchar room_number
    }
```

---

## 📋 Table Descriptions

### 1. **Users** 👤
**Purpose:** Central authentication table for all system users

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| user_id | INT | PK, AUTO_INCREMENT | Unique user identifier |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Login username |
| password | VARCHAR(255) | NOT NULL | Hashed password |
| role | ENUM | NOT NULL | User role: admin, student, faculty |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Email address |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation date |

**Relationships:**
- One-to-One with Students
- One-to-One with Faculty
- One-to-Many with Announcements

---

### 2. **Students** 👨‍🎓
**Purpose:** Stores detailed student information

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| student_id | INT | PK, AUTO_INCREMENT | Unique student identifier |
| user_id | INT | FK, UNIQUE | Reference to Users table |
| first_name | VARCHAR(50) | NOT NULL | Student's first name |
| last_name | VARCHAR(50) | NOT NULL | Student's last name |
| date_of_birth | DATE | | Birth date |
| gender | ENUM | | Male, Female, Other |
| phone | VARCHAR(15) | | Contact number |
| address | TEXT | | Residential address |
| enrollment_date | DATE | NOT NULL | Date of enrollment |
| program | VARCHAR(100) | | Program/Degree name |
| semester | INT | | Current semester |
| status | ENUM | DEFAULT 'Active' | Active, Inactive, Graduated |

**Relationships:**
- Many-to-One with Users
- One-to-Many with Enrollment
- One-to-Many with Attendance
- One-to-Many with Grades
- One-to-Many with Fees

---

### 3. **Faculty** 👨‍🏫
**Purpose:** Stores faculty member information

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| faculty_id | INT | PK, AUTO_INCREMENT | Unique faculty identifier |
| user_id | INT | FK, UNIQUE | Reference to Users table |
| first_name | VARCHAR(50) | NOT NULL | Faculty's first name |
| last_name | VARCHAR(50) | NOT NULL | Faculty's last name |
| department | VARCHAR(100) | | Department name |
| phone | VARCHAR(15) | | Contact number |
| email | VARCHAR(100) | | Email address |
| qualification | VARCHAR(100) | | Educational qualification |
| hire_date | DATE | | Date of joining |

**Relationships:**
- Many-to-One with Users
- One-to-Many with Course_Assignment
- One-to-Many with Timetable

---

### 4. **Courses** 📚
**Purpose:** Stores course information

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| course_id | INT | PK, AUTO_INCREMENT | Unique course identifier |
| course_code | VARCHAR(20) | UNIQUE, NOT NULL | Course code (e.g., CS101) |
| course_name | VARCHAR(100) | NOT NULL | Full course name |
| credits | INT | NOT NULL | Credit hours |
| department | VARCHAR(100) | | Offering department |
| semester | INT | | Recommended semester |
| description | TEXT | | Course description |

**Relationships:**
- One-to-Many with Enrollment
- One-to-Many with Course_Assignment
- One-to-Many with Attendance
- One-to-Many with Grades
- One-to-Many with Timetable

---

### 5. **Course_Assignment** 🎓
**Purpose:** Links faculty to courses they teach

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| assignment_id | INT | PK, AUTO_INCREMENT | Unique assignment identifier |
| course_id | INT | FK | Reference to Courses |
| faculty_id | INT | FK | Reference to Faculty |
| academic_year | VARCHAR(20) | | Academic year (e.g., 2024-25) |
| semester | INT | | Semester number |

**Relationships:**
- Many-to-One with Courses
- Many-to-One with Faculty

---

### 6. **Enrollment** 📝
**Purpose:** Tracks student course enrollments

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| enrollment_id | INT | PK, AUTO_INCREMENT | Unique enrollment identifier |
| student_id | INT | FK | Reference to Students |
| course_id | INT | FK | Reference to Courses |
| enrollment_date | DATE | NOT NULL | Date of enrollment |
| academic_year | VARCHAR(20) | | Academic year |
| status | ENUM | DEFAULT 'Enrolled' | Enrolled, Dropped, Completed |

**Unique Constraint:** (student_id, course_id, academic_year)

**Relationships:**
- Many-to-One with Students
- Many-to-One with Courses

---

### 7. **Attendance** ✅
**Purpose:** Records student attendance for each course

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| attendance_id | INT | PK, AUTO_INCREMENT | Unique attendance record ID |
| student_id | INT | FK | Reference to Students |
| course_id | INT | FK | Reference to Courses |
| attendance_date | DATE | NOT NULL | Date of attendance |
| status | ENUM | NOT NULL | Present, Absent, Late |
| remarks | TEXT | | Additional notes |

**Relationships:**
- Many-to-One with Students
- Many-to-One with Courses

---

### 8. **Grades** 📊
**Purpose:** Stores student assessment grades

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| grade_id | INT | PK, AUTO_INCREMENT | Unique grade record ID |
| student_id | INT | FK | Reference to Students |
| course_id | INT | FK | Reference to Courses |
| assessment_type | ENUM | NOT NULL | Assignment, Midterm, Final, Quiz, Project |
| marks_obtained | DECIMAL(5,2) | | Marks scored |
| max_marks | DECIMAL(5,2) | | Maximum possible marks |
| grade_letter | VARCHAR(2) | | Letter grade (A, B, C, etc.) |
| academic_year | VARCHAR(20) | | Academic year |

**Relationships:**
- Many-to-One with Students
- Many-to-One with Courses

---

### 9. **Fees** 💰
**Purpose:** Manages student fee payments

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| fee_id | INT | PK, AUTO_INCREMENT | Unique fee record ID |
| student_id | INT | FK | Reference to Students |
| academic_year | VARCHAR(20) | | Academic year |
| semester | INT | | Semester number |
| total_amount | DECIMAL(10,2) | NOT NULL | Total fee amount |
| paid_amount | DECIMAL(10,2) | DEFAULT 0 | Amount paid |
| payment_date | DATE | | Date of payment |
| status | ENUM | DEFAULT 'Pending' | Pending, Partial, Paid |

**Relationships:**
- Many-to-One with Students

---

### 10. **Announcements** 📢
**Purpose:** System-wide announcements and notices

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| announcement_id | INT | PK, AUTO_INCREMENT | Unique announcement ID |
| title | VARCHAR(200) | NOT NULL | Announcement title |
| content | TEXT | NOT NULL | Announcement content |
| posted_by | INT | FK | Reference to Users |
| posted_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Posting date |
| target_audience | ENUM | DEFAULT 'All' | All, Students, Faculty |

**Relationships:**
- Many-to-One with Users

---

### 11. **Timetable** 🕐
**Purpose:** Course scheduling and timetable management

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| timetable_id | INT | PK, AUTO_INCREMENT | Unique timetable entry ID |
| course_id | INT | FK | Reference to Courses |
| faculty_id | INT | FK | Reference to Faculty |
| day_of_week | ENUM | NOT NULL | Monday through Saturday |
| start_time | TIME | NOT NULL | Class start time |
| end_time | TIME | NOT NULL | Class end time |
| room_number | VARCHAR(20) | | Classroom/room number |

**Relationships:**
- Many-to-One with Courses
- Many-to-One with Faculty

---

## 🔗 Relationship Summary

### **One-to-One Relationships:**
1. **Users ↔ Students** (1:1)
2. **Users ↔ Faculty** (1:1)

### **One-to-Many Relationships:**
1. **Users → Announcements** (1:N)
2. **Students → Enrollment** (1:N)
3. **Students → Attendance** (1:N)
4. **Students → Grades** (1:N)
5. **Students → Fees** (1:N)
6. **Courses → Enrollment** (1:N)
7. **Courses → Course_Assignment** (1:N)
8. **Courses → Attendance** (1:N)
9. **Courses → Grades** (1:N)
10. **Courses → Timetable** (1:N)
11. **Faculty → Course_Assignment** (1:N)
12. **Faculty → Timetable** (1:N)

### **Many-to-Many Relationships (via Junction Tables):**
1. **Students ↔ Courses** (M:N via Enrollment)
2. **Faculty ↔ Courses** (M:N via Course_Assignment)

---

## 🎯 Key Design Features

### **Cascading Deletes:**
- Deleting a User automatically deletes associated Student/Faculty records
- Deleting a Student automatically removes Enrollments, Attendance, Grades, and Fees
- Deleting a Course automatically removes all related records

### **Referential Integrity:**
- All foreign keys properly defined
- SET NULL on some relationships (e.g., posted_by in Announcements)
- Unique constraints on critical combinations

### **Data Types:**
- **ENUM** for predefined values (roles, status, gender)
- **DECIMAL** for precise financial calculations
- **TEXT** for long descriptions
- **TIMESTAMP** for automatic date tracking

---

## 📈 Cardinality Details

```
Users (1) ──────── (1) Students
Users (1) ──────── (1) Faculty
Users (1) ──────── (N) Announcements

Students (1) ────── (N) Enrollment
Students (1) ────── (N) Attendance
Students (1) ────── (N) Grades
Students (1) ────── (N) Fees

Courses (1) ─────── (N) Enrollment
Courses (1) ─────── (N) Course_Assignment
Courses (1) ─────── (N) Attendance
Courses (1) ─────── (N) Grades
Courses (1) ─────── (N) Timetable

Faculty (1) ─────── (N) Course_Assignment
Faculty (1) ─────── (N) Timetable

Students (M) ────── (N) Courses [via Enrollment]
Faculty (M) ─────── (N) Courses [via Course_Assignment]
```

---

## 🗂️ Table Categories

### **Authentication & Authorization:**
- Users

### **Core Entities:**
- Students
- Faculty
- Courses

### **Academic Operations:**
- Enrollment
- Course_Assignment
- Attendance
- Grades
- Timetable

### **Financial Management:**
- Fees

### **Communication:**
- Announcements

---

## 📊 Database Statistics

- **Total Tables:** 11
- **Total Relationships:** 17
- **Primary Keys:** 11
- **Foreign Keys:** 17
- **Unique Constraints:** 4
- **ENUM Fields:** 8
- **Cascade Deletes:** 10

---

## 🔐 Security Features

1. **Role-Based Access Control** via Users.role
2. **Cascade Deletes** for data integrity
3. **Unique Constraints** prevent duplicates
4. **NOT NULL** constraints for critical fields
5. **Foreign Key Constraints** maintain referential integrity

---

## 💡 Use Cases Supported

✅ **Student Management** - Enrollment, grades, attendance tracking  
✅ **Faculty Management** - Course assignments, teaching schedules  
✅ **Course Management** - Curriculum, credits, departments  
✅ **Attendance Tracking** - Daily attendance with status  
✅ **Grade Management** - Multiple assessment types  
✅ **Fee Collection** - Payment tracking and status  
✅ **Timetable Scheduling** - Class schedules by day/time  
✅ **Announcements** - Targeted communication  

---

## 🎓 Created By: Enhanced Student Management System v2.0

**Repository:** https://github.com/sorathiyaom089/Student-Management-System.git

