.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

run:
	export FLASK_APP=run.py
	export FLASK_DEBUG=1
	python -m flask run

install:
	pip install -r requirements.txt
