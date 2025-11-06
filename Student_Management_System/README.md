# Student Management System

A modern, feature-rich web-based student management system with a dynamic UPES-style student portal. Built with Python Flask and MySQL.

## ✨ Key Features

### 🎓 Student Portal
- **Dynamic Dashboard** with KPI cards (Credits, Courses, Attendance, Performance)
- **Collapsible Sidebar** with smooth animations (250px ↔ 70px)
- **Interactive Calendar** with month navigation
- **Today's Sessions** widget with tabbed interface
- **Attendance Summary** with color-coded progress bars
- **Learning Hours Tracker** with SVG gauge chart
- **Payment Details** with tabs (Due Payment, History, Scholarship)
- **Comprehensive Profile** with academic progress tracking
- **Full-Featured Timetable** (Day/Week/Month/Agenda views)

### 👨‍💼 Admin Portal
- Complete dashboard with system statistics
- Manage students, faculty, and courses
- Fee management and payment tracking
- Excel bulk upload for students
- Comprehensive reporting system
- Announcements management

### 👨‍🏫 Faculty Portal
- View assigned courses
- Mark student attendance
- Manage grades and assessments
- Generate student reports

## 🎨 Modern UI Features

- **Responsive Design** (Mobile, Tablet, Desktop)
- **Smooth Animations** (0.3s ease transitions)
- **Color-Coded System** (Green ≥75%, Yellow ≥60%, Red <60%)
- **Skeleton Loading Screens** for better UX
- **Tabbed Interfaces** for organized content
- **Progress Bars & Gauges** for visual data
- **Professional Gradients** and modern styling

## 🛠️ Technology Stack

- **Backend**: Python 3.13, Flask 3.0.0
- **Database**: MySQL 8.0
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Template Engine**: Jinja2
- **Additional**: Pandas (Excel upload), openpyxl

## 📦 Installation & Setup

### Prerequisites
- Python 3.7+
- MySQL 8.0+
- pip package manager

### Quick Start (5 Minutes)

#### 1. Database Setup
```sql
-- Open MySQL and run:
source C:/Coding/Student_Management_System/database/01_schema.sql;
source C:/Coding/Student_Management_System/database/02_sample_data.sql;
source C:/Coding/Student_Management_System/database/03_procedures_functions.sql;
```

#### 2. Install Dependencies
```powershell
cd C:\Coding\Student_Management_System
pip install flask mysql-connector-python pandas openpyxl
```

#### 3. Configure Database
Edit `backend/database.py`:
```python
self.password = 'YOUR_MYSQL_PASSWORD'  # Change this!
```

#### 4. Run Application
```powershell
python backend/app.py
```

Visit: **http://127.0.0.1:5000**

## 🔑 Default Login Credentials

| Role    | Username      | Password    |
|---------|---------------|-------------|
| Admin   | admin         | admin123    |
| Student | john.student  | pass123     |
| Faculty | dr.smith      | faculty123  |

## 📁 Project Structure

```
Student_Management_System/
├── backend/
│   ├── app.py              # Flask routes (50+ routes)
│   └── database.py         # Database connection class
│
├── templates/
│   ├── base_student.html   # Student portal layout
│   ├── admin/              # Admin templates (15 files)
│   ├── student/            # Student templates (6 files)
│   │   ├── dashboard_new.html  # Modern dashboard
│   │   ├── profile.html        # Student profile with tabs
│   │   └── timetable.html      # Calendar with 4 views
│   └── faculty/            # Faculty templates
│
├── static/
│   └── css/
│       └── student_portal.css  # Modern UI styles (850+ lines)
│
├── database/
│   ├── 01_schema.sql       # 10+ tables, relationships
│   ├── 02_sample_data.sql  # Sample data
│   └── 03_procedures_functions.sql  # Stored procedures
│
├── .vscode/
│   └── settings.json       # VS Code configuration
│
├── README.md               # This file
├── QUICK_START.md          # Quick setup guide
└── IMPLEMENTATION_SUMMARY.md  # Detailed feature docs
```

## 🗄️ Database Schema

### Core Tables (10)
1. **Users** - Authentication for all roles
2. **Students** - Student information
3. **Faculty** - Faculty details
4. **Courses** - Course catalog
5. **Departments** - Department management
6. **Enrollment** - Student-course enrollment
7. **Attendance** - Attendance records
8. **Grades** - Assessment scores
9. **Fees** - Fee management
10. **Fee_Payments** - Payment tracking

### Stored Procedures
- `sp_AddStudent` - Add student with user account
- `sp_EnrollStudent` - Enroll in course
- `sp_MarkAttendance` - Record attendance
- `sp_AddGrade` - Add grades
- `sp_CalculateGPA` - Calculate GPA
- `sp_GetStudentReport` - Generate reports

## 🎯 Student Portal Features

### Dashboard
- **4 KPI Cards**: Total Credits, Active Courses, Avg Attendance, Avg Performance
- **Sidebar Profile**: Avatar, Student ID, Status badge
- **Mini Calendar**: Interactive monthly calendar
- **Today's Sessions**: Time, room, faculty, "Enter Classroom" button
- **Attendance Summary**: Per-course progress with color coding
- **Learning Hours**: Circular gauge chart (SVG)
- **Payment Details**: Tabbed widget with payment info
- **Legend**: Class type indicators (Classroom/Hybrid/Virtual)

