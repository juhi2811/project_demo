# project_demo
This is a demo project to give a tutorial on how to publish projects using Poetry and PyPi.

## Installations
```bash
pip install pyenv
pip install poetry
```
## Setting up project with Poetry

I have described setting up a project with Poetry commands in the medium tutorial. Follow the [tutorial](https://medium.com/p/ed12e1c82833/edit) on medium.

## Adding libaries
To add a new library: library_name to your project, use poetry command `poetry add`
```bash
poetry add <library_name>
poetry update
```

## Removing libraries
To remove a library: library_name to your project, use poetry command `poetry remove`
```bash
poetry remove <library_name>
poetry update
```

## Installing project dependencies
```bash
poetry install
```

## Running unit tests
```bash
poetry run pytest
```

## Generating authentication token with Pypi, test-Pypi
Add your project to Pypi and test-Pypi, and generate authentication tokens. Follow [tutorial](https://medium.com/p/ed12e1c82833/edit) on medium for these steps.

## Publish project to Pypi, test-Pypi
To publish on test-pypi as a package wheel:

```bash
poetry config pypi-token.test-pypi <your-test-pypyi-token>
poetry publish --build -r test-pypi
```
To publish on pypi as a package wheel:

```bash
poetry config pypi-token.pypi <your-pypyi-token>
poetry publish --build 
```
## Installing and using published project
Now that you have published your package on Pypi, you can install in using pip

```bash
pip install project-demo-juhi
```
After installation, you can import the project package as 
```python
import project-demo-juhi
```


