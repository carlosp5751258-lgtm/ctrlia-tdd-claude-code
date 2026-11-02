import unittest

from src.slug import slug


class SlugTests(unittest.TestCase):
    def test_strips_accents_and_turns_enye_into_ascii(self):
        self.assertEqual(slug("Canción Ñandú 2026"), "cancion-nandu-2026")

    def test_collapses_repeated_and_edge_spaces(self):
        self.assertEqual(slug("  Hello   World  "), "hello-world")

    def test_removes_punctuation(self):
        self.assertEqual(slug("¿Qué tal?"), "que-tal")

    def test_empty_string_returns_empty(self):
        self.assertEqual(slug(""), "")
