from db_class import Car

cars = Car("Cars.sql")

cars.create_table()
cars.insert_car(1, "BMW", "X5", 1995)
cars.insert_car(2, "Toyota", "Camry", 2020)

cars.select_car()

# connection = create_connection("cars.sql")





