# project_demo
This is a demo project to give a tutorial on how to publish projects with Poetry and PyPi. This is for the same.

## Installations
```bash
pip install pyenv
pip install poetry
```
## Set up project with Poetry

Follow the tutorial the [tutorial link](https://medium.com/p/ed12e1c82833/edit) on medium.

## Add libaries
To add a new library: library_name to your project, use poetry command `poetry add`
```bash
poetry add <library_name>
poetry update
```

## Remove libraries
To remove a library: library_name to your project, use poetry command `poetry remove`
```bash
poetry remove <library_name>
poetry update
```

## Install project dependencies
```bash
poetry install
```

## Running unit tests
poetry run pytest

## Generate authentication token with Pypi, test-Pypi
Add your project to Pypi and test-Pypi, and generate authentication tokens. Follow [tutorial](https://medium.com/p/ed12e1c82833/edit) on medium for these steps.

## Publish project to Pypi, test-Pypi
To publish on test-pypi as a wheel:

```bash
poetry config pypi-token.test-pypi <your-test-pypyi-token>
poetry publish --build -r test-pypi
```
To publish on pypi as a wheel:

```bash
poetry config pypi-token.pypi <your-pypyi-token>
poetry publish --build 
```


