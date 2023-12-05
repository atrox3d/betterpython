import string
import random
from dataclasses import dataclass


@dataclass
class VehicleInfo:
    """
    describes vehicle informations

    computes taxes based on the fields
    """
    brand: str
    catalogue_price: int
    electric: bool

    def compute_tax(self) -> float:
        """
        comeputes taxes based on electric field
        """
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self) -> None:
        """
        prints brand and taxes
        """
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")    

@dataclass
class Vehicle:
    """
    describes a vehicle with its infos
    """
    id: str
    license_plate: str
    info: VehicleInfo

    def print(self) -> None:
        """
        prints id, licence plate and vehicle_info
        """
        print(f"ID: {self.id}")
        print(f"License PLate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    """
    represents a vehicle registry
    """

    # vehicle info dict
    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price) -> None:
        """
        adds a new VehicleInfo object to the dict
        """
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self) -> None:
        """
        simulate loading of vehicle info from db
        """
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def generate_vehicle_id(self, length: int) -> str:
        """
        creates a random generated ID
        """
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id: str) -> str:
        """
        creates a random license plate
        """
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
    
    def create_vehicle(self, brand: str) -> Vehicle:
        """
        create a new Vehicle
        """
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:

    def __init__(self) -> None:
        pass

    def register_vehicle(self, brand: string) -> Vehicle:
        """
        creates a new VehicleRegistry
        creates and returns a new vehicle from it
        """
        # create a registry instance
        registry = VehicleRegistry()

        return registry.create_vehicle(brand)

if __name__ == '__main__':
    app = Application()
    vehicle = app.register_vehicle("Volkswagen ID3")
    vehicle.print()
