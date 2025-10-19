@echo off
echo ================================================
echo    Student Management System - Setup Script
echo ================================================
echo.

REM Check if PHP is installed
php --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: PHP is not installed or not in PATH
    echo Please install PHP 7.0 or higher and ensure it's in your system PATH
    pause
    exit /b 1
)

echo PHP installation detected...
php --version
echo.

REM Check if MySQL/MariaDB is available
mysql --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: MySQL command line tools not found
    echo Please ensure MySQL/MariaDB is installed and running
    echo You can still proceed with the web-based installation
    echo.
)

REM Get current directory
set PROJECT_DIR=%~dp0

echo Project Directory: %PROJECT_DIR%
echo.

REM Check if we're in a web server directory
if exist "%PROJECT_DIR%index.php" (
    echo index.php found - Project structure looks correct
) else (
    echo WARNING: index.php not found in current directory
    echo Make sure you're running this script from the project root
)

echo.
echo ================================================
echo           INSTALLATION INSTRUCTIONS
echo ================================================
echo.
echo 1. WEB SERVER SETUP:
echo    - If using XAMPP: Copy this folder to xampp/htdocs/
echo    - If using WAMP: Copy this folder to wamp/www/
echo    - If using LAMP: Copy this folder to /var/www/html/
echo    - If using local server: Ensure PHP and MySQL are running
echo.
echo 2. DATABASE SETUP:
echo    - Create a new MySQL database (e.g., 'student_management')
echo    - Note down your database credentials:
echo      * Host (usually 'localhost')
echo      * Database name
echo      * Username
echo      * Password
echo.
echo 3. BROWSER SETUP:
echo    - Open your web browser
echo    - Navigate to: http://localhost/[project-folder-name]/
echo    - Follow the installation wizard
echo.
echo 4. DEFAULT LOGIN (after installation):
echo    - Username: admin
echo    - Password: admin
echo    - IMPORTANT: Change password after first login!
echo.
echo ================================================

REM Try to detect common web server setups
echo           WEB SERVER DETECTION
echo ================================================

if exist "C:\xampp\htdocs" (
    echo XAMPP detected at C:\xampp\htdocs
    echo To install: Copy this folder to C:\xampp\htdocs\student-management
    echo Then visit: http://localhost/student-management/
    echo.
)

if exist "C:\wamp64\www" (
    echo WAMP detected at C:\wamp64\www
    echo To install: Copy this folder to C:\wamp64\www\student-management
    echo Then visit: http://localhost/student-management/
    echo.
)

if exist "C:\laragon\www" (
    echo Laragon detected at C:\laragon\www
    echo To install: Copy this folder to C:\laragon\www\student-management
    echo Then visit: http://localhost/student-management/
    echo.
)

echo ================================================
echo              QUICK START OPTIONS
echo ================================================
echo.
echo Choose an option:
echo [1] Start PHP built-in server (for testing)
echo [2] Open project folder
echo [3] View system requirements
echo [4] Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting PHP built-in server...
    echo Navigate to: http://localhost:8000
    echo Press Ctrl+C to stop the server
    echo.
    cd /d "%PROJECT_DIR%"
    php -S localhost:8000
) else if "%choice%"=="2" (
    echo Opening project folder...
    explorer "%PROJECT_DIR%"
) else if "%choice%"=="3" (
    echo.
    echo ================================================
    echo            SYSTEM REQUIREMENTS
    echo ================================================
    echo.
    echo MANDATORY:
    echo - PHP 7.0 or higher
    echo - MySQL 5.7 or higher (or MariaDB equivalent)
    echo - Web server (Apache/Nginx/IIS)
    echo.
    echo PHP EXTENSIONS REQUIRED:
    echo - mysqli (for database connectivity)
    echo - gd (for image processing)
    echo - session (for user sessions)
    echo.
    echo RECOMMENDED:
    echo - At least 512MB RAM
    echo - 200MB free disk space
    echo - Modern web browser
    echo.
    pause
) else if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Exiting...
    exit /b 1
)

pause