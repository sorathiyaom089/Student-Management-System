<?php
/*
 * Student Management System
 * Database Configuration Template
 * 
 * Instructions:
 * 1. Rename this file to 'db_config.php'
 * 2. Update the database credentials below
 * 3. Save the file
 * 
 * Note: This file will be created automatically during installation
 */

// Database Configuration
define('DB_HOST', 'localhost');          // Database host (usually localhost)
define('DB_NAME', 'student_management'); // Database name
define('DB_USER', 'root');               // Database username
define('DB_PASS', '');                   // Database password
define('DB_CHARSET', 'utf8mb4');         // Character set

// Application Configuration
define('APP_NAME', 'Student Management System');
define('APP_VERSION', '2.0');
define('APP_URL', 'http://localhost/student-management/');

// Security Configuration
define('HASH_ALGO', 'sha256');           // Password hashing algorithm
define('SESSION_TIMEOUT', 3600);        // Session timeout in seconds (1 hour)

// File Upload Configuration
define('MAX_FILE_SIZE', 5242880);       // 5MB in bytes
define('UPLOAD_PATH', 'upload/');       // Upload directory
define('ALLOWED_EXTENSIONS', 'jpg,jpeg,png,pdf,doc,docx');

// SMS Configuration (Optional)
define('SMS_GATEWAY', '');              // SMS gateway URL
define('SMS_API_KEY', '');              // SMS API key
define('SMS_SENDER_ID', '');            // SMS sender ID

// Error Reporting (Set to false in production)
define('DEBUG_MODE', true);

// Time Zone
date_default_timezone_set('Asia/Dhaka'); // Change according to your location

// Database Connection Test
function testDatabaseConnection() {
    try {
        $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($connection->connect_error) {
            return false;
        }
        
        $connection->close();
        return true;
    } catch (Exception $e) {
        return false;
    }
}

// Installation Check
function isInstalled() {
    return file_exists(__DIR__ . '/config/install.lock');
}

// Create Installation Lock File
function createInstallLock() {
    $lockFile = __DIR__ . '/config/install.lock';
    $lockData = [
        'installed_on' => date('Y-m-d H:i:s'),
        'version' => APP_VERSION,
        'php_version' => PHP_VERSION,
        'mysql_version' => 'Detected during installation'
    ];
    
    return file_put_contents($lockFile, json_encode($lockData, JSON_PRETTY_PRINT));
}

?>