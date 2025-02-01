# study-python

Study of Python

- `tutorial/` ... Python official tutorial
- `packages/` ... Tutorial for 3rd party packages
- `playground/` ... Small projects

## Environment

- Python 3.11.4
    - [Release](https://www.python.org/downloads/release/python-3114/)
        - Resolve SSL error on installation by: [pyenv/Troubleshooting/FAQ/Suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
- venv
- pip 23.1.2

List of packages (`pip list --format freeze`)

```
black==24.10.0
click==8.1.8
iniconfig==2.0.0
isort==5.13.2
mypy==1.4.1
mypy-extensions==1.0.0
packaging==23.1
pathspec==0.12.1
pip==23.1.2
pip-licenses==5.0.0
platformdirs==4.3.6
pluggy==1.2.0
prettytable==3.13.0
pytest==7.4.0
PyYAML==6.0
setuptools==65.5.0
tomli==2.2.1
types-PyYAML==6.0.12.10
typing_extensions==4.6.3
wcwidth==0.2.13
```

## License

Following licenses are applied for each sub-project.

- `tutorial/`: Python Software Foundation License (PSFL)
- `packages/`
    - `mypy/`: MIT License
    - `pytest/`: MIT License
- `playground/`: Unlicense

Source codes in following directories are based on the contents in each reference:

- `tutorial/`: [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- `packages/mypy/`: [mypy documentation](https://mypy.readthedocs.io/en/stable/index.html)
- `packages/pytest/`: [pytest documentation](https://docs.pytest.org/en/7.4.x/index.html)

and following changes are included:

- Changes for coding style
- Comments
- Modification for the project structure

Copyright for non-modified parts belongs to the original author.

This project uses various third-party packages.
The licenses for these packages can be found in the `licenses/` directory.
