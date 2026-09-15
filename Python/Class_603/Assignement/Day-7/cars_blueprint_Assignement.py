class car:
    def __init__(self, name, brand, speed):
        self.Car_name = name
        self.Car_brand = brand
        self.Car_TopSpeed = speed
        print(f"This is {self.Car_name} from {self.Car_brand} with a Top Speed of {self.Car_TopSpeed} km/h".center(80))
        
    def display_info(self):
        print('*'*80)    
        print(f"Car Name     : {self.Car_name}".center(80))
        print(f"Car Brand    : {self.Car_brand}".center(80))
        print(f"Top Speed    : {self.Car_TopSpeed} km/h".center(80))
        print('*'*80)    
        
    def car_engine(self, eng_name):
        print('-'*80)
        print("Car Engine Details".center(80))
        self.Car_Engine = eng_name
        print(f"{self.Car_name} has {self.Car_Engine}".center(80))
        print('-'*80)
        
    def car_stereo(self):
        print('+'*80)
        print("Car Stereo".center(80))
        print(f"{self.Car_name} is playing music on its stereo.".center(80))
        print('+'*80)


print('*'*80)
print("Creating Objects".center(80,'-'))   

porsche = car("Porsche 911", "Porsche", 330)
mustang = car("Mustang GT", "Ford", 250)
supra   = car("Toyota Supra", "Toyota", 250)
bmw     = car("BMW M5 Competition", "BMW", 305)

print('*'*80)      
print("Car Info (Objects Created)".center(80,'-'))

porsche.display_info() 
porsche.car_engine("3.0L Twin-Turbo Flat-6")
porsche.car_stereo()

bmw.display_info()
bmw.car_engine("4.4L Twin-Turbo V8")
bmw.car_stereo()
  
supra.display_info()
supra.car_engine("3.0L Turbocharged Inline-6")
supra.car_stereo()

mustang.display_info()
mustang.car_engine("5.0L V8")
mustang.car_stereo()
