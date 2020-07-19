DROP DATABASE IF EXISTS alumnos;
CREATE DATABASE alumnos;

USE alumnos;

CREATE TABLE students(
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    pri_ap varchar(100) NOT NULL,
    seg_ap varchar(100) NOT NULL,
    age int(10) NOT NULL,
    fdate varchar(10) not null ,
    gender varchar(20) NOT NULL,
    state varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO students(id,nombre,pri_ap,seg_ap,age,fdate,gender,state)
VALUES
('1718110040','Fernando','Hernandez', 'Vazquez', '20','2000/01/27', 'Masculino','hidalgo'),
('1719112255','Guadalupe','Espinoz','Riveros','20','2000/05/04','Femenino','Hidalgo');

/*CREATE USER 'alumno'@'localhost' IDENTIFIED BY 'sphinx';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'user_alumno'@'localhost';
FLUSH PRIVILEGES;*/



