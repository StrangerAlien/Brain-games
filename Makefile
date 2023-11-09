install:
	poetry install

brain-games:
	poetry run brain-games

package-install:
	python3 -m pip install --user dist/*.whl