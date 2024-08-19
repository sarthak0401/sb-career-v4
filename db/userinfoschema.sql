-- CREATE USER 'admin'@'%' IDENTIFIED BY 'adminpass';
-- GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
-- FLUSH PRIVILEGES;


CREATE TABLE userinfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_id_no INT NOT NULL,
    job_title VARCHAR(500) NOT NULL,
    applicant_name VARCHAR(500) NOT NULL,
    applicant_email VARCHAR(500) NOT NULL,
    applicant_phno VARCHAR(500) NOT NULL,
    resume LONGBLOB NOT NULL,
    resumeFilename VARCHAR(100) NOT NULL,
    coverletter TEXT NOT NULL
);

