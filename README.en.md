# TDD with Claude Code: red, green and refactor

[Leer en español](README.md)

A real Python example to practice TDD with Claude Code: the prompts for each phase, the starting code (`raise NotImplementedError`), the tests Claude wrote, the green solution and the block for your CLAUDE.md. During the green phase the tests are locked with a permission rule and git checks they were not touched.

- Recipe in English: https://ctrlia.dev/en/recetas/tdd-claude-code.html
- Receta en español: https://ctrlia.dev/recetas/tdd-claude-code.html

## What's inside

| Path | What it is |
| --- | --- |
| `ejemplo/` | The practice project: unimplemented `src/slug.py` and `tests/test_slug.py` |
| `solucion/slug.py` | The green implementation Claude (Haiku) wrote |
| `prompts/rojo.txt`, `prompts/verde.txt`, `prompts/refactor.txt` | The prompts for each phase (red, green, refactor), in Spanish |
| `claude-md-tests.md` | The "Tests" block for your project's CLAUDE.md, in Spanish |

## How to use it

You only need Python 3 (unittest is built in).

```bash
cd ejemplo
git init -q && git add -A && git commit -qm "test: slug (rojo)"
python3 -m unittest discover -s tests -t .     # red: 4 errors from NotImplementedError

# Green phase with Claude Code and the tests locked:
claude --disallowedTools "Edit(tests/**)"
# paste the contents of ../prompts/verde.txt

# Check that does not depend on Claude (0 = tests untouched)
git diff --exit-code HEAD -- tests/ && echo "tests intactos"
```

To practice the red phase too, delete `tests/test_slug.py` (keep `tests/__init__.py`) and use `prompts/rojo.txt`. To see green without spending anything: `cp ../solucion/slug.py src/slug.py`.

## What was tested

With Claude Code **2.1.316** on Linux and `claude -p --model haiku`: the red phase wrote these 4 tests, the green phase with `--disallowedTools "Edit(tests/**)"` wrote `solucion/slug.py`, and `git diff --exit-code` returned 0. In this repository we checked with Python 3.12 that `ejemplo/` fails in red (4 errors from `NotImplementedError`), passes in green with the solution, and that `slug("Árbol--de  Navidad!")` returns `arbol-de-navidad`. `/goal` and a `Stop` hook were not tested.

## License

MIT. See [LICENSE](LICENSE).

---
Part of **[Ctrl+IA](https://ctrlia.dev/en/)**: code with Claude Code like a pro. Made by Carlos P.
