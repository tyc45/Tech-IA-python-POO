class Vehicle:
    def __init__(self, color, brand, model, pre_tax_price, taxed_price, applicable_discount) -> None:
        pass

    def apply_discount(self, dealer, how_many = 1):
        pass

class Car(Vehicle):
    def __init__(self, color, brand, model, pre_tax_price, taxed_price, applicable_discount, auto_gearbox, driving_wheels) -> None:
        super().__init__(color, brand, model, pre_tax_price, taxed_price, applicable_discount)
        pass

class Truck(Vehicle):
    def __init__(self, color, brand, model, pre_tax_price, taxed_price, applicable_discount, weight) -> None:
        super().__init__(color, brand, model, pre_tax_price, taxed_price, applicable_discount)

class Motorcycle(Vehicle):
    def __init__(self, color, brand, model, pre_tax_price, taxed_price, applicable_discount) -> None:
        super().__init__(color, brand, model, pre_tax_price, taxed_price, applicable_discount)

class Dealer:
    def __init__(self, name, sales) -> None:
        pass
    
    def call_for_discount(name):
        pass

class SeniorDealer(Dealer):
    def grant_discount(Sale, num):
        pass

class Sale:
    def __init__(self, vehicle, dealer, seniorDealer = None) -> None:
        pass

    def export_to_pdf():
        pass

class Dealership:
    def __init__(self, adress, siret_number, inventory, dealers) -> None:
        pass

    def vehicles_by_brand(brand):
        pass

    def add_vehicle(vehicle):
        pass

    def sell_vehicle(vehicle):
        pass