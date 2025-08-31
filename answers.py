# Making the base class
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  
        self.battery_level = 100  

    def make_call(self, minutes):
        print(f"Calling for {minutes} minutes...")
        self.battery_level -= minutes * 1  
        if self.battery_level < 0:
            self.battery_level = 0
        print(f"Battery level: {self.battery_level}%")

    def charge(self):
        self.battery_level = 100
        print("Phone fully charged!")

# Inheritance: Smartphone -> GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_capacity, cooling_system):
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system  

    def play_game(self, hours):
        print(f"Playing games for {hours} hours...")
        self.battery_level -= hours * 5 
        if self.battery_level < 0:
            self.battery_level = 0
        print(f"Battery level: {self.battery_level}%")
phone1 = Smartphone("Apple", "iPhone 15", 4000)
phone1.make_call(10)
phone1.charge()

gaming_phone = GamingPhone("Asus", "ROG 7", 6000, "Advanced Cooling")
gaming_phone.play_game(3)
gaming_phone.make_call(5)
