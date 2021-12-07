import pytest
from correction import Vehicule, Voiture, Moto, Magasin, Vente, Seller, Camion, Client

@pytest.fixture
def vehicule_test():
    return Vehicule("Yaris", "Toyota", "Rose", 20000, 10)

@pytest.fixture
def senior_seller_test():
    return Seller("Henri", None, None, True)

@pytest.fixture
def seller_test():
    return Seller("Billy", None, None)

@pytest.fixture
def magasin_test(senior_seller_test, seller_test, vehicle_test):
    temp = [
        vehicle_test,
        Vehicule("Bleu","Peugeot","1008", 30000, 15),
        Vehicule("Vert","Peugeot","305", 2000, 5),
        Vehicule("Bleu","Renault","Megane", 25000, 20),
        Vehicule("Gris","Audi","A3", 40000, 30)]
    return Magasin("47 rue Bathelemy Delespaul", "11256894618963", [senior_seller_test, seller_test], temp, 5)