### Profile Page
- **Tabbed Interface**: Student Info / Program Progress
- **6 Info Sections**: Program, Student, Academic, Parent, Address, Photo
- **Progress Tracking**: Overall, semester, attendance with bars
- **Semester History**: Status badges for all semesters
- **Skeleton Loading**: 800ms animated loading screen

### Timetable
- **4 View Modes**: Day (timeline), Week (grid), Month (calendar), Agenda (list)
- **Calendar Controls**: Export PDF, view toggles, navigation
- **Color-Coded Events**: Blue (Classroom), Orange (Hybrid), Green (Virtual)
- **Event Details**: Time, course, room, faculty, type
- **Dynamic Rendering**: JavaScript-powered calendar

## 🎨 Design Highlights

### Collapsible Sidebar
```javascript
// Click hamburger → Toggle sidebar
// Smooth 0.3s animation
// State persists in localStorage
Expanded: 250px (Icon + Text)
Collapsed: 70px (Icon only)
```

### Color System
```css
Green:  ≥75% (Good attendance/performance)
Yellow: ≥60% (Warning)
Red:    <60% (Critical)
Blue:   Primary actions
```

### Animations
- Sidebar collapse/expand (0.3s ease)
- Tab switching (fade-in 0.3s)
- Progress bar fills (0.6s ease)
- Hover effects (lift + shadow)
- Skeleton loading (pulse 1.5s)

## 📱 Responsive Design

```
Desktop (1024px+):  Full grid, 6-column layout
Tablet (768-1024):  Stacked cards, 2-column grid
Mobile (<768px):    Single column, slide-in sidebar
Small (<480px):     Compact header, icon-only nav
```

## 🚀 Advanced Features

### Excel Bulk Upload
- Upload student data via Excel file
- Template download available
- Validates data before import
- Creates user accounts automatically

### Dynamic Reporting
- Student performance reports
- Attendance reports (by student/course)
- Grade reports with GPA
- Fee collection reports

### Calendar System
- Week view with time slots
- Month view with event pills
- Day view with timeline
- Agenda view with list
- Export to PDF (placeholder)

## 📊 Usage Examples

### Admin Tasks
```
1. Login → Admin Dashboard
2. Manage Students → Add New Student
3. Upload Excel → Select file → Import
4. Manage Fees → Add Fee Record
5. Reports → Generate Report
```

### Student Tasks
```
1. Login → Modern Dashboard
2. View KPI cards (Credits, Attendance)
3. Check Today's Sessions
4. Navigate → Timetable (Switch views)
5. Profile → View academic progress
```

### Faculty Tasks
```
1. Login → Faculty Dashboard
2. View Assigned Courses
3. Mark Attendance → Select Course
4. Add Grades → Enter marks
```

## 🔧 Troubleshooting

### CSS Linting Errors
**Issue**: VS Code shows CSS errors in templates  
**Solution**: Already configured in `.vscode/settings.json`  
**Action**: Reload VS Code (Ctrl+Shift+P → "Reload Window")

### Database Connection
**Error**: `Can't connect to MySQL server`  
**Fix**:
1. Check MySQL is running
2. Verify credentials in `backend/database.py`
3. Ensure database `student_management_system` exists

### Port Conflict
**Error**: `Address already in use`  
**Fix**: Change port in `app.py`
```python
app.run(debug=True, port=5001)  # Use different port
```

### Module Not Found
**Error**: `ModuleNotFoundError: No module named 'flask'`  
**Fix**:
```powershell
pip install flask mysql-connector-python pandas openpyxl
```

## 📚 Documentation

- **README.md** (this file) - Project overview
- **QUICK_START.md** - 5-minute setup guide
- **IMPLEMENTATION_SUMMARY.md** - Complete feature documentation (30+ pages)

## 🎓 Academic Project Info

- **Course**: Database Management Systems
- **Student**: Pranvkumar Kshirsagar
- **SAP ID**: 590011587
- **University**: UPES
- **Year**: 2025

## 🌟 Highlights

✅ **50+ Flask Routes** with complete CRUD operations  
✅ **10+ Database Tables** with relationships  
✅ **6 Stored Procedures** for complex queries  
✅ **Modern UI** matching UPES portal design  
✅ **Responsive** across all devices  
✅ **Dynamic Sidebar** with smooth animations  
✅ **Color-Coded** visual feedback  
✅ **Tabbed Interfaces** for organized content  
✅ **Skeleton Loading** for better UX  
✅ **Excel Import** for bulk data  
✅ **Full Calendar** with 4 view modes  
✅ **Production Ready** code quality  

## 🔮 Future Enhancements

- Email notifications for announcements
- PDF report generation (grades, transcripts)
- Online exam module
- Discussion forums per course
- Document upload/download
- Mobile app (React Native)
- Real-time notifications (WebSockets)
- Advanced analytics dashboard

## 📄 License

Educational use only. Created for DBMS course project.

## 📧 Contact

For questions or issues:
- GitHub: @Pranvkumar
- Email: pranvkumar.11587@stu.upes.ac.in

---

**Last Updated**: November 6, 2025  
**Version**: 2.0.0  
**Status**: ✅ Production Ready
