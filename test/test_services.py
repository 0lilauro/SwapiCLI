import unittest

from controller.swapi_controller import SwapiController


class VerifySwappiController(unittest.TestCase):
    def test_instance_t(self):
             # Arrange
        frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"
      
        # Act
        frase_eh_pangrama = verificar_pangrama(frase)
        
        # Assert
        self.assertEqual(True, frase_eh_pangrama)