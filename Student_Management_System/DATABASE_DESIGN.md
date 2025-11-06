# Database Design Documentation
## Student Management System - Complete ER Model & Relational Schema

**Version**: 2.0  
**Last Updated**: November 6, 2025  
**Database**: MySQL 8.0  
**Normalization Level**: Third Normal Form (3NF)

---

## Table of Contents
1. [Entity-Relationship (ER) Diagram](#er-diagram)
2. [Entities and Attributes](#entities-and-attributes)
3. [Relationships](#relationships)
4. [Relational Schema](#relational-schema)
5. [Table Structures](#table-structures)
6. [Constraints and Integrity](#constraints-and-integrity)
7. [Stored Procedures](#stored-procedures)
8. [Views](#views)
9. [Indexes](#indexes)
10. [Sample Queries](#sample-queries)

---

## 1. Entity-Relationship (ER) Diagram

### High-Level ER Diagram (Chen Notation)

```
                    ┌──────────────┐
                    │  Department  │
                    └──────┬───────┘
                           │
                           │ 1:N
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        │                  │                  │
    ┌───▼────┐        ┌───▼────┐        ┌────▼────┐
    │ Faculty│        │Student │        │ Course  │
    └───┬────┘        └───┬────┘        └────┬────┘
        │                 │                   │
        │                 │                   │
        │ N:M             │ N:M               │
        │ (teaches)       │ (enrolls)         │
        │                 │                   │
        └────────┬────────┴──────┬────────────┘
                 │               │
                 │               │
          ┌──────▼──────┐  ┌────▼─────┐
          │Course_      │  │Enrollment│
          │Assignment   │  └────┬─────┘
          └─────────────┘       │
                                │ 1:N
                                │
                    ┌───────────┼────────────┐
                    │           │            │
               ┌────▼───┐  ┌────▼────┐  ┌───▼────┐
               │Attendance│ │ Grades  │  │  Fees  │
               └──────────┘ └─────────┘  └───┬────┘
                                              │
                                              │ 1:N
                                              │
                                        ┌─────▼────────┐
                                        │Fee_Payments  │
                                        └──────────────┘

                    ┌──────────────┐
                    │    Users     │ (Authentication)
                    └──────┬───────┘
                           │
                           │ 1:1
                           │
                ┌──────────┼──────────┐
                │          │          │
            ┌───▼───┐  ┌───▼───┐  ┌──▼────┐
            │Student│  │Faculty│  │ Admin │
            └───────┘  └───────┘  └───────┘
```

### Detailed ER Diagram Components

#### Entities (Rectangles)
- **Users**: Authentication and role management
- **Students**: Student personal and academic information
- **Faculty**: Faculty personal and professional information
- **Courses**: Course catalog and details
- **Departments**: Academic department organization
- **Enrollment**: Student course registration
- **Attendance**: Daily attendance records
- **Grades**: Assessment and grade tracking
- **Fees**: Fee structure and amounts
- **Fee_Payments**: Payment transaction records
- **Course_Assignment**: Faculty course teaching assignments

#### Relationships (Diamonds)
- **manages**: Department → Faculty (1:N)
- **belongs_to**: Student → Department (N:1)
- **teaches**: Faculty ↔ Course (N:M via Course_Assignment)
- **enrolls_in**: Student ↔ Course (N:M via Enrollment)
- **has_attendance**: Enrollment → Attendance (1:N)
- **receives_grade**: Enrollment → Grades (1:N)
- **pays_fees**: Student → Fees (1:N)
- **makes_payment**: Fees → Fee_Payments (1:N)
- **authenticates**: User → (Student|Faculty|Admin) (1:1)

---

## 2. Entities and Attributes

### 2.1 Users Entity
**Purpose**: Centralized authentication for all user types

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **user_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Login username |
| password | VARCHAR(255) | NOT NULL | Hashed password |
| role | ENUM('student','faculty','admin') | NOT NULL | User role type |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation time |
| last_login | TIMESTAMP | NULL | Last login timestamp |

**Relationships**:
- 1:1 with Students (via user_id)
- 1:1 with Faculty (via user_id)
- 1:1 with Admin (via user_id)

---

### 2.2 Students Entity
**Purpose**: Store student personal and academic information

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **student_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique student ID |
| user_id | INT | FOREIGN KEY → Users(user_id) | Authentication link |
| first_name | VARCHAR(50) | NOT NULL | First name |
| last_name | VARCHAR(50) | NOT NULL | Last name |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Email address |
| phone | VARCHAR(15) | NULL | Contact number |
| date_of_birth | DATE | NULL | Birth date |
| gender | ENUM('Male','Female','Other') | NULL | Gender |
| address | TEXT | NULL | Residential address |
| city | VARCHAR(50) | NULL | City |
| state | VARCHAR(50) | NULL | State/Province |
| country | VARCHAR(50) | NULL | Country |
| program | VARCHAR(100) | NULL | Enrolled program |
| semester | INT | NULL | Current semester |
| enrollment_year | INT | NULL | Year of enrollment |
| department_id | INT | FOREIGN KEY → Departments(dept_id) | Department link |
| parent_name | VARCHAR(100) | NULL | Parent/Guardian name |
| parent_phone | VARCHAR(15) | NULL | Parent contact |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- N:1 with Departments
- 1:N with Enrollment
- 1:N with Fees
- 1:1 with Users

---

### 2.3 Faculty Entity
**Purpose**: Store faculty personal and professional information

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **faculty_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique faculty ID |
| user_id | INT | FOREIGN KEY → Users(user_id) | Authentication link |
| first_name | VARCHAR(50) | NOT NULL | First name |
| last_name | VARCHAR(50) | NOT NULL | Last name |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Email address |
| phone | VARCHAR(15) | NULL | Contact number |
| department_id | INT | FOREIGN KEY → Departments(dept_id) | Department link |
| designation | VARCHAR(100) | NULL | Job title/position |
| qualification | VARCHAR(100) | NULL | Highest degree |
| specialization | VARCHAR(100) | NULL | Area of expertise |
| date_of_joining | DATE | NULL | Joining date |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- N:1 with Departments
- N:M with Courses (via Course_Assignment)
- 1:1 with Users

---

### 2.4 Courses Entity
**Purpose**: Course catalog and course details

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **course_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique course ID |
| course_code | VARCHAR(20) | UNIQUE, NOT NULL | Course code (e.g., CS101) |
| course_name | VARCHAR(100) | NOT NULL | Full course name |
| credits | INT | NOT NULL, CHECK > 0 | Credit hours |
| department_id | INT | FOREIGN KEY → Departments(dept_id) | Offering department |
| semester | INT | NULL | Recommended semester |
| description | TEXT | NULL | Course description |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- N:1 with Departments
- N:M with Students (via Enrollment)
- N:M with Faculty (via Course_Assignment)

---

### 2.5 Departments Entity
**Purpose**: Academic department organization

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **dept_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique department ID |
| dept_name | VARCHAR(100) | UNIQUE, NOT NULL | Department name |
| dept_code | VARCHAR(20) | UNIQUE, NULL | Short code |
| head_faculty_id | INT | FOREIGN KEY → Faculty(faculty_id) | Department head |
| building | VARCHAR(50) | NULL | Building location |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- 1:N with Students
- 1:N with Faculty
- 1:N with Courses

---

### 2.6 Enrollment Entity (Junction Table)
**Purpose**: Link students to courses they are enrolled in

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **enrollment_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique enrollment ID |
| student_id | INT | FOREIGN KEY → Students(student_id) | Student reference |
| course_id | INT | FOREIGN KEY → Courses(course_id) | Course reference |
| enrollment_date | DATE | NOT NULL | Date of enrollment |
| status | ENUM('active','dropped','completed') | DEFAULT 'active' | Enrollment status |
| grade | VARCHAR(2) | NULL | Final grade (A+, A, B, etc.) |
| semester | INT | NULL | Semester enrolled |
| academic_year | VARCHAR(10) | NULL | Academic year (2024-25) |

**Composite Unique Key**: (student_id, course_id, semester)

**Relationships**:
- N:1 with Students
- N:1 with Courses
- 1:N with Attendance
- 1:N with Grades

---

### 2.7 Attendance Entity
**Purpose**: Daily attendance tracking

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **attendance_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique attendance ID |
| enrollment_id | INT | FOREIGN KEY → Enrollment(enrollment_id) | Enrollment reference |
| date | DATE | NOT NULL | Attendance date |
| status | ENUM('Present','Absent','Late','Excused') | NOT NULL | Attendance status |
| marked_by | INT | FOREIGN KEY → Faculty(faculty_id) | Faculty who marked |
| remarks | TEXT | NULL | Additional notes |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Composite Unique Key**: (enrollment_id, date)

**Relationships**:
- N:1 with Enrollment
- N:1 with Faculty (marked_by)

---

### 2.8 Grades Entity
**Purpose**: Assessment and grade management

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **grade_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique grade ID |
| enrollment_id | INT | FOREIGN KEY → Enrollment(enrollment_id) | Enrollment reference |
| assessment_type | ENUM('Quiz','Midterm','Final','Assignment','Project') | NOT NULL | Type of assessment |
| marks_obtained | DECIMAL(5,2) | NOT NULL, CHECK >= 0 | Marks scored |
| max_marks | DECIMAL(5,2) | NOT NULL, CHECK > 0 | Maximum marks |
| date | DATE | NULL | Assessment date |
| remarks | TEXT | NULL | Comments/feedback |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- N:1 with Enrollment

---

### 2.9 Fees Entity
**Purpose**: Fee structure and amounts

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **fee_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique fee ID |
| student_id | INT | FOREIGN KEY → Students(student_id) | Student reference |
| semester | INT | NOT NULL | Semester number |
| academic_year | VARCHAR(10) | NOT NULL | Academic year |
| tuition_fee | DECIMAL(10,2) | NOT NULL, CHECK >= 0 | Tuition amount |
| hostel_fee | DECIMAL(10,2) | DEFAULT 0.00 | Hostel charges |
| library_fee | DECIMAL(10,2) | DEFAULT 0.00 | Library charges |
| other_fees | DECIMAL(10,2) | DEFAULT 0.00 | Miscellaneous fees |
| total_amount | DECIMAL(10,2) | GENERATED, NOT NULL | Sum of all fees |
| due_date | DATE | NOT NULL | Payment deadline |
| status | ENUM('Pending','Partial','Paid') | DEFAULT 'Pending' | Payment status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Composite Unique Key**: (student_id, semester, academic_year)

**Relationships**:
- N:1 with Students
- 1:N with Fee_Payments

---

### 2.10 Fee_Payments Entity
**Purpose**: Payment transaction records

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **payment_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique payment ID |
| fee_id | INT | FOREIGN KEY → Fees(fee_id) | Fee reference |
| amount_paid | DECIMAL(10,2) | NOT NULL, CHECK > 0 | Payment amount |
| payment_date | DATE | NOT NULL | Date of payment |
| payment_method | ENUM('Cash','Card','UPI','NetBanking','Cheque') | NOT NULL | Payment mode |
| transaction_id | VARCHAR(100) | NULL | Transaction reference |
| remarks | TEXT | NULL | Payment notes |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Relationships**:
- N:1 with Fees

---

### 2.11 Course_Assignment Entity (Junction Table)
**Purpose**: Assign faculty to courses they teach

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| **assignment_id** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique assignment ID |
| faculty_id | INT | FOREIGN KEY → Faculty(faculty_id) | Faculty reference |
| course_id | INT | FOREIGN KEY → Courses(course_id) | Course reference |
| semester | INT | NOT NULL | Teaching semester |
| academic_year | VARCHAR(10) | NOT NULL | Academic year |
| room_number | VARCHAR(20) | NULL | Classroom |
| time_slot | VARCHAR(50) | NULL | Class timing |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation |

**Composite Unique Key**: (faculty_id, course_id, semester, academic_year)

**Relationships**:
- N:1 with Faculty
- N:1 with Courses

---

## 3. Relationships

### 3.1 One-to-One (1:1)

| Entity A | Entity B | Description |
|----------|----------|-------------|
| Users | Students | Each user account maps to one student |
| Users | Faculty | Each user account maps to one faculty |
| Users | Admin | Each user account maps to one admin |

### 3.2 One-to-Many (1:N)

| Parent Entity | Child Entity | Foreign Key | Description |
|---------------|--------------|-------------|-------------|
| Departments | Students | department_id | Department has many students |
| Departments | Faculty | department_id | Department has many faculty |
| Departments | Courses | department_id | Department offers many courses |
| Students | Enrollment | student_id | Student enrolls in many courses |
| Courses | Enrollment | course_id | Course has many enrollments |
| Enrollment | Attendance | enrollment_id | Enrollment has many attendance records |
| Enrollment | Grades | enrollment_id | Enrollment has many grade records |
| Students | Fees | student_id | Student has fees for multiple semesters |
| Fees | Fee_Payments | fee_id | Fee can have multiple payments |
| Faculty | Attendance | marked_by | Faculty marks attendance for students |

### 3.3 Many-to-Many (N:M)

| Entity A | Entity B | Junction Table | Description |
|----------|----------|----------------|-------------|
| Students | Courses | Enrollment | Students enroll in multiple courses |
| Faculty | Courses | Course_Assignment | Faculty teach multiple courses |

---

## 4. Relational Schema

### Functional Dependencies

#### Users
- user_id → {username, password, role, created_at, last_login}
- username → user_id

#### Students
- student_id → {user_id, first_name, last_name, email, phone, ...}
- user_id → student_id
- email → student_id

#### Faculty
- faculty_id → {user_id, first_name, last_name, email, phone, ...}
- user_id → faculty_id
- email → faculty_id

#### Courses
- course_id → {course_code, course_name, credits, department_id, ...}
- course_code → course_id

#### Enrollment
- enrollment_id → {student_id, course_id, enrollment_date, status, ...}
- (student_id, course_id, semester) → enrollment_id

### Normalization Analysis

**First Normal Form (1NF)**:
✅ All tables have atomic values
✅ No repeating groups
✅ All columns have unique names

**Second Normal Form (2NF)**:
✅ All non-key attributes fully depend on primary key
✅ No partial dependencies

**Third Normal Form (3NF)**:
✅ No transitive dependencies
✅ All non-key attributes depend only on primary key
✅ Example: `total_amount` in Fees is calculated (could be removed for strict 3NF)

---

## 5. Table Structures (SQL DDL)

### 5.1 Users Table
```sql
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('student', 'faculty', 'admin') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    INDEX idx_username (username),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.2 Departments Table
```sql
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) UNIQUE NOT NULL,
    dept_code VARCHAR(20) UNIQUE,
    head_faculty_id INT,
    building VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (head_faculty_id) REFERENCES Faculty(faculty_id) ON DELETE SET NULL,
    INDEX idx_dept_name (dept_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.3 Students Table
```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) DEFAULT 'India',
    program VARCHAR(100),
    semester INT,
    enrollment_year INT,
    department_id INT,
    parent_name VARCHAR(100),
    parent_phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (department_id) REFERENCES Departments(dept_id) ON DELETE SET NULL,
    INDEX idx_email (email),
    INDEX idx_dept (department_id),
    INDEX idx_program (program)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.4 Faculty Table
```sql
CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    department_id INT,
    designation VARCHAR(100),
    qualification VARCHAR(100),
    specialization VARCHAR(100),
    date_of_joining DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (department_id) REFERENCES Departments(dept_id) ON DELETE SET NULL,
    INDEX idx_email (email),
    INDEX idx_dept (department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.5 Courses Table
```sql
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits > 0),
    department_id INT,
    semester INT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES Departments(dept_id) ON DELETE SET NULL,
    INDEX idx_course_code (course_code),
    INDEX idx_dept (department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.6 Enrollment Table
```sql
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    status ENUM('active', 'dropped', 'completed') DEFAULT 'active',
    grade VARCHAR(2),
    semester INT,
    academic_year VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, course_id, semester),
    INDEX idx_student (student_id),
    INDEX idx_course (course_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.7 Attendance Table
```sql
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Excused') NOT NULL,
    marked_by INT,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollment(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (marked_by) REFERENCES Faculty(faculty_id) ON DELETE SET NULL,
    UNIQUE KEY unique_attendance (enrollment_id, date),
    INDEX idx_date (date),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.8 Grades Table
```sql
CREATE TABLE Grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    assessment_type ENUM('Quiz', 'Midterm', 'Final', 'Assignment', 'Project') NOT NULL,
    marks_obtained DECIMAL(5,2) NOT NULL CHECK (marks_obtained >= 0),
    max_marks DECIMAL(5,2) NOT NULL CHECK (max_marks > 0),
    date DATE,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollment(enrollment_id) ON DELETE CASCADE,
    INDEX idx_enrollment (enrollment_id),
    INDEX idx_type (assessment_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.9 Fees Table
```sql
CREATE TABLE Fees (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    semester INT NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    tuition_fee DECIMAL(10,2) NOT NULL CHECK (tuition_fee >= 0),
    hostel_fee DECIMAL(10,2) DEFAULT 0.00,
    library_fee DECIMAL(10,2) DEFAULT 0.00,
    other_fees DECIMAL(10,2) DEFAULT 0.00,
    total_amount DECIMAL(10,2) GENERATED ALWAYS AS 
        (tuition_fee + hostel_fee + library_fee + other_fees) STORED,
    due_date DATE NOT NULL,
    status ENUM('Pending', 'Partial', 'Paid') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    UNIQUE KEY unique_fee (student_id, semester, academic_year),
    INDEX idx_student (student_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.10 Fee_Payments Table
```sql
CREATE TABLE Fee_Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    fee_id INT NOT NULL,
    amount_paid DECIMAL(10,2) NOT NULL CHECK (amount_paid > 0),
    payment_date DATE NOT NULL,
    payment_method ENUM('Cash', 'Card', 'UPI', 'NetBanking', 'Cheque') NOT NULL,
    transaction_id VARCHAR(100),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (fee_id) REFERENCES Fees(fee_id) ON DELETE CASCADE,
    INDEX idx_fee (fee_id),
    INDEX idx_date (payment_date),
    INDEX idx_transaction (transaction_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5.11 Course_Assignment Table
```sql
CREATE TABLE Course_Assignment (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    faculty_id INT NOT NULL,
    course_id INT NOT NULL,
    semester INT NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    room_number VARCHAR(20),
    time_slot VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_assignment (faculty_id, course_id, semester, academic_year),
    INDEX idx_faculty (faculty_id),
    INDEX idx_course (course_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## 6. Constraints and Integrity

### 6.1 Primary Keys
All tables have auto-incrementing integer primary keys for efficient indexing and foreign key relationships.

### 6.2 Foreign Keys with Actions
- **ON DELETE CASCADE**: Child records deleted when parent is deleted
  - Users → Students, Faculty (delete student/faculty when user deleted)
  - Enrollment → Attendance, Grades (delete related records)
  - Fees → Fee_Payments (delete payments when fee deleted)
  
- **ON DELETE SET NULL**: Foreign key set to NULL when parent deleted
  - Departments → Students, Faculty, Courses (preserve records)
  - Faculty → Attendance (preserve attendance record)

### 6.3 Check Constraints
- `credits > 0` in Courses
- `marks_obtained >= 0` in Grades
- `max_marks > 0` in Grades
- `amount_paid > 0` in Fee_Payments
- All fee amounts `>= 0`

### 6.4 Unique Constraints
- Username in Users
- Email in Students, Faculty
- Course code in Courses
- (student_id, course_id, semester) in Enrollment
- (enrollment_id, date) in Attendance
- (student_id, semester, academic_year) in Fees

### 6.5 NOT NULL Constraints
Applied to essential fields like names, emails, dates, amounts

---

## 7. Stored Procedures

### 7.1 Add Student with User Account
```sql
DELIMITER $$
CREATE PROCEDURE sp_AddStudent(
    IN p_username VARCHAR(50),
    IN p_password VARCHAR(255),
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(15),
    IN p_department_id INT,
    IN p_program VARCHAR(100),
    OUT p_student_id INT
)
BEGIN
    DECLARE v_user_id INT;
    
    -- Insert into Users
    INSERT INTO Users (username, password, role) 
    VALUES (p_username, p_password, 'student');
    
    SET v_user_id = LAST_INSERT_ID();
    
    -- Insert into Students
    INSERT INTO Students (
        user_id, first_name, last_name, email, phone, 
        department_id, program, enrollment_year
    ) VALUES (
        v_user_id, p_first_name, p_last_name, p_email, p_phone,
        p_department_id, p_program, YEAR(CURDATE())
    );
    
    SET p_student_id = LAST_INSERT_ID();
END$$
DELIMITER ;
```

### 7.2 Enroll Student in Course
```sql
DELIMITER $$
CREATE PROCEDURE sp_EnrollStudent(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_semester INT,
    IN p_academic_year VARCHAR(10),
    OUT p_enrollment_id INT
)
BEGIN
    INSERT INTO Enrollment (
        student_id, course_id, enrollment_date, 
        semester, academic_year, status
    ) VALUES (
        p_student_id, p_course_id, CURDATE(),
        p_semester, p_academic_year, 'active'
    );
    
    SET p_enrollment_id = LAST_INSERT_ID();
END$$
DELIMITER ;
```

### 7.3 Mark Attendance
```sql
DELIMITER $$
CREATE PROCEDURE sp_MarkAttendance(
    IN p_enrollment_id INT,
    IN p_date DATE,
    IN p_status ENUM('Present', 'Absent', 'Late', 'Excused'),
    IN p_marked_by INT
)
BEGIN
    INSERT INTO Attendance (enrollment_id, date, status, marked_by)
    VALUES (p_enrollment_id, p_date, p_status, p_marked_by)
    ON DUPLICATE KEY UPDATE 
        status = p_status,
        marked_by = p_marked_by;
END$$
DELIMITER ;
```

### 7.4 Add Grade
```sql
DELIMITER $$
CREATE PROCEDURE sp_AddGrade(
    IN p_enrollment_id INT,
    IN p_assessment_type ENUM('Quiz','Midterm','Final','Assignment','Project'),
    IN p_marks_obtained DECIMAL(5,2),
    IN p_max_marks DECIMAL(5,2),
    IN p_date DATE
)
BEGIN
    INSERT INTO Grades (
        enrollment_id, assessment_type, marks_obtained, 
        max_marks, date
    ) VALUES (
        p_enrollment_id, p_assessment_type, p_marks_obtained,
        p_max_marks, p_date
    );
END$$
DELIMITER ;
```

### 7.5 Calculate GPA
```sql
DELIMITER $$
CREATE FUNCTION fn_CalculateGPA(p_student_id INT, p_semester INT)
RETURNS DECIMAL(3,2)
DETERMINISTIC
BEGIN
    DECLARE v_gpa DECIMAL(3,2);
    
    SELECT AVG(
        CASE grade
            WHEN 'A+' THEN 4.0
            WHEN 'A' THEN 4.0
            WHEN 'A-' THEN 3.7
            WHEN 'B+' THEN 3.3
            WHEN 'B' THEN 3.0
            WHEN 'B-' THEN 2.7
            WHEN 'C+' THEN 2.3
            WHEN 'C' THEN 2.0
            WHEN 'C-' THEN 1.7
            WHEN 'D' THEN 1.0
            ELSE 0.0
        END
    ) INTO v_gpa
    FROM Enrollment
    WHERE student_id = p_student_id 
      AND semester = p_semester
      AND grade IS NOT NULL;
    
    RETURN COALESCE(v_gpa, 0.00);
END$$
DELIMITER ;
```

### 7.6 Get Student Report
```sql
DELIMITER $$
CREATE PROCEDURE sp_GetStudentReport(
    IN p_student_id INT,
    IN p_semester INT
)
BEGIN
    SELECT 
        c.course_code,
        c.course_name,
        c.credits,
        e.grade,
        CONCAT(f.first_name, ' ', f.last_name) AS faculty_name,
        COUNT(a.attendance_id) AS total_classes,
        SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS present_count,
        ROUND(SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(a.attendance_id), 2) AS attendance_percentage
    FROM Enrollment e
    JOIN Courses c ON e.course_id = c.course_id
    LEFT JOIN Course_Assignment ca ON c.course_id = ca.course_id AND e.semester = ca.semester
    LEFT JOIN Faculty f ON ca.faculty_id = f.faculty_id
    LEFT JOIN Attendance a ON e.enrollment_id = a.enrollment_id
    WHERE e.student_id = p_student_id
      AND e.semester = p_semester
    GROUP BY e.enrollment_id, c.course_code, c.course_name, c.credits, e.grade, f.first_name, f.last_name;
END$$
DELIMITER ;
```

---

## 8. Views

### 8.1 Student Course View
```sql
CREATE VIEW vw_StudentCourses AS
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.email,
    c.course_code,
    c.course_name,
    c.credits,
    e.enrollment_date,
    e.status AS enrollment_status,
    e.grade,
    e.semester,
    e.academic_year
FROM Students s
JOIN Enrollment e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
```

### 8.2 Attendance Summary View
```sql
CREATE VIEW vw_AttendanceSummary AS
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_code,
    c.course_name,
    COUNT(a.attendance_id) AS total_classes,
    SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS present_count,
    SUM(CASE WHEN a.status = 'Absent' THEN 1 ELSE 0 END) AS absent_count,
    ROUND(SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(a.attendance_id), 2) AS attendance_percentage
FROM Students s
JOIN Enrollment e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
LEFT JOIN Attendance a ON e.enrollment_id = a.enrollment_id
GROUP BY s.student_id, c.course_code, c.course_name;
```

### 8.3 Faculty Courses View
```sql
CREATE VIEW vw_FacultyCourses AS
SELECT 
    f.faculty_id,
    CONCAT(f.first_name, ' ', f.last_name) AS faculty_name,
    c.course_code,
    c.course_name,
    c.credits,
    ca.semester,
    ca.academic_year,
    ca.room_number,
    ca.time_slot
FROM Faculty f
JOIN Course_Assignment ca ON f.faculty_id = ca.faculty_id
JOIN Courses c ON ca.course_id = c.course_id;
```

### 8.4 Fee Status View
```sql
CREATE VIEW vw_FeeStatus AS
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    f.semester,
    f.academic_year,
    f.total_amount,
    COALESCE(SUM(fp.amount_paid), 0) AS amount_paid,
    f.total_amount - COALESCE(SUM(fp.amount_paid), 0) AS balance,
    f.due_date,
    f.status
FROM Students s
JOIN Fees f ON s.student_id = f.student_id
LEFT JOIN Fee_Payments fp ON f.fee_id = fp.fee_id
GROUP BY f.fee_id;
```

---

## 9. Indexes

### 9.1 Primary Indexes
All primary keys are automatically indexed.

### 9.2 Foreign Key Indexes
Foreign keys are automatically indexed for join performance.

### 9.3 Additional Indexes
```sql
-- Users table
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_role ON Users(role);

-- Students table
CREATE INDEX idx_email ON Students(email);
CREATE INDEX idx_dept ON Students(department_id);
CREATE INDEX idx_program ON Students(program);

-- Faculty table
CREATE INDEX idx_email ON Faculty(email);
CREATE INDEX idx_dept ON Faculty(department_id);

-- Courses table
CREATE INDEX idx_course_code ON Courses(course_code);
CREATE INDEX idx_dept ON Courses(department_id);

-- Enrollment table
CREATE INDEX idx_student ON Enrollment(student_id);
CREATE INDEX idx_course ON Enrollment(course_id);
CREATE INDEX idx_status ON Enrollment(status);

-- Attendance table
CREATE INDEX idx_date ON Attendance(date);
CREATE INDEX idx_status ON Attendance(status);

-- Fees table
CREATE INDEX idx_student ON Fees(student_id);
CREATE INDEX idx_status ON Fees(status);

-- Fee_Payments table
CREATE INDEX idx_fee ON Fee_Payments(fee_id);
CREATE INDEX idx_date ON Fee_Payments(payment_date);
CREATE INDEX idx_transaction ON Fee_Payments(transaction_id);
```

---

## 10. Sample Queries

### 10.1 Get Student Dashboard Data
```sql
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    s.program,
    s.semester,
    SUM(c.credits) AS total_credits,
    COUNT(DISTINCT e.course_id) AS active_courses,
    ROUND(AVG(att.attendance_pct), 2) AS avg_attendance,
    fn_CalculateGPA(s.student_id, s.semester) AS gpa
FROM Students s
LEFT JOIN Enrollment e ON s.student_id = e.student_id AND e.status = 'active'
LEFT JOIN Courses c ON e.course_id = c.course_id
LEFT JOIN (
    SELECT 
        enrollment_id,
        SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS attendance_pct
    FROM Attendance
    GROUP BY enrollment_id
) att ON e.enrollment_id = att.enrollment_id
WHERE s.student_id = ?
GROUP BY s.student_id;
```

### 10.2 Get Faculty Dashboard Data
```sql
SELECT 
    f.faculty_id,
    CONCAT(f.first_name, ' ', f.last_name) AS name,
    f.designation,
    COUNT(DISTINCT ca.course_id) AS assigned_courses,
    COUNT(DISTINCT e.student_id) AS total_students
FROM Faculty f
LEFT JOIN Course_Assignment ca ON f.faculty_id = ca.faculty_id
LEFT JOIN Enrollment e ON ca.course_id = e.course_id AND e.status = 'active'
WHERE f.faculty_id = ?
GROUP BY f.faculty_id;
```

### 10.3 Get Course Enrollment Details
```sql
SELECT 
    c.course_code,
    c.course_name,
    c.credits,
    COUNT(e.enrollment_id) AS enrolled_students,
    CONCAT(f.first_name, ' ', f.last_name) AS faculty_name
FROM Courses c
LEFT JOIN Enrollment e ON c.course_id = e.course_id AND e.status = 'active'
LEFT JOIN Course_Assignment ca ON c.course_id = ca.course_id
LEFT JOIN Faculty f ON ca.faculty_id = f.faculty_id
WHERE c.course_id = ?
GROUP BY c.course_id;
```

### 10.4 Get Outstanding Fees
```sql
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    f.semester,
    f.total_amount,
    COALESCE(SUM(fp.amount_paid), 0) AS paid,
    f.total_amount - COALESCE(SUM(fp.amount_paid), 0) AS outstanding,
    f.due_date
FROM Students s
JOIN Fees f ON s.student_id = f.student_id
LEFT JOIN Fee_Payments fp ON f.fee_id = fp.fee_id
WHERE f.status != 'Paid'
GROUP BY f.fee_id
HAVING outstanding > 0;
```

---

## 11. Database Statistics

| Metric | Value |
|--------|-------|
| **Total Tables** | 11 |
| **Total Columns** | 100+ |
| **Total Relationships** | 15+ |
| **Stored Procedures** | 6 |
| **Views** | 4 |
| **Indexes** | 25+ |
| **Normalization** | 3NF |
| **Engine** | InnoDB |
| **Charset** | utf8mb4 |
| **Collation** | utf8mb4_unicode_ci |

---

## 12. Backup and Maintenance

### 12.1 Backup Commands
```bash
# Full database backup
mysqldump -u root -p student_management_system > backup_$(date +%Y%m%d).sql

# Schema only
mysqldump -u root -p --no-data student_management_system > schema_backup.sql

# Data only
mysqldump -u root -p --no-create-info student_management_system > data_backup.sql
```

### 12.2 Maintenance Tasks
```sql
-- Optimize tables
OPTIMIZE TABLE Students, Faculty, Courses, Enrollment, Attendance, Grades;

-- Analyze tables for query optimization
ANALYZE TABLE Students, Faculty, Courses;

-- Check table integrity
CHECK TABLE Students, Faculty, Courses;

-- Repair tables if needed
REPAIR TABLE Students;
```

---

## 13. Conclusion

This database design provides a robust foundation for the Student Management System with:

✅ **Normalized Structure** (3NF) for data integrity  
✅ **Efficient Indexing** for query performance  
✅ **Foreign Key Constraints** for referential integrity  
✅ **Stored Procedures** for business logic  
✅ **Views** for simplified data access  
✅ **Scalable Architecture** supporting future enhancements

---

**Document Version**: 2.0  
**Last Updated**: November 6, 2025  
**Maintained By**: Pranvkumar Kshirsagar  
**Contact**: pranvkumar.11587@stu.upes.ac.in
