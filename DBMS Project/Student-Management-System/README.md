# Student Management System

> A comprehensive web-based student management system written in PHP and JavaScript. Designed specifically for educational institutions to manage student information, academic programs, examinations, and administrative activities.

> This system provides a complete solution for educational institutions to streamline their administrative processes.

- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Design](#system-design)
- [Installation](#installation)
- [Usage](#usage)
- [Default Login](#default-login)

## Default Login
- **Username:** admin
- **Password:** admin
- **Note:** Change the default password after first login for security

## Features
- **Student Information Management**: Add, edit, and manage comprehensive student records
- **Multi-Program Enrollment**: Students can be enrolled in multiple academic programs
- **Payment System**: Track fee payments with due date management and payment history
- **Attendance System**: Daily attendance tracking with batch-wise management
- **ID Card Generation**: Generate and print student ID cards with barcode integration
- **Program Management**: Create and manage academic programs and batches
- **Examination System**: Add exams, enter results, and generate automatic rankings
- **SMS Integration**: Send results and notices via SMS
- **Notice Board**: Manage and broadcast important announcements
- **Comprehensive Reporting**: Generate reports for payments, expenses, income, profit, and attendance
- **Activity Logging**: All administrative activities are automatically logged
- **Multi-User Support**: Role-based access control for different user types
- **Theme Customization**: Multiple themes for user interface personalization

## Technology Stack
- **Backend**: PHP 7.0+
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap (Responsive Design)
- **Database**: MySQL 5.7+
- **AJAX**: For dynamic user interactions
- **Server Compatibility**: Apache/Nginx

## System Design
For detailed system architecture, database design, and use cases, please refer to:
- [Complete System Design Documentation](SYSTEM_DESIGN.md)
- [Database ER Diagram](ER_DIAGRAM.md)

## Installation

### Prerequisites
- Web server (Apache/Nginx) with PHP support
- PHP 7.0 or higher with the following extensions:
  - mysqli
  - gd
  - session
- MySQL 5.7 or higher
- Modern web browser with JavaScript enabled

### Installation Steps

1. **Setup Web Server**
   - Place the project files in your web server's document root
   - Ensure proper file permissions for web server access

2. **Database Configuration**
   - Create a new MySQL database for the system
   - Note down database credentials (host, username, password, database name)

3. **Run Installation Wizard**
   - Open your web browser and navigate to the project URL
   - The system will automatically detect if installation is needed
   - Follow the installation wizard steps:
     - Enter database connection details
     - Configure system settings
     - Create administrator account

4. **Complete Installation**
   - Once installation is complete, the system will redirect to login page
   - Use the default credentials or the admin account created during installation

### Post-Installation Security
- Change default administrator password immediately
- Configure system settings according to your institution's requirements
- Set up additional user accounts with appropriate permissions
- Configure SMS gateway if SMS functionality is required

## Usage

### Getting Started
1. **Login**: Use admin credentials to access the system
2. **System Configuration**: Configure institution details in Settings
3. **User Management**: Create additional user accounts for staff
4. **Program Setup**: Add academic programs and batches
5. **Student Registration**: Begin adding student records

### Key Workflows
- **Student Enrollment**: Register → Enroll in Program → Generate ID Card
- **Academic Management**: Create Exams → Enter Results → Generate Reports
- **Financial Tracking**: Record Payments → Track Dues → Generate Financial Reports
- **Communication**: Send SMS Notifications → Post Notices → Monitor Activities

## System Requirements
- **Minimum RAM**: 512MB
- **Storage**: 200MB free space (more for student photos and documents)
- **Network**: Internet connection for SMS functionality (optional)
- **Browser Support**: Chrome, Firefox, Safari, Edge (latest versions)

## Support and Maintenance
- Regular database backups recommended
- Monitor system logs for performance optimization
- Keep PHP and MySQL updated for security
- Regularly review user access permissions

---

*For technical documentation, system architecture details, and database design, refer to the included documentation files.*




