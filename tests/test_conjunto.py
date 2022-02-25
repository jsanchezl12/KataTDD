import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())
    def test_conjunto_un_elemento(self):
        conjunto = Conjunto([5])
        self.assertEqual( conjunto.promedio(),5)
    def test_conjunto_dos_elementos(self):
        conjunto = Conjunto([5,7])
        self.assertEqual( conjunto.promedio(), 6)
    def test_conjunto_n_elementos(self):
        conjunto = Conjunto([1,2,3,4,5,6,7])
        self.assertEqual( conjunto.promedio(), (1+2+3+4+5+6+7)/7)