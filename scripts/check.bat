docker run --rm -v %cd%:/usr/src/app -w /usr/src/app python:3.11-alpine sh -c ^
"pip install tox -rrequirements.txt -rtest-requirements.txt > /dev/null && tox -e py311"