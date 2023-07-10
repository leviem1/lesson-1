docker run --rm -v %cd%:/usr/src/app -w /usr/src/app python:3.11-alpine sh -c ^
"pip install -rrequirements.txt > /dev/null && python app/__init__.py"