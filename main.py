from customer import Customer
from restaurant import Restaurant
from review import Review

# testing 

Jeremy = Customer("Jeremy", "Keene")
Alice = Customer("Alice", "Smith")
Bob = Customer("Bob", "Johnson")

McDonalds = Restaurant("McDonald's")
PizzaHut = Restaurant("Pizza Hut")

review1 = Review(Jeremy, McDonalds, 4)
review2 = Review(Alice, McDonalds, 5)
review3 = Review(Bob, PizzaHut, 3)
review4 = Review(Jeremy, PizzaHut, 2)

# testing the names
print(Jeremy.full_name())
print(Alice.full_name())
print(Bob.full_name())

# testing the star ratings
print(McDonalds.average_star_rating()) 
print(PizzaHut.average_star_rating())