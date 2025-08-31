# python-OOP-assignment

Python OOP Assignment 🐍
Overview

This project demonstrates OOP in Python with:

Smartphone Class – Base class with attributes like brand, model, battery_capacity and methods to make_call() and charge().

GamingPhone subclass adds cooling_system and play_game() method.

Polymorphism Challenge – Vehicle classes (Car, Plane, Boat) each implement move() differently.

Example Usage
phone1 = Smartphone("Apple", "iPhone 15", 4000)
phone1.make_call(10)

gaming_phone = GamingPhone("Asus", "ROG 7", 6000, "Advanced Cooling")
gaming_phone.play_game(3)

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
v.move()

Expected Output:

Calling for 10 minutes...
Playing games for 3 hours...
Driving on the road 🚗
Flying in the sky ✈️
Sailing on the water ⛵

Concepts Covered

Constructors – Initialize objects

Inheritance – Extend base classes

Encapsulation – Manage object state via methods

Polymorphism – Same method, different behavior

Author

Fadhili Anicetus
