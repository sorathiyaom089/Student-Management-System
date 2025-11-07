# 🎓 Student Management System

<div align="center">

![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-production%20ready-brightgreen.svg)
![License](https://img.shields.io/badge/license-educational-orange.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey.svg)

**A comprehensive, enterprise-grade Student Management System with modern UPES-style portals**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Screenshots](#-screenshots)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [User Portals](#-user-portals)
- [Database Design](#-database-design)
- [Advanced Features](#-advanced-features)
- [Screenshots](#-screenshots)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

A **production-ready** web-based Student Management System built with Python Flask and MySQL. This enterprise-grade application manages the complete lifecycle of student, faculty, and course data with **role-based access control**, real-time attendance tracking, grade management, fee processing, and advanced reporting.

### 🎯 Project Highlights

✨ **80+ Flask Routes** with complete CRUD operations  
✨ **10+ Database Tables** with proper normalization (3NF)  
✨ **6 Stored Procedures** for complex business logic  
✨ **3 Distinct Portals** (Student, Faculty, Admin)  
✨ **Modern UI/UX** with responsive design  
✨ **Production Quality** clean, maintainable code  
✨ **Comprehensive Documentation** (4 detailed files)

---

## ✨ Key Features

### 🎓 Student Portal
- **Modern Dashboard** with KPI cards, attendance tracker, learning hours gauge
- **Interactive Calendar** with 4 view modes (Day/Week/Month/Agenda)
- **Collapsible Sidebar** with LocalStorage persistence (250px ↔ 70px)
- **LMS System** with colorful course cards (8 gradient themes)
- **Comprehensive Profile** with academic progress tracking
- **Fee Management** with payment history and breakdown
- **Announcements** with category filtering
- **Real-time Attendance** tracking with color-coded progress

### 👨‍🏫 Faculty Portal
- **Course Dashboard** with quick stats and active courses
- **Attendance Management** with bulk actions (Mark All Present/Absent)
- **Grade Management** with visual stat cards
- **LMS Features** for assignment creation and material upload
- **Student Directory** with search and filters
- **Attendance Reports** with percentages and color coding
- **Weekly Timetable** with interactive schedule grid

### 👨‍💼 Admin Portal
- **System Dashboard** with comprehensive statistics
- **Student Management** with Excel bulk upload
- **Faculty Management** with assignment tracking
- **Course Management** with enrollment control
- **Fee Management** with payment tracking
- **Reporting System** for attendance, grades, and fees
- **Announcements** creation and management

---

## 🛠️ Technology Stack

### Backend
- **Python 3.13** - Latest stable version
- **Flask 3.0.0** - Lightweight web framework
- **MySQL 8.0** - Relational database
- **Jinja2** - Template engine
- **Session Management** - Secure authentication

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling (1,700+ lines)
  - Flexbox & Grid layouts
  - CSS Variables
  - Smooth animations
- **Vanilla JavaScript** (800+ lines)
  - No frameworks required
  - LocalStorage integration
  - Dynamic content rendering

### Additional Libraries
- **Pandas** - Excel file processing
- **openpyxl** - Excel operations
- **mysql-connector-python** - Database driver

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- MySQL 8.0+
- pip package manager

### Installation (5 Minutes)

#### Step 1: Clone Repository
```bash
git clone https://github.com/Pranvkumar/Student-Management-System.git
cd Student_Management_System
```

#### Step 2: Install Dependencies
```bash
pip install flask mysql-connector-python pandas openpyxl
```

#### Step 3: Database Setup
```sql
-- Open MySQL Command Line and execute:
source database/01_schema.sql;
source database/02_sample_data.sql;
source database/03_procedures_functions.sql;
```

#### Step 4: Configure Database Connection
Edit `backend/database.py` and update credentials:
```python
self.connection = mysql.connector.connect(
    host='localhost',
    user='root',           # Your MySQL username
    password='yourpass',   # Your MySQL password
    database='student_management_system'
)
```

#### Step 5: Run Application
```bash
cd backend
python app.py
```

#### Step 6: Access Application
Open browser and navigate to:
- **Application**: http://localhost:5000
- **Login**: Use credentials from sample data

### Default Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Student | S001 | student123 |
| Faculty | F001 | faculty123 |

---

## 📁 Project Structure

```
Student_Management_System/
├── backend/
│   ├── app.py              # Flask application (1,097 lines, 80+ routes)
│   └── database.py         # Database connection handler
│
├── templates/
│   ├── base_student.html   # Student portal base template
│   ├── base_faculty.html   # Faculty portal base template
│   ├── admin/              # Admin templates (15 files)
│   ├── student/            # Student templates (9 files)
│   └── faculty/            # Faculty templates (10 files)
│
├── static/
│   └── css/
│       ├── student_portal.css  # Student styles (850+ lines)
│       └── faculty_portal.css  # Faculty styles (856+ lines)
│
├── database/
│   ├── 01_schema.sql           # Database schema
│   ├── 02_sample_data.sql      # Sample data
│   └── 03_procedures_functions.sql  # Stored procedures
│
├── .vscode/
│   └── settings.json       # VS Code configuration
│
├── README.md               # This file
├── QUICK_START.md          # 5-minute setup guide
├── DATABASE_DESIGN.md      # ER diagram & schema
├── IMPLEMENTATION_SUMMARY.md  # Detailed documentation
└── requirements.txt        # Python dependencies
```

---

## 👥 User Portals

### 🎓 Student Portal Features

| Feature | Description |
|---------|-------------|
| **Dashboard** | KPI cards, attendance summary, learning hours tracker |
| **Profile** | Personal info, academic progress, semester history |
| **Timetable** | 4 view modes with interactive calendar |
| **LMS** | Course materials with colorful card design |
| **Attendance** | Real-time tracking with color-coded progress |
| **Grades** | Semester-wise results with GPA calculation |
| **Announcements** | Campus notifications with category filters |
| **Fee Payment** | Due amounts, payment history, breakdown |

### 👨‍🏫 Faculty Portal Features

| Feature | Description |
|---------|-------------|
| **Dashboard** | Course overview with quick statistics |
| **Attendance** | Mark attendance with bulk actions |
| **Grades** | Add/manage grades with visual cards |
| **LMS** | Assignment creation and material upload |
| **Students** | Directory with search and filtering |
| **Reports** | Attendance percentages and analytics |
| **Timetable** | Weekly schedule grid view |

### 👨‍💼 Admin Portal Features

| Feature | Description |
|---------|-------------|
| **Dashboard** | System-wide statistics overview |
| **Students** | CRUD operations + Excel bulk upload |
| **Faculty** | Manage faculty records and assignments |
| **Courses** | Course creation and enrollment |
| **Fees** | Payment tracking and reporting |
| **Reports** | Comprehensive reporting system |
| **Announcements** | Create and manage notifications |

---

## 🗄️ Database Design

### Core Tables (10)

1. **Users** - Authentication and authorization
2. **Students** - Student personal information
3. **Faculty** - Faculty details and qualifications
4. **Courses** - Course catalog and details
5. **Departments** - Academic department structure
6. **Enrollment** - Student-course relationships
7. **Attendance** - Attendance records
8. **Grades** - Assessment and grading
9. **Fees** - Fee structure and dues
10. **Fee_Payments** - Payment transaction records

### Stored Procedures (6)

- `sp_AddStudent` - Create student with user account
- `sp_EnrollStudent` - Enroll student in course
- `sp_MarkAttendance` - Record attendance
- `sp_AddGrade` - Add/update grades
- `sp_CalculateGPA` - Calculate student GPA
- `sp_GetStudentReport` - Generate comprehensive report

**For complete ER diagram and schema details, see [DATABASE_DESIGN.md](DATABASE_DESIGN.md)**

---

## 🚀 Advanced Features

### 📊 Data Visualization
- **SVG Gauge Charts** for learning hours (interactive, animated)
- **Progress Bars** with smooth animations (0.6s ease)
- **Color-Coded Indicators** (Green ≥75%, Yellow ≥60%, Red <60%)
- **KPI Cards** with gradient backgrounds
- **Attendance Heatmaps** in calendar view

### 🎨 Modern UI Components
- **Collapsible Sidebar** with LocalStorage persistence
  - Expanded: 250px (icons + labels)
  - Collapsed: 70px (icons only)
  - Smooth 0.3s transitions
- **Tabbed Interfaces** for organized content
- **Skeleton Loading** screens (800ms animation)
- **Modal Dialogs** for forms and actions
- **Toast Notifications** for user feedback

### 📅 Calendar System
- **4 View Modes**:
  - Day: Timeline view with hourly slots
  - Week: 7-column grid with time blocks
  - Month: Calendar with event pills
  - Agenda: Chronological list view
- **Features**: Month navigation, color-coded events, responsive design

### 📤 Excel Integration
- **Bulk Upload** student data via Excel files
- **Template Download** for proper formatting
- **Data Validation** before import
- **Auto-Generation** of user accounts

### 🔐 Security Features
- **Session-Based Authentication** with secure cookies
- **Role-Based Access Control** (RBAC)
- **SQL Injection Prevention** via parameterized queries
- **XSS Protection** through Jinja2 auto-escaping
- **Password Hashing** (ready for bcrypt)

---

## 📸 Screenshots

> **Coming Soon**: Screenshots of all portal views will be added here.

### Student Portal
- Dashboard with KPI cards
- Interactive calendar (4 views)
- LMS with colorful course cards
- Profile with progress tracking

### Faculty Portal
- Course management dashboard
- Attendance marking interface
- Grade management system
- Student directory

### Admin Portal
- System statistics dashboard
- Student management interface
- Excel bulk upload
- Reports generation

---

## 🧪 Testing

### Manual Testing ✅
- All features tested across browsers
- Cross-browser: Chrome, Firefox, Edge, Safari
- Responsive: Mobile (320px), Tablet (768px), Desktop (1920px)

### Database Operations ✅
- All CRUD operations verified
- Stored procedures tested
- Foreign key constraints validated
- Data integrity confirmed

### User Flows ✅
- Login/logout flows tested
- Session management verified
- Role switching confirmed
- Excel upload validated
- Calendar views rendering correctly

---

## 🔧 Troubleshooting

### Common Issues

#### Database Connection Error
```
Error: Can't connect to MySQL server
Fix:
1. Ensure MySQL is running
2. Check credentials in backend/database.py
3. Verify database exists: student_management_system
```

#### Port Already in Use
```
Error: Address already in use
Fix: Change port in backend/app.py
app.run(debug=True, port=5001)
```

#### Module Not Found
```
Error: ModuleNotFoundError: No module named 'flask'
Fix: Install dependencies
pip install flask mysql-connector-python pandas openpyxl
```

#### CSS Linting Errors
```
Issue: VS Code showing CSS errors
Fix: Reload VS Code window
Ctrl+Shift+P → "Reload Window"
Settings already configured in .vscode/settings.json
```

---

## 🔮 Future Enhancements

### Phase 1 (Short-term)
- [ ] Email notifications for announcements and grades
- [ ] PDF report generation (transcripts, certificates)
- [ ] Two-factor authentication (2FA)
- [ ] Password reset functionality
- [ ] User activity logs and audit trails
- [ ] Advanced search with multiple filters

### Phase 2 (Mid-term)
- [ ] Online examination module with timer
- [ ] Discussion forums per course
- [ ] Document upload/download system
- [ ] Assignment submission portal
- [ ] Grade appeals workflow
- [ ] SMS notifications for critical updates

### Phase 3 (Long-term)
- [ ] Mobile app (React Native / Flutter)
- [ ] Real-time notifications (WebSockets)
- [ ] Advanced analytics with Chart.js
- [ ] AI-powered attendance predictions
- [ ] Video conferencing integration
- [ ] Blockchain-based certificates
- [ ] Alumni portal and networking

---

## 🤝 Contributing

This is an academic project, but contributions and suggestions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📚 Documentation

| File | Description | Lines |
|------|-------------|-------|
| **README.md** | Project overview and setup | 700+ |
| **QUICK_START.md** | 5-minute quick setup guide | 150+ |
| **DATABASE_DESIGN.md** | ER diagram and schema | 400+ |
| **IMPLEMENTATION_SUMMARY.md** | Detailed feature documentation | 1000+ |

---

## 📊 Project Statistics

- **Total Lines of Code**: 12,000+
  - Python: 1,500+
  - HTML: 6,000+
  - CSS: 1,700+
  - JavaScript: 800+
  - SQL: 2,000+
- **Files**: 50+
- **Routes**: 80+
- **Templates**: 34+
- **Development Time**: 40+ hours

---

## 🎓 Academic Information

- **Course**: Database Management Systems (DBMS)
- **Student**: Pranvkumar Kshirsagar
- **SAP ID**: 590011587
- **University**: University of Petroleum and Energy Studies (UPES)
- **Semester**: Fall 2025
- **Year**: 2025

---

## 📄 License

This project is created for educational purposes as part of the DBMS course at UPES.

**License**: Educational Use Only  
**Copyright**: © 2025 Pranvkumar Kshirsagar

All rights reserved. This code is provided for educational and portfolio purposes only.

---

## 📧 Contact & Support

**Developer**: Pranvkumar Kshirsagar  
**Email**: pranvkumar.11587@stu.upes.ac.in  
**GitHub**: [@Pranvkumar](https://github.com/Pranvkumar)  
**Repository**: [Student-Management-System](https://github.com/Pranvkumar/Student-Management-System)

### Get Help
- 🐛 Report bugs via [GitHub Issues](https://github.com/Pranvkumar/Student-Management-System/issues)
- 💬 Ask questions via email
- 🔀 Suggest improvements via Pull Requests

---

## 🙏 Acknowledgments

Special thanks to:
- **UPES Faculty** for guidance and support
- **Flask Community** for excellent documentation
- **MySQL Team** for robust database system
- **MDN Web Docs** for comprehensive web references
- **Stack Overflow** community for problem-solving

---

<div align="center">

**Last Updated**: January 2025  
**Version**: 3.0.0  
**Status**: ✅ Production Ready  

---

**⭐ If you find this project helpful, please star it on GitHub!**

[Back to Top](#-student-management-system)

</div>
