#!/bin/bash
#
# Hacky virtualenv launcher thing for development
#

virtualenv --prompt '(venv) ' venv
bash --rcfile <(cat << EOF
  $(cat ~/.bashrc)
  source venv/bin/activate || :
  pip install --editable . || exit 1
EOF)
