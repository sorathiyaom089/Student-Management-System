# Student Management System - System Design Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Use Cases](#use-cases)
3. [Database Design (ER Diagram)](#database-design-er-diagram)
4. [Module Description](#module-description)
5. [System Architecture](#system-architecture)
6. [Installation Guide](#installation-guide)

## System Overview

The Student Management System is a comprehensive web-based application designed for educational institutions to manage student information, academic programs, examinations, payments, and administrative activities. The system provides a centralized platform for handling all aspects of student lifecycle management.

### Key Features
- Student registration and profile management
- Academic program and batch management
- Examination and result management
- Payment tracking and fee management
- Attendance monitoring
- SMS notification system
- ID card generation
- Multi-user access with role-based permissions

## Use Cases

### 1. Actor Identification
- **Primary Actors:**
  - Administrator
  - Academic Staff
  - Student
  - System

### 2. Use Case Diagrams

#### 2.1 Student Management Use Cases
```
┌─────────────────────────────────────────────────────────┐
│                Student Management System                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Administrator        Academic Staff        Student     │
│       │                     │                 │        │
│       │                     │                 │        │
│       ▼                     ▼                 ▼        │
│  ┌─────────┐           ┌─────────┐       ┌─────────┐    │
│  │ Login   │           │ Login   │       │View     │    │
│  │ System  │           │ System  │       │Profile  │    │
│  └─────────┘           └─────────┘       └─────────┘    │
│       │                     │                 │        │
│       ▼                     ▼                 ▼        │
│  ┌─────────┐           ┌─────────┐       ┌─────────┐    │
│  │Manage   │           │Take     │       │View     │    │
│  │Students │           │Attend   │       │Results  │    │
│  └─────────┘           └─────────┘       └─────────┘    │
│       │                     │                 │        │
│       ▼                     ▼                 ▼        │
│  ┌─────────┐           ┌─────────┐       ┌─────────┐    │
│  │Manage   │           │Enter    │       │View     │    │
│  │Programs │           │Results  │       │Schedule │    │
│  └─────────┘           └─────────┘       └─────────┘    │
│       │                     │                          │
│       ▼                     ▼                          │
│  ┌─────────┐           ┌─────────┐                      │
│  │Generate │           │Send SMS │                      │
│  │Reports  │           │Notices  │                      │
│  └─────────┘           └─────────┘                      │
└─────────────────────────────────────────────────────────┘
```

#### 2.2 Detailed Use Cases

**UC-001: Student Registration**
- **Actor:** Administrator
- **Description:** Register new student with personal and academic information
- **Preconditions:** User must be logged in as administrator
- **Flow:**
  1. Administrator selects "Add Student"
  2. System displays student registration form
  3. Administrator enters student details
  4. System validates information
  5. System saves student data and generates student ID
- **Postconditions:** Student is registered in the system

**UC-002: Program Enrollment**
- **Actor:** Administrator
- **Description:** Enroll student in academic programs
- **Preconditions:** Student must exist in system
- **Flow:**
  1. Administrator selects student
  2. Administrator chooses program and batch
  3. System validates enrollment criteria
  4. System enrolls student in program
- **Postconditions:** Student is enrolled in selected program

**UC-003: Attendance Management**
- **Actor:** Academic Staff
- **Description:** Record and manage student attendance
- **Flow:**
  1. Staff selects program and batch
  2. System displays student list
  3. Staff marks attendance for each student
  4. System records attendance data
- **Postconditions:** Attendance is recorded

**UC-004: Examination Management**
- **Actor:** Academic Staff, Administrator
- **Description:** Create exams and enter results
- **Flow:**
  1. User creates examination
  2. System schedules exam
  3. Staff enters results
  4. System calculates grades and rankings
- **Postconditions:** Exam results are recorded

**UC-005: Payment Processing**
- **Actor:** Administrator
- **Description:** Process student fee payments
- **Flow:**
  1. Administrator selects student
  2. System displays payment history
  3. Administrator records new payment
  4. System updates payment status
- **Postconditions:** Payment is recorded

## Database Design (ER Diagram)

### Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Student Management System ER Diagram          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐   │
│    │   STUDENT   │         │   PROGRAM   │         │    BATCH    │   │
│    │─────────────│         │─────────────│         │─────────────│   │
│    │ PK: id      │         │ PK: id      │         │ PK: id      │   │
│    │    name     │◄────────┤    name     │◄────────┤    name     │   │
│    │ father_name │         │    start    │         │    start    │   │
│    │ mother_name │         │    end      │         │    end      │   │
│    │    email    │         │   subject   │         │    day      │   │
│    │   photo     │         │    batch    │         └─────────────┘   │
│    │personal_mob │         │    fee      │                           │
│    │father_mobile│         │    type     │                           │
│    │mother_mobile│         │monthly_fee  │                           │
│    │   address   │         │   add_by    │                           │
│    │ birth_day   │         │    date     │                           │
│    │   gender    │         └─────────────┘                           │
│    │  religion   │                │                                  │
│    │   school    │                │                                  │
│    │  ssc_roll   │                │                                  │
│    │   ssc_reg   │                │                                  │
│    │  ssc_board  │                │                                  │
│    │ ssc_result  │                │                                  │
│    │    date     │                │                                  │
│    └─────────────┘                │                                  │
│           │                       │                                  │
│           │                       │                                  │
│           ▼                       ▼                                  │
│    ┌─────────────┐         ┌─────────────┐                           │
│    │ADMIT_PROGRAM│         │    EXAM     │                           │
│    │─────────────│         │─────────────│                           │
│    │ PK: id      │         │ PK: id      │                           │
│    │ FK:student_id│        │FK:program_id│                           │
│    │FK:program_id│         │FK: sub_id   │                           │
│    │FK: batch_id │         │ exam_name   │                           │
│    │ admit_date  │         │   total     │                           │
│    │  admit_by   │         │    mcq      │                           │
│    └─────────────┘         │   written   │                           │
│           │                │ exam_date   │                           │
│           │                │    date     │                           │
│           │                │   add_by    │                           │
│           │                └─────────────┘                           │
│           │                       │                                  │
│           ▼                       ▼                                  │
│    ┌─────────────┐         ┌─────────────┐                           │
│    │ ATTENDANCE  │         │   RESULT    │                           │
│    │─────────────│         │─────────────│                           │
│    │ PK: id      │         │ PK: id      │                           │
│    │FK:student_id│         │FK: exam_id  │                           │
│    │FK:program_id│         │FK:student_id│                           │
│    │FK: batch_id │         │    mcq      │                           │
│    │   status    │         │   written   │                           │
│    │    date     │         │   total     │                           │
│    └─────────────┘         │    date     │                           │
│           │                │   add_by    │                           │
│           │                │    sms      │                           │
│           │                └─────────────┘                           │
│           │                                                          │
│           ▼                                                          │
│    ┌─────────────┐         ┌─────────────┐                           │
│    │   PAYMENT   │         │   SUBJECT   │                           │
│    │─────────────│         │─────────────│                           │
│    │ PK: id      │         │ PK: id      │                           │
│    │FK:student_id│         │  sub_name   │                           │
│    │    paid     │         │  sub_code   │                           │
│    │ next_date   │         └─────────────┘                           │
│    │    date     │                                                   │
│    │   add_by    │                                                   │
│    └─────────────┘                                                   │
│           │                                                          │
│           ▼                                                          │
│    ┌─────────────┐         ┌─────────────┐                           │
│    │    USER     │         │   NOTICE    │                           │
│    │─────────────│         │─────────────│                           │
│    │ PK: id      │         │ PK: id      │                           │
│    │   uname     │         │   title     │                           │
│    │   fname     │         │description  │                           │
│    │   photo     │         │    date     │                           │
│    │   gender    │         │   add_by    │                           │
│    │   email     │         └─────────────┘                           │
│    │   phone     │                                                   │
│    │  address    │         ┌─────────────┐                           │
│    │    pass     │         │   SETTING   │                           │
│    │   permit    │         │─────────────│                           │
│    │   status    │         │ PK: id      │                           │
│    │   theme     │         │option_name  │                           │
│    └─────────────┘         │option_value │                           │
│                            └─────────────┘                           │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Relationships

1. **Student-Program (Many-to-Many)**: Students can enroll in multiple programs through admit_program table
2. **Program-Batch (One-to-Many)**: Each program can have multiple batches
3. **Student-Attendance (One-to-Many)**: Each student has multiple attendance records
4. **Student-Payment (One-to-Many)**: Each student can have multiple payment records
5. **Exam-Result (One-to-Many)**: Each exam can have multiple student results
6. **User-Activity (One-to-Many)**: Each user action is logged in site_activity

## Module Description

### 1. Authentication Module
**Files:** `login.php`, `login_action.php`, `logout.php`
- **Purpose:** Handles user authentication and session management
- **Features:**
  - Secure login with encrypted passwords
  - Session management
  - Role-based access control
  - Activity logging

### 2. Student Management Module
**Files:** `student.php`, `student_action.php`, `add_student.php`, `student_profile.php`
- **Purpose:** Complete student lifecycle management
- **Features:**
  - Student registration with comprehensive personal details
  - Photo upload and management
  - Academic history tracking
  - Student profile editing and viewing

### 3. Academic Program Module
**Files:** `program_list.php`, `program_action.php`, `batch_list.php`, `batch_action.php`
- **Purpose:** Manages academic programs and batches
- **Features:**
  - Program creation and management
  - Batch scheduling and organization
  - Program enrollment
  - Subject assignment

### 4. Examination Module
**Files:** `exam.php`, `exam_action.php`, `result.php`, `result_action.php`
- **Purpose:** Comprehensive examination management
- **Features:**
  - Exam creation and scheduling
  - Result entry and calculation
  - Automatic ranking generation
  - Grade management

### 5. Attendance Module
**Files:** `attend.php`, `attend_action.php`
- **Purpose:** Student attendance tracking
- **Features:**
  - Daily attendance marking
  - Attendance reports
  - Batch-wise attendance management
  - Attendance analytics

### 6. Payment Module
**Files:** `payment.php`, `student_payment.php`
- **Purpose:** Financial management and fee tracking
- **Features:**
  - Fee payment recording
  - Payment history tracking
  - Due date management
  - Payment reports

### 7. Communication Module
**Files:** `sms_dashboard.php`, `sms_action.php`, `notice.php`, `chat.php`
- **Purpose:** Communication between administration and students
- **Features:**
  - SMS notifications for results and notices
  - Notice board management
  - Internal chat system
  - Bulk messaging

### 8. Reporting Module
**Files:** `report.php`, `report_action.php`, `export.php`
- **Purpose:** Generate various administrative reports
- **Features:**
  - Student reports
  - Financial reports
  - Attendance reports
  - Performance analytics

### 9. ID Card Module
**Files:** `id_card.php`, `id_card_action.php`, `print_page.php`
- **Purpose:** Generate and print student ID cards
- **Features:**
  - ID card design and generation
  - Barcode integration
  - Print-ready formatting
  - Bulk ID card generation

### 10. System Administration Module
**Files:** `setting.php`, `user_list.php`, `theme.php`
- **Purpose:** System configuration and user management
- **Features:**
  - System settings management
  - User role management
  - Theme customization
  - Activity monitoring

## System Architecture

### Technology Stack
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Backend:** PHP
- **Database:** MySQL
- **Server:** Apache/Nginx compatible
- **Additional:** AJAX for dynamic interactions

### Architecture Pattern
The system follows a **3-Tier Architecture**:

1. **Presentation Layer (Frontend)**
   - HTML templates with Bootstrap styling
   - JavaScript for client-side interactions
   - AJAX for asynchronous operations

2. **Business Logic Layer (Backend)**
   - PHP scripts for server-side processing
   - Action files for specific operations
   - Session management and authentication

3. **Data Access Layer (Database)**
   - MySQL database with normalized schema
   - Database abstraction through custom classes
   - Transaction management for data integrity

### Security Features
- Password encryption using SHA-256
- SQL injection prevention
- Session-based authentication
- Role-based access control
- Activity logging for audit trails

## Installation Guide

### Prerequisites
- Web server (Apache/Nginx)
- PHP 7.0 or higher
- MySQL 5.7 or higher
- Web browser with JavaScript enabled

### Installation Steps

1. **Download and Extract**
   - Extract the project files to your web server directory

2. **Database Setup**
   - Create a new MySQL database
   - Import the SQL file from `/sql/install_sql.sql`

3. **Configuration**
   - Navigate to the project URL in your browser
   - Follow the installation wizard
   - Enter database connection details

4. **Default Login**
   - Username: `admin`
   - Password: `admin`

5. **Post-Installation**
   - Change default admin password
   - Configure system settings
   - Add users and roles as needed

### System Requirements
- **Minimum RAM:** 512MB
- **Storage:** 100MB free space
- **PHP Extensions:** mysqli, gd, session
- **Browser Support:** Chrome, Firefox, Safari, Edge

---

*This documentation provides a comprehensive overview of the Student Management System. For technical support or feature requests, please refer to the project documentation or contact the development team.*