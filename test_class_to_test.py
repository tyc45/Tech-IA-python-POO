from class_to_test import Voiture
import pytest
# Tester une classe correspond à tester chacune de ses méthodes.
# Pour cela on crée une classe de test dont le nom commence par Test 
# Chacun de ses méthodes permettra de tester les méthodes de la classe à tester


class TestVoiture:
    
    
    def test_prix_apres_reduction(self):
        assert Voiture("toyota","rouge",20000,0.1).prix_apres_reduction() == 18000

    def test_prix_apres_double_reduction(self):
        assert Voiture("toyota","rouge",20000,0.1).prix_apres_double_reduction() == 16000

    def test_prix_apres_triple_reduction(self):
        assert Voiture("toyota","rouge",20000,0.1).prix_apres_triple_reduction() == 14000
    
    def test_initialisation(self):
        assert Voiture("toyota","rouge",20000,0.1).prix == 20000
        with pytest.raises(ValueError) :
            Voiture("toyota","rouge","20000",0.1)


# Je dois créer trois fois ma voiture. C'est plutot embettant. 

# Je peux préférer utiliser des fixtures

@pytest.fixture
def voiture_test():
   return Voiture("toyota","rouge",20000,0.1)


class TestVoiture2():
    def test_prix_apres_reduction(self,voiture_test):
        assert voiture_test.prix_apres_reduction() == 18000

    def test_prix_apres_double_reduction(self,voiture_test):
        assert voiture_test.prix_apres_double_reduction() == 16000

    def test_prix_apres_triple_reduction(self,voiture_test):
        assert voiture_test.prix_apres_triple_reduction() == 14000 

    def test_initialisation(self, voiture_test):
        assert voiture_test.prix == 20000
        with pytest.raises(ValueError) :
            Voiture("toyota","rouge","20000",0.1)
