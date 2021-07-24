#/bin/sh

set -eu

pipenv run python -m ipykernel install --user --name=python_proto
pipenv run jupyter lab
