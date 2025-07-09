# Demo App for RustCI Pipeline

This is a tiny Python project demonstrating how to set up a 6‑job `.rustci.yml` file
that RustCI can run end‑to‑end: install, lint, test.

To try locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flake8 .
pytest
mypy app
sphinx-build -b html docs/ build/html
python -m build
```
