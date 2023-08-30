# frictionless-dataframe

- [x] poetry (devcontainer feature)
  - `pip install poetry`
  - Add packages (flag for development): `poetry add --group dev`
  - Install packages for production: `poetry install --only main`
  - Install packages directly on the system (not in venv): `poetry config virtualenvs.create false --local`
  - Use venv in project: `poetry config virtualenvs.in-project true --local`
- [x] Pytest
  - `poetry add --group dev pytest`
  - `poetry run pytest`
- [x] Black (vscode extension)
  - `poetry add --group dev black`
  - `poetry run black .`
- [x] Ruff (vscode extension)
  - `poetry add --group dev ruff`
  - `poetry run ruff check .`
- [x] MyPy type checker (vscode extension)
  - `poetry add --group dev mypy`
  - `poetry run mypy .`
