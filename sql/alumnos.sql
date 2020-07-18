CREATE DATABASE alumnos;

USE alumnos;

CREATE TABLE students(
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    pri_ap varchar(100) NOT NULL,
    seg_ap varchar(100) NOT NULL,
    age int(10) NOT NULL,
    date date NOT NULL,
    gender varchar(20) NOT NULL,
    state varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO personas(nombre,pri_ap,seg_ap,age,date,gender,state)
VALUES
('Fernando','Hernandez', 'Vazquez', '20','27-01-00', 'masculino','hidalgo');

CREATE USER 'user_alumno'@'localhost' IDENTIFIED BY 'sphinx';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'user_alumno'@'localhost';
FLUSH PRIVILEGES;
