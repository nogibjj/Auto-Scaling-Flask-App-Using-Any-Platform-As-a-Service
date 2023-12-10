install:
	sudo apt-get update
	sudo apt-get install -y python3-dev portaudio19-dev
	pip install --upgrade pip
	pip install --no-cache-dir -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:
	black *.py 

lint:
	# Disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# Ruff linting is 10-100X faster than pylint
	ruff check *.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# Deploy goes here

all: install lint test format deploy

job:
	python run_job.py