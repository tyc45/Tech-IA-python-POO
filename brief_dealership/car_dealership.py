from numpy import where
from dataclasses import dataclass

@dataclass
class Vehicle:
    color: str
    brand: str
    model: str
    pre_tax_price: float
    taxed_price: float
    applicable_discount: float

    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, color):
        self.color = color
    
    @property
    def brand(self):
        return self.brand
    
    @brand.setter
    def brand(self, brand):
        self.brand = brand
    
    @property
    def model(self):
        return self.model
    
    @model.setter
    def model(self, model):
        self.model = model

    @property
    def pre_tax_price(self):
        return self.pre_tax_price
    
    @pre_tax_price.setter
    def pre_tax_price(self, pre_tax_price):
        self.pre_tax_price = pre_tax_price

    @property
    def taxed_price(self):
        return self.taxed_price
    
    @taxed_price.setter
    def taxed_price(self, taxed_price):
        self.taxed_price = taxed_price

    @property
    def applicable_discount(self):
        return self.applicable_discount
    
    @applicable_discount.setter
    def applicable_discount(self, applicable_discount):
        self.applicable_discount = applicable_discount


    # Applies discount by how_many times only if commanded by a SeniorDealer 
    def apply_discount(self, dealer, how_many = 1) -> None:
        if isinstance(dealer, SeniorDealer):
            self.taxed_price = self.taxed_price - (self.taxed_price * self.applicable_discount * how_many)
        else: print("You can't apply a discount if you're not a senior dealer!")

@dataclass
class Car(Vehicle):
    auto_gearbox: bool
    driving_wheels: str

    @property
    def auto_gearbox(self):
        return self.auto_gearbox
    
    @auto_gearbox.setter
    def auto_gearbox(self, auto_gearbox):
        self.auto_gearbox  = auto_gearbox

    @property
    def driving_wheels(self):
        return self.driving_wheels
    
    @driving_wheels.setter
    def driving_wheels(self, driving_wheels):
        self.driving_wheels  = driving_wheels


@dataclass
class Truck(Vehicle):
    weight: int
    
    @property
    def weight(self):
        return self.weight
    
    @weight.setter
    def weight(self, weight):
        self.weight  = weight


@dataclass
class Bike(Vehicle):
    engine_displacement: int
    
    @property
    def engine_displacement(self):
        return self.engine_displacement
    
    @engine_displacement.setter
    def engine_displacement(self, engine_displacement):
        self.engine_displacement  = engine_displacement


@dataclass
class Dealer:
    name: str
    sales: list

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name  = name

    @property
    def sales(self):
        return self.sales
    
    @sales.setter
    def sales(self, sales):
        self.sales  = sales
    
    def call_for_discount(name):
        pass


@dataclass
class SeniorDealer(Dealer):
    def grant_discount(self, vehicle: Vehicle, num: int) -> Vehicle:
        vehicle.apply_discount(self, num)
        return vehicle


@dataclass
class Sale:
    vehicle: Vehicle
    dealer: Dealer
    seniorDealer = None

    @property
    def vehicle(self):
        return self.vehicle
    
    @vehicle.setter
    def vehicle(self, vehicle: Vehicle):
        self.vehicle  = vehicle

    @property
    def dealer(self):
        return self.dealer
    
    @dealer.setter
    def dealer(self, dealer):
        self.dealer  = dealer

    @property
    def seniorDealer(self):
        return self.seniorDealer
    
    @seniorDealer.setter
    def seniorDealer(self, seniorDealer):
        self.seniorDealer  = seniorDealer

    def export_to_pdf(self):
        pass


@dataclass
class Dealership:
    adress: str
    siret_number: str
    inventory: list
    dealers: list

    @property
    def adress(self):
        return self.adress
    
    @adress.setter
    def adress(self, adress):
        self.adress  = adress
    
    @property
    def siret_number(self):
        return self.siret_number
    
    @siret_number.setter
    def siret_number(self, siret_number):
        self.siret_number  = siret_number
    
    @property
    def inventory(self):
        return self.inventory
    
    @inventory.setter
    def inventory(self, inventory):

        self.inventory  = inventory
    
    @property
    def dealers(self):
        return self.dealers
    
    @dealers.setter
    def dealers(self, dealers):
        self.dealers  = dealers

    def vehicles_by_brand(self, brand):
        return range(where(self.inventory) == brand)

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle): self.inventory.append(vehicle)

    def sell_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            print("Error, didn't ask for a vehicle!")
            pass

        if vehicle in self.inventory:
            self.inventory.remove(vehicle)
            return vehicle
        else:
            print("Could not find vehicle, please check our stock")