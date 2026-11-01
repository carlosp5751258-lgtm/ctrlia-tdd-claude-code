import re
import unicodedata


def slug(texto: str) -> str:
    ascii_texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_texto.lower()).strip("-")
