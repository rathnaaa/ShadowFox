# Base class: MobilePhone
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        return f"Screen Type: {self.screen_type}\n" \
               f"Network Type: {self.network_type}\n" \
               f"Dual Sim: {self.dual_sim}\n" \
               f"Front Camera: {self.front_camera}\n" \
               f"Rear Camera: {self.rear_camera}\n" \
               f"RAM: {self.ram}\n" \
               f"Storage: {self.storage}"

    def make_call(self, number):
        return f"Calling {number}..."

    def receive_call(self, number):
        return f"Receiving call from {number}..."

    def take_a_picture(self):
        return f"Taking a picture with {self.rear_camera} camera..."

# Child class: Apple (Inherits from MobilePhone)
class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)

    def display_brand(self):
        return "This is an Apple Mobile Phone."

# Child class: Samsung (Inherits from MobilePhone)
class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)

    def display_brand(self):
        return "This is a Samsung Mobile Phone."


# Creating Apple phone objects with different properties
apple_phone1 = Apple("12MP", "48MP", "4GB", "64GB")
apple_phone2 = Apple("8MP", "16MP", "3GB", "32GB")

# Creating Samsung phone objects with different properties
samsung_phone1 = Samsung("10MP", "32MP", "6GB", "128GB")
samsung_phone2 = Samsung("5MP", "13MP", "2GB", "16GB")

# Displaying specs of Apple phones
print("Apple Phone 1 Specs:")
print(apple_phone1.display_specs())
print(apple_phone1.display_brand())
print(apple_phone1.make_call("123-456-7890"))
print(apple_phone1.receive_call("987-654-3210"))
print(apple_phone1.take_a_picture())
print()

print("Apple Phone 2 Specs:")
print(apple_phone2.display_specs())
print(apple_phone2.display_brand())
print(apple_phone2.make_call("555-555-5555"))
print(apple_phone2.receive_call("111-222-3333"))
print(apple_phone2.take_a_picture())
print()

# Displaying specs of Samsung phones
print("Samsung Phone 1 Specs:")
print(samsung_phone1.display_specs())
print(samsung_phone1.display_brand())
print(samsung_phone1.make_call("123-456-7890"))
print(samsung_phone1.receive_call("987-654-3210"))
print(samsung_phone1.take_a_picture())
print()

print("Samsung Phone 2 Specs:")
print(samsung_phone2.display_specs())
print(samsung_phone2.display_brand())
print(samsung_phone2.make_call("555-555-5555"))
print(samsung_phone2.receive_call("111-222-3333"))
print(samsung_phone2.take_a_picture())
