#!/bin/sh

pip_version=$(pip --version)
echo "Usando a versão do pip: $pip_version"

pip install --upgrade git+https://github.com/jaraco/path.py.git > path_install.log

python3 -m venv local_lib

python3 my_program.py