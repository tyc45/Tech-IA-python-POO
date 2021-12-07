from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta, abstractmethod
from fpdf import FPDF

@dataclass
class Vehicule(metaclass = ABCMeta):
    modele : str
    marque :str
    couleur :str
    prix_HT :int
    reduction :int
    _prix_TTC: float = field(init=False)
  

    def __post_init__(self):
        self._prix_TTC : float = self._get_prix_TTC()

    @property
    def prix_TTC(self) -> float:
        return self._prix_TTC

    @property
    def reduction(self) -> int:
        return self._reduction

    @reduction.setter
    def reduction(self, value):
        if type(value) != int:
            raise ValueError("Reduction should be an int")
        elif value > 100 or value < 0:
            raise ValueError("Reduction should be between 0 et 100")
        else:
            self._reduction = value

    @property
    def prix_HT(self) -> int:
        return self._prix_HT   


    @prix_HT.setter
    def prix_HT(self, value):
        if type(value) != int:
            raise ValueError("Prix should be an integer")
        else:
            self._prix_HT = value
            self._prix_TTC = self._get_prix_TTC()

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, value):
        if type(value) != str:
            raise ValueError("Marque should be a str")
        else:
            self._marque = value

    @property
    def couleur(self) -> str:
        return self._couleur

    @couleur.setter
    def couleur(self, value):
        if type(value) != str:
            raise ValueError("Couleur should be a str")
        else:
            self._couleur = value

    def _get_prix_TTC(self):
        return self.prix_HT * 1.2

    def final_price(self,reduction:bool):
        if reduction:
            return self.prix_TTC * (1 - self.reduction/100)
        else:
            return self.prix_TTC


@dataclass
class Voiture(Vehicule):
    roues : ClassVar[int] = 4
    type : ClassVar[str] = "Voiture"

@dataclass
class Moto(Vehicule):
    roues : ClassVar[int] = 2
    type : ClassVar[str] = "Moto"
  


@dataclass
class Camion(Vehicule):
    roues : ClassVar[int]
    type : ClassVar[str] = "Camion"



# print(my_car.prix_TTC)
# my_car.prix_HT = 200
# print(my_car.prix_HT)
# print(my_car.prix_TTC)
# my_car.prix_TTC = 20
# print(my_car.prix_HT)
# print(my_car.prix_TTC)

@dataclass
class Magasin():
    adresse: str 
    siret: str
    _seller_list: list = field(default_factory=list)
    _inventory: list = field(default_factory=list)
    _stock: dict = field(default_factory=dict)
    
    @property
    def seller_list(self) -> list:
        return self._seller_list
        
    @property
    def inventory(self) -> list:
        return self._inventory

    @property
    def stock(self) -> dict:
        return self._stock
      
    def get_vehicle_brand_count(self, marque):
        return self._stock[marque]

    def add_vehicle(self, vehicle):
        self._inventory.append(vehicle)
        if vehicle.marque not in self.stock:
            self._stock[vehicle.marque] = 0
        self._stock[vehicle.marque] += 1
        print(f"la {vehicle.marque} a été ajoutée à l'inventaire")
        return self._inventory
    
    def delete_vehicle(self, vehicle):
        self._inventory.remove(vehicle)
        self._stock[vehicle.marque] -= 1
        print(f"la {vehicle.marque} a été retirée de l'inventaire")
        return self.inventory
    
    def add_seller(self, full_name:str, senior:bool):
        seller = Seller(full_name,self,senior=senior)
        self._seller_list.append(seller)
        print(f"le vendeur {seller.full_name} a été recruté")
        return self._seller_list
    
    def delete_seller(self, seller):
        self._seller_list.remove(str(seller))
        print(f"le vendeur {seller.full_name} a été supprimé du magasin")
        return self._seller_list




# mon_magasin.add_vehicle(my_car)

# print(mon_magasin.stock)
# print(mon_magasin.inventory)

# mon_magasin.delete_vehicle(Voiture("Hiaris","Toyota","Rouge",20000, 20))

# print(mon_magasin.stock)
# print(mon_magasin.inventory)

# print(mon_magasin.get_vehicle_brand_count("Toyota"))

@dataclass
class Seller():
    full_name: str
    _magasin: Magasin
    _liste_de_vente: list = field(default_factory=list)
    senior: bool = False

    @property
    def liste_de_vente(self) -> list:
        return self._liste_de_vente

    @property
    def magasin(self) -> Magasin:
        return self._magasin

    def create_sale(self,vehicule,client,reduction_asked=False):
        if reduction_asked & self.senior:
            sale = Vente(self._magasin,vehicule,self,client,True)
        else:
            sale = Vente(self._magasin,vehicule,self,client,False)
        self._liste_de_vente.append(sale)
        self._magasin.delete_vehicle(vehicule)
        return sale



@dataclass
class Client:
    nom : str
    email : str
    id : int

@dataclass
class Vente:
    magasin : Magasin
    vehicule : Vehicule
    vendeur : Seller
    client : Client
    reduction : bool

    def create_pdf(self):
        print(f"Facture au format PDF pour une {self.vehicule.marque} {self.vehicule.couleur} à {self.vehicule.final_price(self.reduction)} par {self.vendeur.full_name}")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 16)
        pdf.cell(60, 10, "Facture", 'C')
        pdf.ln(20)
        pdf.cell(60, 10, f"Voiture: {self.vehicule.marque} {self.vehicule.couleur} à {self.vehicule.final_price(self.reduction)} euros")
        pdf.ln(20)
        pdf.cell(60, 10, f"Vendeur: {self.vendeur.full_name}")
        pdf.output(f'Facture_{self.vehicule.marque}.pdf', 'F')
        return "PDF"


mon_magasin = Magasin("Rue Barthelemy Delespaul","084948384")
#my_seller = Seller("Denis",mon_magasin, senior=True)
my_car = Voiture("Hiaris","Toyota","Rouge",10000, 20)
my_client = Client("Fabien","fb",89)

mon_magasin.add_vehicle(my_car)
mon_magasin.add_seller("Denis",True)

my_sale = mon_magasin._seller_list[0].create_sale( my_car, my_client,True)
print(my_sale)
my_sale = mon_magasin._seller_list[0].create_sale( my_car, my_client,True)
# my_sale.create_pdf()
print(mon_magasin.inventory)


