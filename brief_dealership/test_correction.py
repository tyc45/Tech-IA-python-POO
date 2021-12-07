import pytest
from correction import Vehicule, Magasin, Vente, Seller

@pytest.fixture
def vehicule_test():
    return Vehicule("Yaris", "Toyota", "Rose", 20000, 10)

@pytest.fixture
def magasin_test(senior_seller_test, seller_test, vehicule_test):
    temp = [
        vehicule_test,
        Vehicule("Bleu","Peugeot","1008", 30000, 15),
        Vehicule("Vert","Peugeot","305", 2000, 5),
        Vehicule("Bleu","Renault","Megane", 25000, 20),
        Vehicule("Gris","Audi","A3", 40000, 30)]
    return Magasin("47 rue Bathelemy Delespaul", "11256894618963")

@pytest.fixture
def senior_seller_test(magasin_test):
    return Seller("Henri", magasin_test, senior = True)

@pytest.fixture
def seller_test(magasin_test):
    return Seller("Billy", magasin_test)


class TestVehicule:
    def test_final_price(self, vehicule_test:Vehicule):
        assert vehicule_test.final_price(True) == 21600
        assert vehicule_test.final_price(False) == 24000

class TestMagasin:
    def test_add_vehicle(self, magasin_test:Magasin, vehicule_test:Vehicule):
        assert magasin_test.add_vehicle(vehicule_test) == [vehicule_test]