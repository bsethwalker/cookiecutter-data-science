# Getting started

## Package Installation
This project uses [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/index.html) 
for package and virtual environment management. By default the virtual environment
is not placed in the project directory. To override this behavior, set the 
`PIPENV_VENV_IN_PROJECT` environment variable, as follows in your `.zshrc` or `.bashrc`
file, depending on which terminal you're using. 

```
export PIPENV_VENV_IN_PROJECT=1
```

To install the package and all dependencies run: 
```
pipenv install 
```
from within the project directory. 