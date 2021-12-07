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
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def pre_tax_price(self):
        return self._pre_tax_price
    
    @pre_tax_price.setter
    def pre_tax_price(self, pre_tax_price):
        self._pre_tax_price = pre_tax_price

    @property
    def taxed_price(self):
        return self._taxed_price
    
    @taxed_price.setter
    def taxed_price(self, taxed_price):
        self._taxed_price = taxed_price

    @property
    def applicable_discount(self):
        return self._applicable_discount
    
    @applicable_discount.setter
    def applicable_discount(self, applicable_discount):
        self._applicable_discount = applicable_discount


    # Applies discount by how_many times only if commanded by a SeniorDealer 
    def apply_discount(self, dealer, how_many = 1) -> None:
        if dealer.isSenior:
            self.taxed_price -=self.taxed_price * self.applicable_discount * how_many
        else: print("You can't apply a discount if you're not a senior dealer!")

@dataclass
class Car(Vehicle):
    auto_gearbox: bool
    driving_wheels: str

    @property
    def auto_gearbox(self):
        return self._auto_gearbox
    
    @auto_gearbox.setter
    def auto_gearbox(self, auto_gearbox):
        self._auto_gearbox  = auto_gearbox

    @property
    def driving_wheels(self):
        return self._driving_wheels
    
    @driving_wheels.setter
    def driving_wheels(self, driving_wheels):
        self._driving_wheels  = driving_wheels


@dataclass
class Truck(Vehicle):
    weight: int
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        self._weight  = weight


@dataclass
class Bike(Vehicle):
    engine_displacement: int
    
    @property
    def engine_displacement(self):
        return self._engine_displacement
    
    @engine_displacement.setter
    def engine_displacement(self, engine_displacement):
        self._engine_displacement  = engine_displacement


@dataclass
class Dealer:
    name: str
    sales: list
    isSenior: bool

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name  = name

    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self, sales):
        self._sales  = sales

    @property
    def isSenior(self):
        return self._isSenior
    
    @isSenior.setter
    def isSenior(self, isSenior):
        self._isSenior  = isSenior

    def call_for_discount(name):
        pass

    def grant_discount(self, vehicle: Vehicle, num: int) -> Vehicle:
        if self.isSenior:
            vehicle.apply_discount(self, num)
            print(f"This {vehicle.model} now costs {vehicle.taxed_price}.")
            return vehicle
        else: 
            print("You are not allowed to do that!")
            return vehicle


@dataclass
class Sale:
    vehicle: Vehicle
    dealer: Dealer
    seniorDealer: bool = False

    @property
    def vehicle(self):
        return self._vehicle
    
    @vehicle.setter
    def vehicle(self, vehicle: Vehicle):
        self._vehicle  = vehicle

    @property
    def dealer(self):
        return self._dealer
    
    @dealer.setter
    def dealer(self, dealer):
        self._dealer  = dealer

    @property
    def seniorDealer(self):
        return self._seniorDealer
    
    @seniorDealer.setter
    def seniorDealer(self, seniorDealer):
        self._seniorDealer  = seniorDealer

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
        return self._adress
    
    @adress.setter
    def adress(self, adress):
        self._adress  = adress
    
    @property
    def siret_number(self):
        return self._siret_number
    
    @siret_number.setter
    def siret_number(self, siret_number):
        self._siret_number  = siret_number
    
    @property
    def inventory(self):
        return self._inventory
    
    @inventory.setter
    def inventory(self, inventory):

        self._inventory  = inventory
    
    @property
    def dealers(self):
        return self._dealers
    
    @dealers.setter
    def dealers(self, dealers):
        self._dealers  = dealers

    def vehicles_by_brand(self, brand):
        count = 0
        for elmt in self.inventory:
            if brand.lower() == elmt.brand.lower():
                count += 1
        return count

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