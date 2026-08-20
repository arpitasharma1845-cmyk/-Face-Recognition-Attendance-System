USE face_recognizer;

CREATE TABLE student (

    student_id INT PRIMARY KEY ,

    roll_no VARCHAR(20) UNIQUE NOT NULL,

    student_name VARCHAR(100) NOT NULL,

    dob DATE NOT NULL,

    gender ENUM('Male','Female','Other') NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(10) NOT NULL,

    address TEXT,

    department VARCHAR(50) NOT NULL,

    course VARCHAR(50) NOT NULL,

    year ENUM(
        '1st Year',
        '2nd Year',
        '3rd Year',
        '4th Year'
    ) NOT NULL,

    semester ENUM(
        'Semester-1',
        'Semester-2',
        'Semester-3',
        'Semester-4',
        'Semester-5',
        'Semester-6',
        'Semester-7',
        'Semester-8'
    ) NOT NULL,

    photo_sample ENUM('Yes','No') DEFAULT 'No',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CHECK (CHAR_LENGTH(phone) = 10),

    CHECK (phone REGEXP '^[0-9]{10}$'),

    CHECK (
        email REGEXP
        '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
    )

);