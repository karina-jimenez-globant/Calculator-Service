
VENV_ACTIVATE=. venv/bin/activate
PYTHON=venv/bin/python2.7

venv: ven/bin/activate
ven/bin/activate: requirements.txt
	test -d ven || virtualenv venv
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

run: venv
	${PYTHON} run_app.py

test: venv
	${PYTHON} -m pytest -v
