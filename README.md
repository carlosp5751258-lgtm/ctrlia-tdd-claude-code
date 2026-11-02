# TDD con Claude Code: rojo, verde y refactor

[Read in English](README.en.md)

English version: [README.en.md](README.en.md) (archivos en `en/`).

Un ejemplo real en Python para practicar TDD con Claude Code: los prompts de cada fase, el código de partida (`raise NotImplementedError`), los tests que escribió Claude, la solución verde y el bloque para tu CLAUDE.md. Durante la fase verde los tests quedan bloqueados con una regla de permisos y git comprueba que no se tocaron.

- Receta en español: https://ctrlia.dev/recetas/tdd-claude-code.html
- Recipe in English: https://ctrlia.dev/en/recetas/tdd-claude-code.html

## Qué incluye

| Ruta | Qué es |
| --- | --- |
| `ejemplo/` | El proyecto de práctica: `src/slug.py` sin implementar y `tests/test_slug.py` |
| `solucion/slug.py` | La implementación verde que escribió Claude (Haiku) |
| `prompts/rojo.txt`, `prompts/verde.txt`, `prompts/refactor.txt` | Los prompts de cada fase |
| `claude-md-tests.md` | El bloque «Tests» para el CLAUDE.md de tu proyecto |

## Cómo usarlo

Solo necesitas Python 3 (unittest viene incluido).

```bash
cd ejemplo
git init -q && git add -A && git commit -qm "test: slug (rojo)"
python3 -m unittest discover -s tests -t .     # rojo: 4 errores por NotImplementedError

# Fase verde con Claude Code y los tests bloqueados:
claude --disallowedTools "Edit(tests/**)"
# pega el contenido de ../prompts/verde.txt

# Comprobación que no depende de Claude (0 = tests intactos)
git diff --exit-code HEAD -- tests/ && echo "tests intactos"
```

Para practicar también la fase roja, borra `tests/test_slug.py` (deja `tests/__init__.py`) y usa `prompts/rojo.txt`. Para ver el verde sin gastar nada: `cp ../solucion/slug.py src/slug.py`.

## Qué se probó

Con Claude Code **2.1.316** en Linux y `claude -p --model haiku`: la fase roja escribió estos 4 tests, la fase verde con `--disallowedTools "Edit(tests/**)"` escribió `solucion/slug.py` y `git diff --exit-code` devolvió 0. En este repositorio se comprobó con Python 3.12 que `ejemplo/` falla en rojo (4 errores por `NotImplementedError`), pasa en verde con la solución y que `slug("Árbol--de  Navidad!")` devuelve `arbol-de-navidad`. No se probaron `/goal` ni un hook `Stop`.

## Licencia

MIT. Ver [LICENSE](LICENSE).

---
Parte de **[Ctrl+IA](https://ctrlia.dev/)**: programa con Claude Code como un pro, en español. Hecho por Carlos P.
