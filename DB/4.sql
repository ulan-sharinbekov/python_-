CREATE TABLE factory(
	ID INT PRIMARY Key,
  	name VARCHAR(40),
  	country VARCHAR(40)
)

create Table car(
	ID INT PRIMARY KEY,
  	model Varchar(40),
  	brand varchar(40),
  	year_ int,
  	factory_id INT,
  	FOREIGN KEY(factory_id) REFERENCES factory(ID)
);

INSERT INTO factory VALUES(3, "BMW", "Germany")
INSERT INTO factory VALUES(1, "Audi", "Germany")
INSERT INTO factory VALUES(2, "Toyota", "Japan")

INSERT INTO car VALUES(4, "A8", "Audi", 2021, 1)
INSERT INTO car VALUES(3, "A6", "Audi", 2020, 1)
INSERT INTO car VALUES(2, "Camry", "Toyota", 2021, 2)
INSERT INTO car VALUES(1, "X5", "BMW", 1995, 3)


SELECT car.ID, car.model, car.brand, car.year_, factory.country From car
    INNER JOIN factory ON car.factory_id = factory.ID;

SELECT * FROM car WHERE brand in
    (SELECT name FROM factory WHERE country == "Germany");