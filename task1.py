from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USCar(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} (US Spec): Двигун запущено")

class USMotorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} (US Spec): Мотор заведено")

class EUCar(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} (EU Spec): Двигун запущено")

class EUMotorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} (EU Spec): Мотор заведено")

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return USCar(make, model)
    
    def create_motorcycle(self, make, model):
        return USMotorcycle(make, model)
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return EUCar(make, model)
    
    def create_motorcycle(self, make, model):
        return EUMotorcycle(make, model)

factoryUS = USVehicleFactory()
factoryEU = EUVehicleFactory()

vehicle1 = factoryEU.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = factoryUS.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
