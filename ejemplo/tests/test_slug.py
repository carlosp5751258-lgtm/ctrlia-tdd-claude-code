import unittest

from src.slug import slug


class SlugTests(unittest.TestCase):
    def test_quita_acentos_y_convierte_nh_a_ascii(self):
        self.assertEqual(slug("Canción Ñandú 2026"), "cancion-nandu-2026")

    def test_colapsa_espacios_repetidos_y_bordes(self):
        self.assertEqual(slug("  Hola   Mundo  "), "hola-mundo")

    def test_elimina_signos_de_puntuacion(self):
        self.assertEqual(slug("¿Qué tal?"), "que-tal")

    def test_cadena_vacia_devuelve_vacia(self):
        self.assertEqual(slug(""), "")
