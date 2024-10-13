full-install: install build publish package-install

install:
	poetry install
	
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games