# lint the codebase
lint:
	# TODO: need to work on fixing warnings
	pylint meshtastic_mqtt/*.py

upload:
	# generate token in pypi
	rm -rf dist/
	pip install twine
	pip install build
	python -m build --sdist --wheel --outdir dist/ .
	twine upload dist/*
