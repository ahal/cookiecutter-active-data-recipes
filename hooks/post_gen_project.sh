#!/usr/bin/env bash

function dump_help() {
cat << EOF

Project setup complete!

Take a look at your project's README for information on how to
use it. You can also look at the 'What to Do Next' section of the
cookiecutter README:

https://github.com/ahal/cookiecutter-active-data-recipes
EOF
}

if ! [ -x "$(command -v poetry)" ]; then
  while true; do
    read -p "Poetry not found, would you like to install it? [Y/n] " yn
    case $yn in
      [Yy]* ) curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python; break;;
      [Nn]* ) echo "Skipped generating poetry.lock."; dump_help; exit;;
      * ) echo "Enter 'y' or 'n'.";;
    esac
  done
fi

echo "Generating poetry.lock."
poetry lock
dump_help
