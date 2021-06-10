create Table student(
	ID int,
  	firstname Varchar(40),
  	lastname varchar(40),
  	year_of_study int
);

INSERT INTO student VALUES(1, "Derbes", "Utebaliyev", 4);

SELECT ID, firstname, lastname FROM student;
SELECT * FROM student;
SELECT * FROm student WHERE firstname == "Derbes";
SELECT * FROm student WHERE year_of_study > 2;


UPDATE student SET firstname = "Bagjan" WHERE firstname == "Derbes";


DELETE FROM student Where firstname == "Azamat";

ALTER TABLE student ADD COLUMN faculty VARCHAR(40);
ALTER TABLE student DROP COLUMN faculty;


SELECT * FROM student ORDER BY year_of_study DESC;
SELECT * FROM student ORDER BY year_of_study ASC;


SELECT AVG(year_of_study) FROM student WHERE year_of_study > 1;
SELECT COUNT(year_of_study) FROM student WHERE year_of_study > 1;
SELECT SUM(year_of_study) FROM student WHERE year_of_study > 2;
SELECT MAX(year_of_study) FROM student WHERE year_of_study > 2;
SELECT MIN(year_of_study) FROM student WHERE year_of_study > 2;

SELECT COUNT(faculty), faculty FROM student GROUP By faculty;

SELECT * FROM student WHERE year_of_study >= 2 AND year_of_study <=3;
SELECT * FROM student WHERE year_of_study BETWEEN 2 and 3;

DROP TABLE student;