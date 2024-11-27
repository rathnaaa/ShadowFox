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

# Child class: Apple (Inherits from MobilePhone)
class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        # Apple phones always have Touch Screen, 4G/5G, and True Dual Sim by default
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)

    def display_brand(self):
        return "This is an Apple Mobile Phone."

# Child class: Samsung (Inherits from MobilePhone)
class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        # Samsung phones also have Touch Screen, 4G/5G, and may or may not have Dual Sim
        super().__init__("Touch Screen", "4G/5G", True, front_camera, rear_camera, ram, storage)

    def display_brand(self):
        return "This is a Samsung Mobile Phone."

# Create an Apple phone object
apple_phone = Apple("12MP", "48MP", "4GB", "64GB")

# Create a Samsung phone object
samsung_phone = Samsung("8MP", "32MP", "3GB", "32GB")

# Display specs of Apple phone
print("Apple Phone Specs:")
print(apple_phone.display_specs())
print(apple_phone.display_brand())
print()

# Display specs of Samsung phone
print("Samsung Phone Specs:")
print(samsung_phone.display_specs())
print(samsung_phone.display_brand())
