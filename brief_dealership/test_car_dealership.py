import pytest
from car_dealership import Vehicle, Car, Truck, Bike, Dealer, SeniorDealer, Sale, Dealership

@pytest.fixture
def vehicle_test():
   return Vehicle("Rouge","Toyota","Yaris", 16000, 18000, 0.1)

@pytest.fixture
def senior_dealer_test():
    return SeniorDealer("George", [])
    
@pytest.fixture
def dealer_test():
    return Dealer("Corentin", [])

@pytest.fixture
def sale_test():
    return Sale(vehicle_test(), dealer_test())

@pytest.fixture
def car_list():
    return [
        vehicle_test, 
        Vehicle("Bleu","Peugeot","1008", 30000, 32000, 0.15),
        Vehicle("Vert","Peugeot","305", 2000, 2100, 0.05),
        Vehicle("Bleu","Renault","Megane", 25000, 26000, 0.20),
        Vehicle("Gris","Audi","A3", 40000, 45000, 0.30)
    ]

@pytest.fixture
def dealership_test():
    return Dealership("47 rue Bathelemy Delespaul", "36252187900034", car_list(), [dealer_test, senior_dealer_test])

class TestVehicle:
    def test_apply_discount(self, vehicle_test: Vehicle):
        assert vehicle_test.apply_discount(senior_dealer_test, 1) == 16200
    
    def test_apply_discount_two(self, vehicle_test: Vehicle):
        assert vehicle_test.apply_discount(senior_dealer_test, 2) == 14400
    
    def test_apply_discount_three(self, vehicle_test: Vehicle):
        assert vehicle_test.apply_discount(senior_dealer_test, 1) == 12600



# class TestDealer:
#     def test_call_for_discount(self):
#         pass

class TestSeniorDealer:
    def test_grant_discount(self, senior_dealer_test: SeniorDealer, vehicle_test: Vehicle):
        assert senior_dealer_test.grant_discount(vehicle_test, 1).taxed_price == 16200
    
    def test_grant_discount_two(self, senior_dealer_test: SeniorDealer, vehicle_test: Vehicle):
        assert senior_dealer_test.grant_discount(vehicle_test, 1).taxed_price == 14400
    
    def test_grant_discount_three(self, senior_dealer_test: SeniorDealer, vehicle_test: Vehicle):
        assert senior_dealer_test.grant_discount(vehicle_test, 1).taxed_price == 12600




# class TestSale:
#     def test_export_to_pdf():
#         pass


class TestDealership:
    def test_vehicles_by_brand(self, dealership_test: Dealership):
        assert dealership_test.vehicles_by_brand("Renault") == 2

    def test_vehicles_by_brand_two(self, dealership_test: Dealership):
        assert dealership_test.vehicles_by_brand("Toyota") == 1

    def test_vehicles_by_brand_three(self, dealership_test: Dealership):
        assert dealership_test.vehicles_by_brand("Hyundai") == 0